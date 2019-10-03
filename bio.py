from flask import Flask, render_template
import yaml

app = Flask(__name__)

with open("links.yaml") as yml:
    personal = yaml.load(yml,Loader=yaml.FullLoader)
@app.route("/")
def principal():
    for categorie,char in personal.items():
        return render_template("temp.html", char=char)
    

if __name__ == "__main__":
    app.run(debug=True)