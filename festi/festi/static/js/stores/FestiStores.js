window.fbAsyncInit = function () {
    FB.init({
        appId: '791867294202589',
        cookie: true,
        xfbml: true,
        version: 'v2.2'
    });

    FestiActions.checkFbAuth();
};

(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

var _FestiStore = {
    isSignInOpen: false,
    fbAuthState: FestiConstants.STATE_FB_AUTH_NONE,

    changeAuthStatus: function (responseStatus) {
        if (responseStatus == 'not_authorized') {
            _FestiStore.fbAuthState = FestiConstants.STATE_FB_AUTH_NOT_AUTHORIZED;
            _FestiStore.isSignInOpen = false;
        } else if (responseStatus == 'connected') {
            _FestiStore.fbAuthState = FestiConstants.STATE_FB_AUTH_CONNECTED;
            _FestiStore.isSignInOpen = false;
        } else {
            _FestiStore.fbAuthState = FestiConstants.STATE_FB_AUTH_ELSE;
            _FestiStore.isSignInOpen = false;
        }
    },

    processResponseCode: function (response) {
        FestiActions.changeAuthStatus(response.status);
    },

    checkFbAuth: function () {
        FB.getLoginStatus(this.processResponseCode);
    }
};

var FestiStore = React.addons.update(EventEmitter.prototype, {
    $merge: {
        isSignInOpen: function () {
            return _FestiStore.isSignInOpen;
        },

        getFbAuthState: function () {
            return _FestiStore.fbAuthState;
        },

        emitChange: function () {
            this.emitEvent(FestiConstants.EVENT_CHANGE);
        },

        addChangeListener: function (callback) {
            this.on(FestiConstants.EVENT_CHANGE, callback);
        },

        removeChangeListener: function (callback) {
            this.removeListener(FestiConstants.EVENT_CHANGE, callback);
        }
    }
});

AppDispatcher.register(function (payload) {
    var action = payload.action;

    switch (action.actionType) {
        case FestiConstants.ACTION_OPEN_SIGNIN:
            _FestiStore.isSignInOpen = true;
            break;

        case FestiConstants.ACTION_CLOSE_SIGNIN:
            _FestiStore.isSignInOpen = false;
            break;

        case FestiConstants.ACTION_CHECK_FB_AUTH:
            _FestiStore.checkFbAuth();
            break;

        case FestiConstants.ACTION_SIGN_IN_FB:
            FB.login(_FestiStore.processResponseCode);
            break;

        case FestiConstants.ACTION_SIGN_OUT_FB:
            FB.logout(_FestiStore.processResponseCode);
            break;

        case FestiConstants.ACTION_CHANGE_AUTH_STATUS:
            _FestiStore.changeAuthStatus(action.statusCode);
            break;

        default:
            return true;
    }

    FestiStore.emitChange();

    return true;
});