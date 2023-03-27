from flask import Flask, request, jsonify, render_template
from audio_transcription import summarise_recording
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

recording_summary= ""

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save(r".\media\temp_audio.mp4")
        recording_summary = summarise_recording()
        return jsonify({"summary": recording_summary})
    else:
        error = 'Some Error Occured!'
        return jsonify({'error': error})


@app.route('/chatbot')
def chatbot():
    message = request.args.get('message', '')
    # Handle chatbot logic here
    response = "Hello! How can I help you?"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='localhost',port='5100')