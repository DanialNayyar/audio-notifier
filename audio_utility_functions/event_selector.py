#chooses the events from events.py and returns the correct one


from events import sound_events

def selected_event(achieved_score, threshold, is_event = None):

    if achieved_score >= threshold:
        return sound_events["high_score"]

    if achieved_score < threshold:
        return sound_events["low_score"]    

selected_event(achieved_score= 0.5, threshold=0.8, is_event="Success")

