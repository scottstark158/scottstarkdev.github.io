from flask import Flask, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "This is the server. Send POST requests to /submit-inquiry."

@app.route('/submit-inquiry', methods=['POST'])
def submit_inquiry():
    data = request.form
    # You can customize the file name or format
    with open('inquiries.json', 'a') as f:
        json.dump(dict(data), f)
        f.write('\n')
    return "Inquiry received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
