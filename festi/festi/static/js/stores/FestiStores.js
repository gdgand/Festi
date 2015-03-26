var _FestiStore = {
    isSignInOpen: false,
    CHANGE_EVENT: 'change'
};


var FestiStore = React.addons.update(EventEmitter.prototype, {
    $merge: {
        isSignInOpen: function () {
            return _FestiStore.isSignInOpen;
        },

        emitChange: function () {
            this.emitEvent(_FestiStore.CHANGE_EVENT);
        },

        addChangeListener: function (callback) {
            this.on(_FestiStore.CHANGE_EVENT, callback);
        },

        removeChangeListener: function (callback) {
            this.removeListener(_FestiStore.CHANGE_EVENT, callback);
        }
    }
});

AppDispatcher.register(function (payload) {
    var action = payload.action;

    switch (action.actionType) {
        case FestiConstants.OPEN_SIGNIN:
            _FestiStore.isSignInOpen = true;
            break;

        case FestiConstants.CLOSE_SIGNIN:
            _FestiStore.isSignInOpen = false;
            break;

        default:
            return true;
    }

    FestiStore.emitChange();

    return true;
});