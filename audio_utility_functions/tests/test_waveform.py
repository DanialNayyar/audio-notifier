from audio_notifier.waveform_generation import sine_wave, sawtooth_wave, triangle_wave, square_wave, generator
from audio_notifier.sound_configuration import configuration
import pytest
import numpy as np

def test_sine_returns_correct_samples(): #passed
    config = configuration(frequency=400,
                           duration = 3.0,
                           waveform="sine",
                           volume=1.0)
    
    sample_rate = 10_000

    wave = generator(config=config, sample_rate=sample_rate)

    assert len(wave) == int(sample_rate * config["duration"])


def test_sawtooth_returns_correct_samples(): #passed
    config = configuration(frequency=400,
                           duration = 3.0,
                           waveform="sawtooth",
                           volume=1.0)
    
    sample_rate = 10_000

    wave = generator(config=config, sample_rate=sample_rate)

    assert len(wave) == int(sample_rate * config["duration"])


def test_square_returns_correct_samples(): #passed
    config = configuration(frequency=400,
                           duration = 3.0,
                           waveform="square",
                           volume=1.0)
    
    sample_rate = 10_000

    wave = generator(config=config, sample_rate=sample_rate)

    assert len(wave) == int(sample_rate * config["duration"])


def test_triangle_returns_correct_samples(): #passed
    config = configuration(frequency=400,
                           duration = 3.0,
                           waveform="triangle",
                           volume=1.0)
    
    sample_rate = 10_000

    wave = generator(config=config, sample_rate=sample_rate)

    assert len(wave) == int(sample_rate * config["duration"])



def test_generator_rejects_invalid_wave(): #passed

    config = {
        "frequency": 400,
        "duration": 3.0,
        "waveform" :  "unknown",
        "volume" : 1.0
    }
    sample_rate = 10_000

    with pytest.raises(ValueError):
        generator(config=config, sample_rate=sample_rate)


def test_waveform_within_volume_range():
    config = configuration(frequency=400,
                           duration = 3.0,
                           waveform= "sine",
                           volume=1.0
                           )
    
    sample_rate = 10_000

    wave = generator(config=config, sample_rate=sample_rate)

    assert wave.max() <= config["volume"]
    assert wave.min() >= -config["volume"]




def test_sample_rate_invalid():
    config = configuration(frequency=400,
                           duration = 3.0,
                           waveform= "sine",
                           volume=1.0
                           )
    
    sample_rate = 0
    
    with pytest.raises(ValueError):
        generator(config=config, sample_rate=sample_rate)