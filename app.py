from flask import Flask,render_template,request
from summerizer import summerizer

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary,og,len_og,len_summary=summerizer(rawtext)
    return render_template('summary.html',summary=summary,og=og,len_og=len_og,len_summary=len_summary)

if __name__=="__main__":
    app.run(debug=True)
