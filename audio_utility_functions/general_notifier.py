# for success, training complete, error, etc


from events import sound_events
from event_selector import selected_event

def notificaiton (event, sample_rate):
    configuration = sound_config(event)
    waveform = generate_waveform(configuration, sample_rate = sample_rate)
    play_sound(waveform)



notificaiton(sound_events["success"])
notificaiton(sound_events["error"])
notificaiton(sound_events["training_complete"])

