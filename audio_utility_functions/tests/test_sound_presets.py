from audio_notifier.sound_presets import get_sound_config
from audio_notifier.events import sound_events
from audio_notifier.sound_configuration import allowed_waveforms
import pytest 


def test_success_returns_valid_config():
    event = sound_events["success"]

    config = get_sound_config(event=event)

    assert config["waveform"] in allowed_waveforms
    assert config["frequency"] >0
    assert config["duration"] >0
    assert 0< config["volume"] <=1




def test_error_returns_valid_config():
    event = sound_events["error"]

    config = get_sound_config(event=event)

    assert config["waveform"] in allowed_waveforms
    assert config["frequency"] >0
    assert config["duration"] >0
    assert 0< config["volume"] <=1



def test_high_score_returns_valid_config():
    event = sound_events["high_score"]

    config = get_sound_config(event=event)

    assert config["waveform"] in allowed_waveforms
    assert config["frequency"] >0
    assert config["duration"] >0
    assert 0< config["volume"] <=1



def test_low_score_returns_valid_config():
    event = sound_events["low_score"]

    config = get_sound_config(event=event)

    assert config["waveform"] in allowed_waveforms
    assert config["frequency"] >0
    assert config["duration"] >0
    assert 0< config["volume"] <=1


def test_training_complete_returns_valid_config():
    event = sound_events["training_complete"]

    config = get_sound_config(event=event)

    assert config["waveform"] in allowed_waveforms
    assert config["frequency"] >0
    assert config["duration"] >0
    assert 0< config["volume"] <=1


def test_unknown_event_returns_valid_config():
    with pytest.raises(ValueError):
        get_sound_config(event = "Unknown")

