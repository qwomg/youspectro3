```python
import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt
import os

def generate_spectrogram(audio_file_path, spectrogram_file_path):
    try:
        # Read the audio file
        sample_rate, data = wavfile.read(audio_file_path)

        # Generate the spectrogram
        frequencies, times, spectrogram = signal.spectrogram(data, sample_rate)

        # Create the figure and axis
        fig, ax = plt.subplots()

        # Display the spectrogram
        ax.imshow(spectrogram, aspect='auto', cmap='hot_r', origin='lower')
        ax.axis('off')

        # Save the spectrogram to a file
        plt.savefig(spectrogram_file_path, bbox_inches='tight', pad_inches=0)

        return True
    except Exception as e:
        # If there's an error, log it and return False
        print(f"Error generating spectrogram: {e}")
        return False

def main():
    # Define the paths to the audio file and the output spectrogram file
    audio_file_path = os.path.join(os.getcwd(), 'audio_file.wav')
    spectrogram_file_path = os.path.join(os.getcwd(), 'spectrogram.png')

    # Generate the spectrogram
    success = generate_spectrogram(audio_file_path, spectrogram_file_path)

    if success:
        print("Spectrogram generated successfully.")
    else:
        print("Failed to generate spectrogram.")

if __name__ == "__main__":
    main()
```