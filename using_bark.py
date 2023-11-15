from bark import SAMPLE_RATE, generate_audio, preload_models

import speech_recognition as sr
import sounddevice as sd



recognizer = sr.Recognizer()
preload_models(fine_use_gpu=True)
# ... rest of your imports and your code ...

while True:
    try:
     with sr.Microphone() as source:
          # Adjust recognizer sensitivity to ambient noise
          recognizer.adjust_for_ambient_noise(source, duration=1)
          print("Listening for speech...")

          # Speech recognition with a timeout
          audio_data = recognizer.listen(source, timeout=5)
          print("Processing speech...")
          text_input = recognizer.recognize_google(audio_data)
          print(f"Recognized speech: {text_input}")

          audio_array = generate_audio(text_input)
          sd.play(audio_array, SAMPLE_RATE)
          sd.wait()  # Wait until audio is finished playing
    except:
       continue
    


