from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        """
        The homepage of the website, which just renders the index.html template.
        """
        return render_template('index.html')

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=False)