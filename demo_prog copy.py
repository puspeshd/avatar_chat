import openai
import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
openai.api_key = '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'

def gpt4_response(prompt_text):
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text},
        ]
    )
    message = response['choices'][0]['message']['content']
    return message.strip()

print("You can start speaking now...")

while True:
    with sr.Microphone() as source:
        # Adjust recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for speech...")
        try:
            # Speech recognition with a timeout
            audio_data = recognizer.listen(source, timeout=5)
            print("Processing speech...")
            text_input = recognizer.recognize_google(audio_data)
            print(f"Recognized speech: {text_input}")

            # Simulate GPT-4 response for now
            #response_text = gpt4_response(text_input)
            response_text="SAUMI do your studies  otherwise you would fail"
            print(f"GPT-4 response: {response_text}")

            # Text-to-Speech output
            tts_engine.say(response_text)
            tts_engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
