import whisper
import json

model = whisper.load_model("small") # large-v2

result = model.transcribe(audio="audios/13_Entities, Code tag and more on HTML.mp3",
                          language="hi",
                          task="translate",
                          word_timestamps=False)

print(result["segments"])

chunks = []
for segment in result["segments"]:
    chunks.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    })
    
print(chunks)

with open("output1.json", "w") as f:
    json.dump(chunks, f)