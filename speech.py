import speech_recognition as sr
import socket


def main(host='192.168.1.1', port=65432):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=1)
                r.energy_threshold = 800
                print("Say something!")
                audio = r.listen(source)
                print("Done")
                s.sendall(bytes(r.recognize_google(audio), 'utf-8'))


if __name__ == '__main__':
    main()
