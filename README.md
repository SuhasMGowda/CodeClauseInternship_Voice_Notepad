# Voice_Notepad
This is an python program where you can create text files and add text using voice commands.

## Overview

This project is designed to recognize basic spoken commands or words using a pre-trained model or a simple speech recognition algorithm. The program listens to audio input from the user's microphone and identifies the spoken words, providing real-time feedback.

## Problem Statement

The objective of this project is to create a program that can recognize basic spoken commands or words. The challenge is to use a pre-trained model or a basic algorithm to process and interpret the audio input, converting it into text. This project aims to provide a foundation for more advanced speech recognition applications, such as voice-activated controls or speech-to-text services.

## Features

- Real-time speech recognition using a microphone.
- Handles basic spoken commands and words.
- Utilizes Google's Web Speech API for accurate recognition.
- Provides feedback on the recognized speech.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/speech-recognition.git
   cd speech-recognition


### Problem Statement Recap

The goal of the project is to create a program capable of recognizing basic spoken commands or words. This involves using either a pre-trained model or a basic speech recognition algorithm to process audio input and convert it into text. The program must handle real-time speech input and provide accurate, immediate feedback to the user.

### Challenges Faced

1. **Noise Interference**: Background noise was a significant challenge, affecting the accuracy of recognition. The solution involved using ambient noise adjustment techniques to filter out unnecessary sounds.

2. **Accurate Recognition**: Achieving high accuracy was difficult, particularly with varying accents and pronunciations. Implementing Google's Web Speech API helped address this challenge, thanks to its high recognition accuracy and adaptability.

3. **Real-Time Processing**: Processing the speech input in real-time without lag was essential. Optimizing the program to handle audio input quickly helped maintain the real-time experience.

4. **Handling Unrecognized Speech**: The program needed to gracefully handle situations where speech wasn't recognized. Error handling was added to inform the user when this occurred, prompting them to try again.

