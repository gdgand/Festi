var Header = React.createClass({
    render: function () {
        return (
            <div className="navbar navbar-default navbar-fixed-top">
                <div className="container">
                    <div className="navbar-header">
                        <a className="navbar-brand" href="/survey">Survey</a>
                    </div>
                    <div className="navbar-right">
                        <button type="button" className="btn btn-primary navbar-btn" onClick={this._signin}>
                            Sign in
                        </button>
                    </div>
                </div>
            </div>
        );
    },

    _signin: function () {
        FestiActions.openSignIn();
    }
});

var Footer = React.createClass({
    render: function () {
        return (
            <footer className="footer">
                <div className="container">
                    <p className="text-muted">&copy; GDG Korea</p>
                </div>
            </footer>
        );
    }
});

var Facebook = React.createClass({
    getInitialState: function () {
        return this._getFestiSession();
    },

    componentDidMount: function () {
        FestiStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function () {
        FestiStore.removeChangeListener(this._onChange);
    },

    render: function () {
        var style = {};
        style.visibility = this.state.visibility;

        return (
            <div className="panel panel-default login" style={style}>
                <div className="panel-heading">
                    <h3 className="panel-title">Sign in
                        <button type="button" className="close" aria-label="Close" onClick={this._close}>
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </h3>
                </div>
                <div className="panel-body">
                    <button type="button" className="btn btn-primary btn-lg">Sign in with Facebook</button>
                </div>
            </div>
        );
    },

    _getFestiSession: function () {
        return {
            visibility: FestiStore.isSignInOpen() ? 'visible' : 'hidden'
        };
    },

    _close: function () {
        FestiActions.closeSignIn();
    },

    _onChange: function () {
        this.setState(this._getFestiSession());
    }
});