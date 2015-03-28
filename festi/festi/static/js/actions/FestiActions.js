var FestiActions = {
    openSignInPanel: function () {
      AppDispatcher.handleViewAction({
          actionType: FestiConstants.ACTION_OPEN_SIGNIN,
      })
    },

    closeSignIn: function () {
      AppDispatcher.handleViewAction({
          actionType: FestiConstants.ACTION_CLOSE_SIGNIN,
      })
    },

    checkFbAuth: function () {
        AppDispatcher.handleViewAction({
            actionType: FestiConstants.ACTION_CHECK_FB_AUTH,
        })
    },

    signInFb: function () {
        AppDispatcher.handleViewAction({
            actionType: FestiConstants.ACTION_SIGN_IN_FB,
        })
    },

    signOutFb: function () {
        AppDispatcher.handleViewAction({
            actionType: FestiConstants.ACTION_SIGN_OUT_FB,
        })
    },

    changeAuthStatus: function (statusCode) {
        AppDispatcher.handleViewAction({
            actionType: FestiConstants.ACTION_CHANGE_AUTH_STATUS,
            statusCode: statusCode
        })
    }
};