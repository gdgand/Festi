# coding: utf8
import json
from django import forms
from django.forms import Widget
from django.forms.utils import flatatt
from django import utils
import copy


class SplitJSONWidget(forms.Widget):

    def __init__(self, attrs=None, sep='__', debug=False):
        self.separator = sep
        self.debug = debug
        super(SplitJSONWidget, self).__init__(attrs)

    def _as_text_field(self, name, key, value, is_sub=False, is_readonly=False, is_hidden=False, answer_type=None):
        value = utils.encoding.force_unicode(value)

        attrs = self.build_attrs(self.attrs, type='text', name='%s%s%s' % (name, self.separator, key))
        attrs['id'] = attrs.get('name', None)
        attrs['class'] = 'form-control'
        if is_readonly:
            attrs['readonly'] = 'readonly'
            attrs['tabindex'] = '-1'
        if is_hidden:
            attrs['type'] = 'hidden'

        tag = u'<label for="%s">%s</label>' % (attrs['id'], key)
        if answer_type == 'textarea':
            tag = u'<textarea %s>%s</textarea>' % (flatatt(attrs), value)
        else:
            attrs['value'] = utils.encoding.force_unicode(value)
            tag = u'<input%s />' % flatatt(attrs)

        return tag

    def _to_build(self, name, json_obj, **kwargs):
        inputs = []
        if isinstance(json_obj, list):
            _l = []
            for key, value in enumerate(json_obj):
                answer_type = None
                if isinstance(value, dict) and 'answer_type' in value:
                    answer_type = value['answer_type']

                _l.append(self._to_build('%s%s%s' % (name, self.separator, key),
                                         value, answer_type=answer_type))
            inputs.extend([_l])

        elif isinstance(json_obj, dict):
            _l = []

            question = json_obj.pop('question', None)
            if question:
                _l.append(self._to_build('%s%s%s' % (name, self.separator, 'question'), question, is_readonly=True))

            for key, value in json_obj.items():
                _l.append(self._to_build('%s%s%s' % (name, self.separator, key), value, **kwargs))

            inputs.extend([_l])

        elif isinstance(json_obj, (basestring, int)):
            name, _, key = name.rpartition(self.separator)
            if key in ('id', 'answer_type'):
                inputs.append(self._as_text_field(name, key, json_obj, is_hidden=True))
            else:
                inputs.append(self._as_text_field(name, key, json_obj, **kwargs))

        elif json_obj is None:
            name, _, key = name.rpartition(self.separator)
            inputs.append(self._as_text_field(name, key, '', **kwargs))

        return inputs

    def _prepare_as_ul(self, inputs):
        if inputs:
            result = ''
            for el in inputs:
                if isinstance(el, list) and len(inputs) == 1:
                    result += self._prepare_as_ul(el)
                elif isinstance(el, list):
                    result += '<ul>'
                    result += self._prepare_as_ul(el)
                    result += '</ul>'
                else:
                    result += '<li>%s</li>' % el
            return result
        return ''

    def _to_pack_up(self, root_node, raw_data):
        copy_raw_data = copy.deepcopy(raw_data)
        result = []

        def _to_parse_key(k, v):
            if k.find(self.separator) != -1:
                apx, _, nk = k.rpartition(self.separator)
                try:
                    # parse list
                    int(nk)
                    l = []
                    obj = {}
                    index = None
                    if apx != root_node:
                        for key, val in copy_raw_data.items():
                            head, _, t = key.rpartition(self.separator)
                            _, _, index = head.rpartition(self.separator)
                            if key is k:
                                del copy_raw_data[key]
                            elif key.startswith(apx):
                                try:
                                    int(t)
                                    l.append(val)
                                except ValueError:
                                    if index in obj:
                                        obj[index].update({t: val})
                                    else:
                                        obj[index] = {t: val}
                                del copy_raw_data[key]
                        if obj:
                            for i in obj:
                                l.append(obj[i])
                    l.append(v)
                    return _to_parse_key(apx, l)
                except ValueError:
                    # parse dict
                    d = {}
                    if apx != root_node:
                        for key, val in copy_raw_data.items():
                            _, _, t = key.rpartition(self.separator)
                            try:
                                int(t)
                                continue
                            except ValueError:
                                pass
                            if key is k:
                                del copy_raw_data[key]
                            elif key.startswith(apx):
                                d.update({t: val})
                                del copy_raw_data[key]
                    v = {nk: v}
                    if d:
                        v.update(d)
                    return _to_parse_key(apx, v)
            else:
                return v

        for k, v in raw_data.iteritems():
            if k in copy_raw_data:
                # to transform value from list to string
                v = v[0] if isinstance(v, list) and len(v) is 1 else v
                if k.find(self.separator) != -1:
                    d = _to_parse_key(k, v)
                    # set type result
                    if not len(result):
                        result = type(d)()
                    try:
                        result.extend(d)
                    except:
                        result.update(d)

        result = sorted(result, key=lambda _p: int(_p['id'])) # monkey-patch

        return result

    def value_from_datadict(self, data, files, name):
        data_copy = copy.deepcopy(data)
        result = self._to_pack_up(name, data_copy)
        return json.dumps(result)

    def render(self, name, value, attrs=None):
        try:
            value = json.loads(value)
        except TypeError:
            pass
        inputs = self._to_build(name, value or {})
        result = self._prepare_as_ul(inputs)
        if self.debug:
            # render json as well
            source_data = u'<hr/>Source data: <br/>%s<hr/>' % str(value)
            result = '%s%s' % (result, source_data)
            print result
        return utils.safestring.mark_safe(result)
