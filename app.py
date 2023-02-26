from flask import Flask, render_template, request

app = Flask(__name__)

# Define some example words for our application
nouns = ["cat", "dog", "apple", "banana", "car"]
verbs = ["runs", "jumps", "eats", "drives", "sleeps"]
adjectives = ["happy", "sad", "funny", "tall", "short"]
adverbs = ["quickly", "slowly", "loudly", "softly", "gently"]


@app.route("/")
def index():
    # Render the main page with a form to choose words
    return render_template("index.html", nouns=nouns, verbs=verbs, adjectives=adjectives, adverbs=adverbs)


@app.route("/sentence", methods=["POST"])
def sentence():
    # Get the user's selected words from the form data
    selected_noun = request.form.get("noun", "apple")
    selected_verb = request.form.get("verb", "sleeps")
    selected_adjective = request.form.get("adjective", "happy")
    selected_adverb = request.form.get("adverb", "softly")

    # Build a sentence using the selected words
    sentence = f"The {selected_adjective} {selected_noun} {selected_verb} {selected_adverb}."

    # Render the sentence page with the generated sentence
    return render_template("sentence.html", sentence=sentence)


if __name__ == "__main__":
    app.run(debug=True)
