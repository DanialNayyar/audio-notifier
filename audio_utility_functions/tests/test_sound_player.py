import numpy as np
from sound_player import to_wav
import pytest

def test_save_to_wv(tmp_path):
    waveform = np.array([0.0, 0.5, -0.5, 0.0])
    sample_rate = 10_000
    output_file = tmp_path/"test_sound.wav"

    to_wav(waveform=waveform, sample_rate=sample_rate, filename=output_file)

    assert output_file.exists()


def test_to_wv_creates_non_empty_file(tmp_path):
    waveform = np.array([0.0, 0.5, -0.5, 0.0])
    sample_rate = 10_000
    output_file = tmp_path/"test_sound.wav"

    to_wav(waveform=waveform, sample_rate=sample_rate, filename=output_file)

    assert output_file.stat().st_size >0


def test_invalid_sample_rate(tmp_path):
    waveform = np.array([0.0, 0.5, -0.5, 0.0])
    output_file = tmp_path/"test_sound.wav"
    sample_rate = 0

    with pytest.raises(ValueError):
        to_wav(waveform=waveform,
              sample_rate=sample_rate,
              filename=output_file)
        

def test_empty_waveform_equals_error(tmp_path):

    waveform = np.array([])
    output_file = tmp_path/"test_sound.wav"
    sample_rate = 10_000

    with pytest.raises(ValueError):
        to_wav(waveform=waveform,
              sample_rate=sample_rate,
              filename=output_file)
        


def test_invalid_file_ext(tmp_path):

    waveform = np.array([])
    output_file = tmp_path/"test_sound.txt"
    sample_rate = 10_000

    with pytest.raises(ValueError):
        to_wav(waveform=waveform,
              sample_rate=sample_rate,
              filename=output_file)
        

        

