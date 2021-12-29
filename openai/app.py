from flask import *
import os
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        response = openai.Completion.create(
        engine="davinci",
        prompt=request.form['msg'],
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        
        user_msg = request.form['msg'] + response["choices"][0]["text"]
    else:
        user_msg = "Create an outline for an essay about Walt Disney and his contributions to animation:\n\nI: Introduction"

    return render_template("index.html", output_msg = user_msg)


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)