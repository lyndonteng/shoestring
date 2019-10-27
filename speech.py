import speech_recognition as sr


def main():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)

    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=1)
            r.energy_threshold = 800
            print("Say something!")
            audio = r.listen(source)
            print("Done")
            print(r.recognize_google(audio))


if __name__ == '__main__':
    main()
