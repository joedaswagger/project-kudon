import sounddevice as sd
from scipy.io.wavfile import write

def main():

    #temporary CLI menu will be removed soon
    while True:
        choice = input("1 for plotting, 2 for recording")
        if choice == 1:
            pass
        else:
            fs = 44100  # Sample rate
            seconds = 10  # Duration of recording

            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            write('output.wav', fs, myrecording)  # Save as WAV file 

if __name__ == "__main__":
    main()