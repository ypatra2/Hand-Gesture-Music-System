import numpy as np
import simpleaudio as sa

# Parameters
# duration = 0.3 # seconds
sampling_freq = 44100 # Hz
# freq = 261.626 # Hz

NOTE_C4 = 261.626
NOTE_D4 = 293.665
NOTE_E4 = 329.628
NOTE_F4 = 349.228
NOTE_G4 = 391.995
NOTE_A4 = 440.000
NOTE_B4 = 493.883
NOTE_C5 = 523.251


def tone(freq, duration=1):

    # Generate samples
    samples = np.sin(2 * np.pi * freq * np.arange(duration * sampling_freq) / sampling_freq)

    # Convert to 16-bit integers
    samples = np.int16(samples * 32767)

    # Create audio object
    audio = sa.play_buffer(samples, 1, 2, sampling_freq)

    # Wait for audio to finish
    audio.wait_done()


while True:

    # code to play the first 16 notes of the Star Wars Theme song

    tone(NOTE_C4, 1)
    tone(NOTE_G4, 1)
    tone(NOTE_F4, 0.167)
    tone(NOTE_E4, 0.167);
    tone(NOTE_D4, 0.167);
    tone(NOTE_C5, 1);
    tone(NOTE_G4, 0.5);
    tone(NOTE_F4, 0.167);
    tone(NOTE_E4, 0.167);
    tone(NOTE_D4, 0.167);
    tone(NOTE_C5, 1);
    tone(NOTE_G4, 0.5);
    tone(NOTE_F4, 0.167);
    tone(NOTE_E4, 0.167);
    tone(NOTE_F4, 0.167);
    tone(NOTE_D4, 2);