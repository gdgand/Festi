var SurveyApp = React.createClass({
    render: function () {
        return (
            <div>
                <Header />
                <div className="container body-container">
                    <Facebook />
                </div>
                <Footer />
            </div>
        );
    }
})

React.render(
    <SurveyApp />,
    document.body
);