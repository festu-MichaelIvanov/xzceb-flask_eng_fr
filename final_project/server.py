import json

from flask import Flask, render_template, request

from machinetranslation import translator


app = Flask("Web Translator")


@app.route("/english-to-french")
def engish_to_french():
    return translator.english_to_french(
        english_text=request.args.get('text_to_translate')
    )


@app.route("/french-to-english")
def frenchToEnglish():
    return translator.french_to_english(
        french_text=request.args.get('text_to_translate')
    )


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
