# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
openai.api_key = ""

def transcribe_audio():
    audio_file= open(r".\media\temp_audio.mp4", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']


def summarise_recording():
    text= transcribe_audio()
    with open(r".\media\temp_transcript.txt","w") as txt_file:
        txt_file.write(text) 
    prompt= f"Summarize the following text in a numerical point wise manner:\n{text}"
    completion = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0.7,
                                        max_tokens= 500,
                                        top_p= 1.0,
                                        frequency_penalty= 0.0,
                                        presence_penalty=1)

    return completion.choices[0].text.strip("\n")