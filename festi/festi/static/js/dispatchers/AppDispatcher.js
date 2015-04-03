var AppDispatcher = React.addons.update(Dispatcher.prototype, {

    $merge: {
        handleViewAction: function (action) {
            this.dispatch({
                source: 'VIEW_ACTION',
                action: action
            });
        }
    }
});