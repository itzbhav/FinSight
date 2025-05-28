import pyttsx3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
engine = pyttsx3.init()

class SpeakRequest(BaseModel):
    text: str

@app.post("/speak")
def speak_text(data: SpeakRequest):
    engine.say(data.text)
    engine.runAndWait()
    return {"status": "spoken"}
