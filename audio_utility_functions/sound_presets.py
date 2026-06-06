from events import sound_events
from sound_configuration import configuration

def get_sound_config(event):
    if event == sound_events["success"]:

        return configuration(
            frequency= 800,
            duration = 3.0,
            waveform="sine",
            volume = 1.0
        )
    
    elif event == sound_events["error"]:
        return configuration(
            frequency= 200,
            duration = 3.0,
            waveform="square",
            volume = 1.0
        )
        
    
    elif event == sound_events["high_score"]:
        return configuration(
            frequency= 1000,
            duration = 3.0,
            waveform="sawtooth",
            volume = 1.0
        )
        
    elif event == sound_events["low_score"]:
        return configuration(
            frequency= 150,
            duration = 3.0,
            waveform="sawtooth",
            volume = 1.0
        )
            
    elif event == sound_events["training_complete"]:
        return configuration(
            frequency= 600,
            duration = 3.0,
            waveform="sine",
            volume = 1.0
        )
        
    else:
        raise ValueError(f"Event Unknown: {event}")

    
