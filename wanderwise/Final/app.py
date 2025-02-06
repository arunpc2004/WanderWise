import os
import threading
import platform
from flask import Flask, render_template, request, jsonify
import cv2
import pytesseract
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory, LangDetectException
import numpy as np
import speech_recognition as sr
import gtts

# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize Flask app
app = Flask(__name__)

# Initialize Translator and Language Detection
DetectorFactory.seed = 0

# Ensure static directory exists
os.makedirs('static', exist_ok=True)

# Image Processing Function
def preprocess_image(frame):
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    denoised_image = cv2.fastNlMeansDenoising(gray_image, None, 30, 7, 21)
    alpha = 1.5  
    adjusted = cv2.convertScaleAbs(denoised_image, alpha=alpha)
    binary_image = cv2.adaptiveThreshold(adjusted, 255,
                                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, 2)
    kernel = np.ones((3,3), np.uint8)
    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    return binary_image

# Voice Processing Function
def recognize_and_convert(dest_language):
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak now...")
            voice = recognizer.listen(source)
            listen = recognizer.recognize_google(voice, language="en")
            print(f"Recognized text: {listen}")

        translate = GoogleTranslator(source='auto', target=dest_language).translate(listen)
        print(f"Translated text: {translate}")

        converted_audio = gtts.gTTS(translate, lang=dest_language)
        converted_audio.save("output.mp3")

        # Play audio based on OS
        if platform.system() == "Windows":
            os.system("start output.mp3")
        else:
            os.system("xdg-open output.mp3")
        
        return {
            "original_text": listen,
            "translated_text": translate
        }
    
    except sr.UnknownValueError:
        print("Could not understand audio")
        return {"error": "Could not understand audio"}
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return {"error": "Speech recognition service unavailable"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": f"Translation error: {str(e)}"}

# Flask Routes
@app.route('/')
def landing_page():
    return render_template('overall.html')

@app.route('/process')
def process_page():
    return render_template('index.html')

@app.route('/scan', methods=['GET', 'POST'])
def image_scan():
    if request.method == 'POST':
        if 'image' in request.files:  # File upload
            file = request.files['image']
            target_language = request.form['language']
            
            if file:
                filepath = os.path.join('static', file.filename)
                file.save(filepath)

                # Read and process the image
                frame = cv2.imread(filepath)
                binary_image = preprocess_image(frame)

                # Perform OCR with custom configuration
                custom_config = r'--oem 3 --psm 6'
                extracted_text = pytesseract.image_to_string(binary_image, config=custom_config)

                cleaned_text = ' '.join(extracted_text.strip().split())
                
                if cleaned_text:
                    try:
                        detected_language = detect(cleaned_text)
                        if detected_language != target_language:
                            translated_text = GoogleTranslator(source=detected_language, target=target_language).translate(cleaned_text)
                            return render_template('scan.html', extracted_text=cleaned_text, translated_text=translated_text)
                        else:
                            return render_template('scan.html', extracted_text=cleaned_text, translated_text="Text is already in the selected language.")
                    except LangDetectException as e:
                        return render_template('scan.html', error=f"Language detection error: {e}")
                else:
                    return render_template('scan.html', error="No valid text extracted.")

    return render_template('scan.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming generator function."""
    camera = cv2.VideoCapture(0)  # Use default camera
    while True:
        success, frame = camera.read()
        if not success:
            break
        
        # Encode the frame in JPEG format
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/convert', methods=['POST'])
def voice_convert():
    selected_language = request.form.get('language')
    
    if not selected_language:
        return jsonify({"error": "No language selected"}), 400
    
    # Run in a separate thread
    thread = threading.Thread(target=recognize_and_convert, args=(selected_language,))
    thread.start()
    
    return jsonify({"message": "Translation started"}), 200

@app.route('/cultural-insights')
def cultural_insights():
    return render_template('cultural-insights.html')

@app.route('/blog')
def blog_page():
    return render_template('blog.html')

@app.route('/must-visit')
def must_visit_page():
    return render_template('must-visit.html')

@app.route('/reviews')
def reviews_page():
    return render_template('reviews.html')

@app.route('/travelmate-finder')
def travelmate_finder_page():
    return render_template('travelmate-finder.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
