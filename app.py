from flask import Flask, render_template, request, jsonify,send_file,session, redirect,url_for
import threading
import time
import cv2
import os
# from cvzone.HandTrackingModule import HandDetector
import numpy as np
import mediapipe as mp
import pyautogui
import pickle
import face_recognition
# from datetime import datetime
import base64
import pythoncom  # Required for COM in Flask
import win32com.client
from PIL import Image
import numpy as np

pyautogui.PAUSE = 0.01

app = Flask(__name__)
app.secret_key = "any_random_secret_123"  # ✅ Needed for session handling


# Global flags to control module execution
module_status = {"module1": False, "module2": False}

""" -------- Hand Audio/Video Module Function ------------"""

def is_palm_facing_z(hand_landmarks):
    # Index Finger Tip (8) and MCP (5)
    tip_z = hand_landmarks.landmark[8].z
    mcp_z = hand_landmarks.landmark[5].z
    return tip_z < mcp_z  # Palm facing if fingertip is closer to camera


def fingers_up(lmList,tipIds):
    fingers = []
    # Thumb
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:  # right hand logic
        fingers.append(1)
    else:
        fingers.append(0)
    # Fingers (index to pinky)
    for id in range(1,5):
        if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers



def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# Simulated function for Audio/Video module
def run_module(module_name):
    while module_status[module_name]: 
        
        if module_name == "module2":
        
            """------  Hand Video/Audio Control Module --------"""    
        
            # Mediapipe Hands initialization
            mpHands = mp.solutions.hands
            hands = mpHands.Hands(max_num_hands=1)
            mpDraw = mp.solutions.drawing_utils

            # Webcam
            cap = cv2.VideoCapture(0)

            # Finger tip landmarks
            tipIds = [4, 8, 12, 16, 20]

            prev_action_time = 0
            action_delay = 1  # seconds delay between actions

            while module_status[module_name]:
                success, img = cap.read()
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = hands.process(imgRGB)
                
                lmList = []
                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                        
                        lmList = []
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            lmList.append((id, cx, cy))
                        
                        # Check using Z-axis method
                        if is_palm_facing_z(handLms):
                            fingers = fingers_up(lmList,tipIds)
                            totalFingers = fingers.count(1)
                            current_time = time.time()
                            if current_time - prev_action_time > action_delay:
                                if fingers == [0,1,0,0,0]:
                                    print("Forward 5s")
                                    pyautogui.press('right')
                                elif fingers == [0,1,1,0,0]:
                                    print("Backward 5s")
                                    pyautogui.press('left')
                                elif fingers == [0,1,1,1,0]:
                                    for _ in range(2):
                                        pyautogui.press('volumeup')
                                    print("Volume Up")
                                elif fingers == [0,1,1,1,1]:
                                    for _ in range(2):
                                        pyautogui.press('volumedown')
                                    print("Volume Down")
                                elif fingers == [1,1,1,1,1]:
                                    print("Play/Pause")
                                    pyautogui.press('space')
                                
                                prev_action_time = current_time
                        else:
                            print("Back side detected — Ignoring gesture")
                            
                cv2.imshow("Video Control", img)

                if cv2.waitKey(1) == 27:
                    cv2.destroyAllWindows()
                    cap.release()
                    break 
                if not module_status[module_name]:
                        cap.release()
                        cv2.destroyAllWindows()
    
        if module_name == "module3":
            pass
        

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/start/<module_name>')
def start_module(module_name):
    if module_name in module_status:
        module_status[module_name] = True
        thread = threading.Thread(target=run_module, args=(module_name,))
        thread.start()
        return jsonify({"status": "started", "module": module_name})
    return jsonify({"status": "error", "message": "Invalid module"})

@app.route('/stop/<module_name>')
def stop_module(module_name):
    if module_name in module_status:
        module_status[module_name] = False
        return jsonify({"status": "stopped", "module": module_name})
    return jsonify({"status": "error", "message": "Invalid module"})



""" Presentation Control Module """



UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")  # Store uploaded files in "uploads"
OUTPUT_FOLDER = os.path.join(os.getcwd(), "static/slides")  # Store converted PNGs in "output"

ALLOWED_EXTENSIONS = {'ppt', 'pptx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_ppt_to_png(ppt_path, output_folder, resolution=(1776, 1000)):
    """Converts PPT/PPTX slides to PNG images with resolution 1776x1000."""
    pythoncom.CoInitialize()  # Initialize COM in this thread

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Open PowerPoint
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        powerpoint.Visible = 1  # 1 = visible, 0 = hidden

        # Open the presentation
        presentation = powerpoint.Presentations.Open(ppt_path, WithWindow=False)

        # Export slides
        presentation.Export(output_folder, "png")

        # Close PowerPoint
        presentation.Close()
        powerpoint.Quit()

        print(f"Slides exported to: {output_folder}")

        # Resize images
        for file in os.listdir(output_folder):
            if file.endswith(".png"):
                img_path = os.path.join(output_folder, file)
                img = Image.open(img_path)
                img = img.resize(resolution, Image.LANCZOS)
                img.save(img_path, "png")
                print(f"Resized: {img_path}")

    except Exception as e:
        print(f"Error converting PPT to PNG: {e}")


@app.route('/inputppt')
def inputppt():
    return render_template("input.html")



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        print(f"File saved: {file_path}")

        # Run PowerPoint conversion in a separate thread
        threading.Thread(target=convert_ppt_to_png, args=(file_path, OUTPUT_FOLDER)).start()

        return f'File {file.filename} uploaded successfully! Conversion started.'

    return 'Invalid file type. Only PPT and PPTX files are allowed.'



ENCODINGS_FILE_PRE = "static/model_presentation/trained_faces.pkl"
if os.path.exists(ENCODINGS_FILE_PRE):
    with open(ENCODINGS_FILE_PRE, "rb") as f:
        known_faces_presentation = pickle.load(f)
else:
    known_faces_presentation = {}

@app.route("/presentation")
def presentation():
    return render_template("presentation.html")

@app.route("/presentation_register", methods=["POST"])
def presentation_register():
    data = request.json
    name = data.get("name")
    img_data = data.get("image").split(',')[1]
    # print(name)
    # img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB)

    if not name or not img_data:
        return jsonify({"success": False, "message": "Invalid request data"})

    try:
        # Decode the Base64 image
        img_bytes = base64.b64decode(img_data)
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if img is None:
            print("❌ Image could not be decoded")
            return jsonify({"success": False, "message": "Image decoding failed"})

        # Check if a face is detected
        face_encodings = face_recognition.face_encodings(img)
        if len(face_encodings) > 0:
            for known_name,known_encoding in known_faces_presentation.items():
                # match = face_recognition.compare_faces([known_encoding], face_encodings[0])[0]
                distance = face_recognition.face_distance([known_encoding], face_encodings[0])[0]
                match = distance < 0.5  # You can experiment with 0.5 to 0.6
                if match:
                    return jsonify({"success": False, "message": f"Face is already Exist {known_name}"})

            # if face is not matches all the fases in the Pickle then will be register
            known_faces_presentation[name] = face_encodings[0]
            with open(ENCODINGS_FILE_PRE, "wb") as f:
                pickle.dump(known_faces_presentation, f)
            print(f"✅ Face registered for: {name}")
            return jsonify({"success": True, "message": "Face Registered Successfully!"})

        print("❌ No face detected!")
        return jsonify({"success": False, "message": "Face not detected Please Try again. Make sure your face is clearly visible"})

    except Exception as e:
        print(f"⚠️ Error in register: {str(e)}")
        return jsonify({"success": False, "message": "Internal Server Error"})



@app.route("/login", methods=["POST"])
def login():
    
    data = request.json
    img_data = data.get("image").split(',')[1]

    if not img_data:
        return jsonify({"status": "fail", "message": "No image received"})

    # Decode Base64 image
    img_bytes = base64.b64decode(img_data)
    img_array = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is None:
        return jsonify({ "status" : "fail", "message": "Image decoding failed"})

    # Detect faces
    face_encodings = face_recognition.face_encodings(img)
    if len(face_encodings) > 0:
        for name, known_encoding in known_faces_presentation.items():
            # match = face_recognition.compare_faces([known_encoding], face_encodings[0])[0]
            distance = face_recognition.face_distance([known_encoding], face_encodings[0])[0]
            match = distance < 0.5  # You can experiment with 0.5 to 0.6
            if match:
                print("Login success")
                session["user"] = name
                session["encoding"] = known_encoding.tolist()
                print(f"✅ Login for {name}")  # Debugging

                return jsonify({ "status" : "success", "message": f" Welcome {name}  "})
        return jsonify({"status":"fail","message":"Face not Registered! Please Register "})
    
    return jsonify({"status" : "fail", "message": "Face not Recognized!"})

@app.route("/verify_face", methods=["POST"])
def verify_face():
    if "encoding" not in session:
        return jsonify({"match": False})

    data = request.get_json()
    img_data = data["image"].split(",")[1]
    img_bytes = base64.b64decode(img_data)
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_img)
    if not face_locations:
        return jsonify({"match": False})

    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
    if not face_encodings:
        return jsonify({"match": False})

    current_encoding = face_encodings[0]
    known_encoding = np.array(session["encoding"])

    # match = face_recognition.compare_faces([known_encoding], current_encoding)[0]
    distance = face_recognition.face_distance([known_encoding], current_encoding)[0]
    match = distance < 0.5  # You can experiment with 0.5 to 0.6
    return jsonify({"match": bool(match)})

@app.route("/present")
def present():
    if "user" in session:
        return render_template("gesture.html", user=session["user"])
    return redirect(url_for("index"))

@app.route("/stop_presentation")
def stop_presentation():
    clear_folder(os.path.join(os.getcwd(),"static/slides"))
    return redirect(url_for("index"))


@app.route("/slide_count")
def slide_count():
    slide_folder = os.path.join("static", "slides")
    total = len([f for f in os.listdir(slide_folder) if f.endswith(".PNG")])
    return jsonify({"total": total})


# Run form the Vscode

if __name__ == '__main__':
    app.run(debug=True)

# def runproject():
#     app.run(debug=True)
