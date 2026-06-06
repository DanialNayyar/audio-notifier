import wave as wv
from pathlib import Path
import numpy as np

def to_wav(waveform, sample_rate, filename):

    if sample_rate <= 0:
        raise ValueError("Sample rate must be larger than 0")
    
    filename = Path(filename)

    if filename.suffix != ".wav":
        raise ValueError("file name must end with .wav")
    
    waveform = np.asarray(waveform)

    if waveform.size ==0:
        raise ValueError("Waveform cannot be empty")
    
    if np.isnan(waveform).any():
        raise ValueError("Waveform cannot contain NaNs")
    

    if waveform.max() >1.0 or waveform.min() < -1.0:
        raise ValueError("Waveform values should be between -1 and 1")
    
    audio_data = (waveform *32767) .astype(np.int16) #-32767 to +32767

    with wv.open(str(filename), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data.tobytes())

    return filename