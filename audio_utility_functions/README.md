# Audio Notification Utility

Small Python utility project that generates audio notification sounds. Developed for notebooks, model training scripts and overall long running code. The project was built to practice project strcutre, reuseable functions, pytest testing and simple waveform genereating.

## Project Purpose

This utility creates simple notification sounds for different events such as: 
- Code ran successfully
- Code Failed
- Model scored above a threshold
- Model score below a threshold
- Training completed

The project is useful for long running machine learning experiments where an audio signal can be used to signify when the code has executed completely.

## Features

- Event based sound selection
- Waveform generation with NumPy
- Supported waveforms include:
-   Sine wave
-   Square Wave
-   Sawtooth Wave
-   Triangle Wave
- The sounds generated are saved as .wav files
- Pytest tests are also included in the tests folder

## What I Learned

This project was supposed to helped develop the end-to-end workflow used in software development.
It helped practice:
- Creating seperate modules
- Creating reusable functions
- Validating inputs
- Generating waveforms
- Saving files
- Using pytest
- Build a clean GitHub workflow

## Future Work

- Developed a lightweightr Google Colab version that can be imported into a notebook and be used to play sounds.
