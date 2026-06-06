from sound_configuration import configuration, allowed_waveforms
from sound_presets import get_sound_config

import numpy as np

def sine_wave(volume, frequency, time_array):
    wave = volume *np.sin(2*np.pi *frequency *time_array)
    return wave

def triangle_wave(volume, frequency, time_array):
    phase = (frequency * time_array ) % 1
    wave = volume * (1-4 *np.abs(phase - 0.5)) 
    return wave

def sawtooth_wave(volume, frequency, time_array):
    phase = (frequency * time_array ) % 1
    wave = volume * (2*phase - 1)
    return wave

def square_wave(volume, frequency, time_array):
    wave = volume *np.where(np.sin(2*np.pi*frequency*time_array) >=0, 1,-1)
    return wave




def generator(config, sample_rate):
    if sample_rate <= 0:
        raise ValueError("Sample Rate needs to be above 0")
    
    frequency = config["frequency"]
    duration = config["duration"]
    wave_type = config["waveform"]
    volume = config["volume"]

    samples = int(duration * sample_rate)

    time_array = np.linspace(0, duration,  samples, endpoint = False) 

    if wave_type == "sine":
        wave = sine_wave(volume=volume, frequency=frequency , time_array=time_array )   

    elif wave_type == "square":
        wave = square_wave(volume=volume, frequency=frequency, time_array=time_array)

    elif wave_type == "sawtooth":
        wave = sawtooth_wave(volume=volume, frequency=frequency, time_array=time_array)

    elif wave_type == "triangle":
        wave = triangle_wave(volume=volume, frequency=frequency, time_array=time_array)
    

    else:
        raise ValueError("Invalid Wave Type")
    
    return wave