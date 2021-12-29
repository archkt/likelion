from flask import *

from model import generate_text

app = Flask(__name__)

SAMPLE = "Write a restaurant review based on these notes:\n\nexample:\nName: The Blue Wharf\nLobster great, noisy, service polite, prices good.\n\nReview:"

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generate():
    generated_text = ""
    input_text = request.form["input_text"]
    #print(input_text)
    if input_text == '':
        generated_text = generate_text(SAMPLE)
    else:
        generated_text = generate_text(input_text)
        
    return jsonify({'place_holder':SAMPLE, 'generated_text':generated_text, 'msg':'POST call success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)