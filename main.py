import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")
print(df)


@app.route("/")
def home():
    return render_template("translators.html")





@app.route("/api/v1/<word>")
def about(word):
    definition = df.loc[df["word"]==word]["definition"].squeeze()

    return {
        "word": word,
        "discription": definition,
    }

if __name__ == "__main__":
    app.run(debug=True)