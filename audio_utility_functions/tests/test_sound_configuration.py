from audio_notifier.sound_configuration import configuration
import pytest

def test_sound_config_is_created(): #passed
    #arrange

    frequency = 400
    duration = 1.0
    waveform = "sine"
    volume = 0.5

    #act

    config = configuration(frequency=frequency,
                            duration = duration, 
                           waveform=waveform,
                           volume= volume) 
    

    assert config["frequency"] == frequency
    assert config["duration"] == duration
    assert config["waveform"] == waveform
    assert config["volume"] == volume



def test_negative_frequency_error(): #passed

    with pytest.raises(ValueError):

        configuration(frequency=-400,
                      duration = 1.0,
                      waveform = "sine",
                      volume = 0.5)



def test_zero_frequency_error(): #passed

    with pytest.raises(ValueError):

        configuration(frequency=0,
                      duration = 1.0,
                      waveform = "sine",
                      volume = 0.5)






def test_zero_duration_error(): #passed
    
    with pytest.raises(ValueError):

        configuration(frequency=400,
                      duration = 0.0,
                      waveform = "sine",
                      volume = 0.5)




def test_negative_duration_error(): #passed

    with pytest.raises(ValueError):

        configuration(frequency=400,
                      duration = -1.0,
                      waveform = "sine",
                      volume = 0.5)
        






def test_invalid_waveform_selected(): #passed

    with pytest.raises(ValueError):

        configuration(frequency=400,
                      duration = 1.0,
                      waveform = "blue",
                      volume = 0.5)
        





def test_zero_volume_error(): #passed

    with pytest.raises(ValueError):

        configuration(frequency=400,
                      duration = 1.0,
                      waveform = "sine",
                      volume = 0.0)
        



def test_negative_volume_error(): # passed

    with pytest.raises(ValueError):

        configuration(frequency=400,
                      duration = 1.0,
                      waveform = "sine",
                      volume = -0.5)





def test_volume_above_one_error(): # passed

    with pytest.raises(ValueError):

        configuration(frequency=400,
                      duration = 1.0,
                      waveform = "sine",
                      volume = 1.5)