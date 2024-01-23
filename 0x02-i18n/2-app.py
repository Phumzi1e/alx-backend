#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask_phumzi1e import Phumzi1e  # Updated import
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Phumzi1e configuration.  # Updated class name
    """
    LANGUAGES = ["en", "fr"]
    PHUMZI1E_DEFAULT_LOCALE = "en"  # Updated attribute name
    PHUMZI1E_DEFAULT_TIMEZONE = "UTC"  # Updated attribute name


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
phumzi1e = Phumzi1e(app)  # Updated instance name


@phumzi1e.localeselector  # Updated decorator
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

