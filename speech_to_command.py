# %%
import json
import pyaudio
from vosk import Model, KaldiRecognizer

# %%
recognition_words = {
    "keywords": {
        "play": {
            "type": "action",
            "contexts": ["music", "plugs"],
            "compatible_services": ["apple music", "spotify"]
        },
        "shuffle": {
            "type": "action",
            "contexts": ["music"],
            "compatible_services": ["apple music", "spotify"]
        },
        "start": {
            "type": "action",
            "contexts": ["music", "plugs", "time"],
            "compatible_services": ["apple music", "spotify"]
        },
        "turn on": {
            "type": "action",
            "contexts": ["plugs"],
            "compatible_services": ["openhab"]
        },
        "pause": {
            "type": "action",
            "contexts": ["music"],
            "compatible_services": ["apple music", "spotify"]
        },
        "stop": {
            "type": "action",
            "contexts": ["music", "plugs", "time"],
            "compatible_services": ["apple music", "spotify"]
        },
        "turn off": {
            "type": "action",
            "contexts": ["plugs"],
            "compatible_services": ["openhab"]
        },
        "apple music": {
            "type": "music",
            "service": "apple music",
            "supported_actions": ["play", "shuffle", "start", "pause", "stop"],
        },
        "spotify": {
            "type": "music",
            "service": "spotify",
            "supported_actions": ["play", "shuffle", "start", "pause", "stop"],
        },
        "office": {
            "type": "plugs",
            "room": "office",
            "service": "openhab",
            "supported_actions": ["turn on", "turn off"],
        },
        "timer": {
            "type": "time",
            "feature": "timer",
            "supported_actions": ["start", "stop"],
            "contexts": ["time"]
        }
    },
    "services": {
        "music": ["apple music", "spotify"],
        "plugs": ["dining room"],
        "time": ["timer"]
    },
    "actions": {
        "on":  ["play", "shuffle", "start", "turn on"],
        "off": ["pause", "stop", "turn off"]
    }
}

# %%
speech = "turn on the office"

# %%
def generate_commands(text):
    action, service, input = "action", "input", "service"
    command_input = [action, input, service]
    for element in recognition_words['keywords']:
        if element in text:
            type = recognition_words['keywords'][element]["type"]
            if type in recognition_words["services"].keys():
                command_input[command_input.index(service)] = recognition_words['keywords'][element]["service"]
                command_input[command_input.index(input)] = element
            else:
                command_input[command_input.index(type)] = element
    print(command_input)
generate_commands(speech)

# %%
# model = Model("vosk-model-en-us-0.22")

# recognizer = KaldiRecognizer(
#     model,
#     16000,
# )

# %%
# mic = pyaudio.PyAudio()

# stream = mic.open(
#     format=pyaudio.paInt16,
#     channels=1,
#     rate=16000,
#     input=True,
#     frames_per_buffer=8192
# )
# stream.start_stream()

# %%
# while True:
#     data = stream.read(4096, exception_on_overflow=False)

#     if recognizer.AcceptWaveform(data):
#         result = json.loads(recognizer.Result())
#         text = result["text"]
#         print(text)
#         # if text:
#         #     generate_commands(text)


# %%
# stream.stop_stream()


