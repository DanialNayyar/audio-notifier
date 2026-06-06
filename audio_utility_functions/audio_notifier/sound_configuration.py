# stores: frequency, duration, waveform and  volume 

allowed_waveforms = ["sine", "triangle", "square", "sawtooth"]


def configuration(frequency, duration, waveform, volume):

    config = {
        "frequency": frequency,
        "duration": duration,
        "waveform": waveform,
        "volume": volume
    }

    #check that waveform input is valid

    if config["waveform"] not in allowed_waveforms:
        raise ValueError(f"Waveform {waveform} is an invalid input")

    if config["frequency"] <= 0:
        raise ValueError("Frequency needs to be above 0")
    
    if config["duration"] <=0:
        raise ValueError("Duration needs to be above zero")

    if config["volume"] <= 0:
        raise ValueError("Volume needs to be above zero")
    
    if config["volume"] > 1.0:
        raise ValueError("Volume needs to be less than 1.0")


    return config

    
        
