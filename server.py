from flask import Flask, request, jsonify, render_template
from audio_transcription import summarise_recording, bot_response
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

chat_history= []

@app.route('/')
def index():
    chat_history= []
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save(r".\media\temp_audio.mp4")
        recording_summary = summarise_recording()
        with open(r".\media\temp_transcript.txt","r") as txt_file:
            prompt_dict = {"role": "system", 
            "content": f"""You are a virtual assistant. Below text is the transcription of a video. 
                        You will answer user's questions regarding the video using this transcription.\nTranscript:{txt_file.read()}"""}
            chat_history.append(prompt_dict)
        return jsonify({"summary": recording_summary})
    else:
        error = 'Some Error Occured!'
        return jsonify({'error': error})


@app.route('/chatbot', methods=['POST'])
def chatbot():
    input_text = request.json['input_text']
    prompt_dict = {"role": "user", "content": f"""Answer below question in not more than 60 words.
                                    If this question is irrrelevant to this video, then reply "Sorry. This question is not relevant to the video".
                                     Ask clarifying question if necessary.\n{input_text.strip()}"""}
    chat_history.append(prompt_dict)
    print(chat_history)
    response= bot_response(chat_history)
    prompt_dict = {"role": "assistant", "content": f"{response.strip()}"}
    chat_history.append(prompt_dict)
    print(chat_history)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='localhost',port='5100')