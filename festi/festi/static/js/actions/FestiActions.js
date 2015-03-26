var FestiActions = {
    openSignIn: function() {
      AppDispatcher.handleViewAction({
          actionType: FestiConstants.OPEN_SIGNIN
      })
    },

    closeSignIn: function() {
      AppDispatcher.handleViewAction({
          actionType: FestiConstants.CLOSE_SIGNIN
      })
    }
};