# instalar openai-whisper
# instalar ffmpeg

import whisper

modelo = whisper.load_model("base")

resposta=modelo.transcribe("andreia-chociai.mp3")

print(resposta)

