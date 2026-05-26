
from events import sound_events
from event_selector import selected_event


# for the tests, make sure the file path is set to the main folder, then run python -m pytest
# PS C:\Users\dani_\OneDrive\Desktop\PROJECTSSSSSS\UTILITY FUNCTIONS\audio_utility_functions> python -m pytest


def test_metric_threshold_reached_passed_returns_high_score_sound():
    # arrange
    achieved_score = 0.92
    threshold =0.90

    #act
    result = selected_event(achieved_score=achieved_score, threshold=threshold)

    assert result == sound_events["high_score"]



def test_achieved_score_equals_high_score_sound():
    # arrange
    achieved_score = 0.92
    threshold =0.90

    #act
    result = selected_event(achieved_score=achieved_score, threshold=threshold)

    assert result == sound_events["high_score"]



def test_metric_below_threshold_returns_high_score_sound():
    # arrange
    achieved_score = 0.72
    threshold =0.90

    #act
    result = selected_event(achieved_score=achieved_score, threshold=threshold)

    assert result == sound_events["low_score"]

