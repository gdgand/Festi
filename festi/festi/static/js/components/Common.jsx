var Header = React.createClass({
    getInitialState: function () {
        return this._getSession();
    },

    componentDidMount: function () {
        FestiStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function () {
        FestiStore.removeChangeListener(this._onChange);
    },

    render: function () {
        var text, task;
        if (this.state.fbAuthState == FestiConstants.STATE_FB_AUTH_NONE) {
            text = '';
            task = null;
        } else if (this.state.fbAuthState == FestiConstants.STATE_FB_AUTH_CONNECTED) {
            text = 'Sign out';
            task = this._signOut;
        } else {
            text = 'Sign in';
            task = this._openSignInPanel;
        }

        return (
            <div className="navbar navbar-default navbar-fixed-top">
                <div className="container">
                    <div className="navbar-header">
                        <a className="navbar-brand" href="/survey">Survey</a>
                    </div>
                    <div className="navbar-right">
                        <button type="button" className="btn btn-primary navbar-btn" onClick={task}>
                        {text}
                        </button>
                    </div>
                </div>
            </div>
        );
    },

    _signOut: function () {
        FestiActions.signOutFb();
    }
    ,

    _openSignInPanel: function () {
        FestiActions.openSignInPanel();
    },

    _getSession: function () {
        return {
            fbAuthState: FestiStore.getFbAuthState(),
        };
    },

    _onChange: function () {
        this.setState(this._getSession());
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
        return this._getSession();
    },

    componentDidMount: function () {
        FestiStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function () {
        FestiStore.removeChangeListener(this._onChange);
    },

    render: function () {
        var style = {
            visibility: this.state.visibility
        };

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
                    <button type="button" className="btn btn-primary btn-lg" onClick={this._signIn}>
                        Sign in with Facebook
                    </button>
                </div>
            </div>
        );
    },

    _signIn: function () {
      FestiActions.signInFb();
    },

    _getSession: function () {
        return {
            visibility: FestiStore.isSignInOpen() ? 'visible' : 'hidden',
            fbAuthState: FestiStore.getFbAuthState()
        };
    },

    _close: function () {
        FestiActions.closeSignIn();
    },

    _onChange: function () {
        this.setState(this._getSession());
    }
});