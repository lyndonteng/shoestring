import speech_recognition as sr
import socket


HOST = '192.168.43.145'
PORT = 13000


def main():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=3)
            r.energy_threshold = 800
            print("Say something!")
            audio = r.listen(source, phrase_time_limit=10)
            print("Done")
            try:
                _ = len(r.recognize_google(audio))
                s.sendto(bytes(r.recognize_google(audio), 'utf-8'), (HOST, PORT))
            except sr.UnknownValueError:
                pass


if __name__ == '__main__':
    main()
