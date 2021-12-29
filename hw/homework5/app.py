from flask import *

from model import generate_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sample = "Write a restaurant review based on these notes:\n\nexample:\nName: The Blue Wharf\nLobster great, noisy, service polite, prices good.\n\nReview:"
    generated_text = ""
    # TODO
    # 1) if get: show
    # 2) if post: 
    #       if input == '':
    #           generate_text(sample)
    #       else:
    #           generate_text(user_input)

    # generated_text = generate_text(user_input)

    return render_template('index.html', place_holder=sample, generated_text=generated_text)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)