from .waveform_generation import sine_wave, sawtooth_wave, triangle_wave, square_wave, generator
from .sound_configuration import configuration
from .events import sound_events
from .sound_presets import get_sound_config



def notification (event, sample_rate):
    event = event
    sample_rate = sample_rate

    config = get_sound_config(event=event)
    wave = generator(config=config, sample_rate=sample_rate)

    return wave
