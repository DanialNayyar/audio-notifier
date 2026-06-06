from pathlib import Path
from events import sound_events
from general_notifier import notification
from sound_player import to_wav

def main():
    
    sample_rate = 10_000

    event1 = sound_events["success"]
    event2 = sound_events["error"]
    event3 = sound_events["high_score"]
    event4 = sound_events["low_score"]
    event5 = sound_events["training_complete"]

    wave1 = notification(event=event1, sample_rate=sample_rate)
    wave2 = notification(event=event2, sample_rate=sample_rate)
    wave3 = notification(event=event3, sample_rate=sample_rate)
    wave4 = notification(event=event4, sample_rate=sample_rate)
    wave5 = notification(event=event5, sample_rate=sample_rate)    

    output_folder = Path("events_outputs")
    output_folder.mkdir(exist_ok=True)

    output_file_success = output_folder/"success.wav"
    output_file_error = output_folder/"error.wav"
    output_file_high_score = output_folder/"high_score.wav"
    output_file_low_score = output_folder/"low_score.wav"
    output_file_training_complete = output_folder/"training_complete.wav"

    to_wav(waveform=wave1, 
           sample_rate=sample_rate, 
           filename=output_file_success)
    print(f"Sound saved: {output_file_success}")




    to_wav(waveform=wave2, 
            sample_rate=sample_rate, 
            filename=output_file_error)
    print(f"Sound saved: {output_file_error}")




    to_wav(waveform=wave3, 
            sample_rate=sample_rate, 
            filename=output_file_high_score)
    print(f"Sound saved: {output_file_high_score}")


    

    to_wav(waveform=wave4, 
            sample_rate=sample_rate, 
            filename=output_file_low_score)
    print(f"Sound saved: {output_file_low_score}")





    to_wav(waveform=wave5, 
            sample_rate=sample_rate, 
            filename=output_file_training_complete)
    
    print(f"Sound saved: {output_file_training_complete}")



if __name__ == "__main__":
    main()