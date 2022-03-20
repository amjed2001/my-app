from flask import Flask,render_template, jsonify,request,redirect,url_for
from textblob import TextBlob

app = Flask(__name__)
@app.route("/")
def begining():
    return render_template("begining.html")

@app.route("/more_information")
def more_information():
    return render_template("info.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/home")
def home():
    title="test if your sentiment is positive or negative"
    return render_template("home.html",title=title)
   
@app.route("/sentiment",methods=["POST"])
def sentiment():
    your_text=request.form.get("your_text")
    title="thank you for visiting my website"
    inter=interp(your_text)
    return render_template("sentiment.html",title=title,your_text=your_text,inter=inter)

def interp(txt):
    num=float(sent(txt))
    if num>0 :
        return "  you have a positive emotion"
    else:
        return "  you have a negative emotion"

def sent(txt) :   
    text =str(txt)
    blob = TextBlob(text)
    blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

    blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

    for sentence in blob.sentences:
        return sentence.sentiment.polarity

    
app.run(debug=True,port=9000)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method=='POST':
        data = request.json
        text = data['text']
        return text
    return "this is a response from a get request"


