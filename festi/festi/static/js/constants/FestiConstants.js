var keyMirror = function(obj) {
  var ret = {};
  var key;
  if (!(obj instanceof Object && !Array.isArray(obj))) {
    throw new Error('keyMirror(...): Argument must be an object.');
  }
  for (key in obj) {
    if (!obj.hasOwnProperty(key)) {
      continue;
    }
    ret[key] = key;
  }
  return ret;
};

FestiConstants = keyMirror({
    ACTION_OPEN_SIGNIN: null,
    ACTION_CLOSE_SIGNIN: null,
    ACTION_SIGN_IN_FB: null,
    ACTION_SIGN_OUT_FB: null,
    ACTION_CHECK_FB_AUTH: null,
    ACTION_CHANGE_AUTH_STATUS: null,
    STATE_FB_AUTH_NONE: null,
    STATE_FB_AUTH_CONNECTED: null,
    STATE_FB_AUTH_NOT_AUTHORIZED: null,
    STATE_FB_AUTH_ELSE: null,
    EVENT_CHANGE: null,
});
