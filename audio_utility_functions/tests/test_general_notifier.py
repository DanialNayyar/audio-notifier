from audio_notifier.general_notifier import notification
from audio_notifier.events import sound_events
from audio_notifier.sound_presets import get_sound_config

def test_notifier_returns_wave():
    event = sound_events["success"]

    sample_rate = 10_000

    wave = notification(event=event, sample_rate=sample_rate)
    
    assert len(wave) > 0


def test_notifier_returns_correct_sample_number():
    event = sound_events["success"]

    sample_rate = 10_000
    

    config = get_sound_config(event=event)
    wave = notification(event=event, sample_rate=sample_rate)

    expected_samples = int(config["duration"]*sample_rate)

    assert len(wave) == expected_samples

    