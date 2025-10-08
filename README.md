# WanderWise - Your One-Stop Travel Companion

### Authors:
[ARUN P C]

---

## Project Overview

**WanderWise** is an innovative travel companion platform that helps users navigate international travel by overcoming language barriers, providing cultural insights, and offering real-time translation services for text and speech. The platform utilizes modern technologies like Optical Character Recognition (OCR), Google Translator, speech recognition, and text-to-speech (TTS) to enhance the user experience.

### Key Features
- **Text Language Conversion**: Real-time translation of text in images via OCR.
- **Real-Time Speech Conversion**: Instant translation and speech synthesis for seamless conversation.
- **Cultural Insights**: Discover the historical and cultural significance of travel destinations.
- **Must-Visit Spots**: Get recommendations for top attractions and hidden gems based on location.
- **User Reviews**: Read feedback and suggestions from other travelers.
- **Travelmate Finder**: Connect with like-minded travelers to share experiences.

---

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Features Implementation](#features-implementation)
- [API Integration](#api-integration)
- [Running the Application](#running-the-application)
- [Conclusion](#conclusion)
- [References](#references)

---

## Introduction
In today’s interconnected world, international travel is common, but language barriers and lack of cultural knowledge can make it difficult for travelers. **WanderWise** simplifies travel experiences by providing real-time translations, cultural insights, and personalized recommendations. The platform integrates multiple features to help travelers better understand their surroundings and connect with others while traveling.

---

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Libraries**:
  - `OpenCV` for image processing
  - `pytesseract` for Optical Character Recognition (OCR)
  - `deep_translator` for Google Translate API integration
  - `langdetect` for language detection
  - `speech_recognition` for voice input
  - `gtts` for converting translated text to speech
- **API Integration**: Google Vision API, Microsoft Translator API, OpenWeatherMap API

---

## Setup Instructions
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/WanderWise.git
   cd WanderWise
2.Create a virtual environment (optional but recommended):
pip install -r requirements.tx

3. Install Tesseract OCR
Download and install Tesseract OCR: Tesseract OCR
After installation, update the path to Tesseract in app.py:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

3. Install Tesseract OCR
Download and install Tesseract OCR: Tesseract OCR
After installation, update the path to Tesseract in app.py:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
---
## Features Implementation
1. Image Language Translation
•	Users can upload an image containing text.
•	The image is processed using OpenCV to enhance its quality.
•	OCR (using pytesseract) is applied to extract text.
•	The detected text is translated to the target language using the Google Translator API.
•	If the translation is successful, the translated text is displayed.
2. Real-Time Speech Conversion
•	Users speak into the microphone, and their speech is captured.
•	The captured speech is converted to text using Speech Recognition.
•	The recognized text is translated into the target language using the Google Translator API.
•	The translated text is converted back into speech using Google Text-to-Speech (gTTS), so users can hear the translation.
3. Cultural Insights
The platform offers cultural insights based on the current travel destination, helping users explore the historical and cultural significance of locations.
4. Travelmate Finder
A feature that connects like-minded travelers, allowing them to share experiences and plan together during their trips.

## API Integration
•	Google Vision API: Used for text extraction from images.
•	Google Translator API: Provides real-time text translation in multiple languages.
•	OpenWeatherMap API: Fetches weather data for the travel destination.
•	Speech Recognition API: Converts speech to text.
•	gTTS API: Converts translated text back to speech.

## Running the Application

Once you've set up the environment and installed all dependencies, run the application using:
python app.py
This will start a Flask server at http://localhost:5000. You can access features like text scanning, voice translation, cultural insights, and more directly through the web interface.

---
## Conclusion

WanderWise brings together language translation, cultural knowledge, and social connectivity to enhance the travel experience. The platform bridges communication gaps, promotes cultural understanding, and connects travelers from around the world. By integrating cutting-edge technologies such as OCR, speech recognition, and AI-driven language translation, it creates a seamless experience for users.



## Future Updates:
•	Offline functionality for real-time translation.
•	Mobile app version for a broader reach.
