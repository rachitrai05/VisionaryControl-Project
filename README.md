## ✨ Visionary Control (A Smart Gesture Based Interaction System)

## 🧠 INTRODUCTION:

**Visionary Control** is a smart, gesture-based control system that enables users to interact with digital media and presentation tools using intuitive hand gestures. It is a unified platform that improves human-computer interaction by providing touchless control through real-time gesture recognition.

The system utilizes computer vision and hand tracking technologies to allow seamless operation of presentations and media players without physical contact, making it especially suited for classrooms, seminars, and professional environments.

---

## 🎯 PURPOSE:

The purpose of this project is to develop an intelligent, gesture and vision-based interface system—**Visionary Control**—which enhances human-computer interaction by replacing conventional input devices with intuitive, contactless control mechanisms.

The system is designed to facilitate seamless interaction with two key digital functions:

- 🖥️ **Presentation control** secured by **face-based login**  
- 🎵 **Media player Control** through **gesture recognition**

By integrating computer vision and facial authentication, the project ensures:

- 🔐 Secure access  
- ✋ Hands-free operation  
- 💡 Modernized engagement  

...especially within academic and professional environments.  
The goal is to improve **accessibility**, reduce reliance on hardware, and promote **automation** in user interaction.

---

## 🛠️ TOOLS USED

- **IDE:** VS Code  
- **Dataset Handling:** OpenCV, MediaPipe, Pickle  
- **Libraries:** OpenCV, MediaPipe, NumPy, Flask, face_recognition, pyautogui  
- **GUI:** HTML + Tailwind CSS + JavaScript  
- **Backend:** Python (Flask)

---

It comprises two core modules:

---

### 1️⃣ ✋ Presentation Control using Hand Gesture + 🔐 Face-Based Login for Authentication

The **Presentation Control Module** enables users to:

- 👉 Control slides  
- 👉 Navigate content  
- ✏️ Draw on the screen using predefined hand gestures

This module is uniquely integrated with a **Face-Based Login and Registration System**, which ensures that **only authenticated users** can access the presentation control features.

- 🧑‍💼 Users must register their face once  
- 🧾 Their identity is verified before they are granted access

➡️ Providing a **secure and personalized experience**

---
## FLOW CHART OF PRESENTATION CONTROL
![image](https://github.com/user-attachments/assets/d54eed61-f576-4ec2-a8a2-5858f818c3e6)

## ACTUAL INTERFACE:- This is User Interface of VisionaryControl

![Screenshot 2025-05-06 004228](https://github.com/user-attachments/assets/e9f0e503-5901-4cec-a599-3f0d5c6db375)

## Now Click on Presentation Control (This is Interface of Presentation Control

## Upload your PowerPoint file for Presentation

![Screenshot 2025-05-06 094640](https://github.com/user-attachments/assets/42223672-77ae-487d-9fce-4283de6cd28b)

## Module is Started and Open For Registration First Using Face Detection

![Screenshot 2025-05-05 224232](https://github.com/user-attachments/assets/3621f452-4f5d-461b-94ee-b40b80791470)

## Authenticity and Login

![Screenshot 2025-05-05 224506](https://github.com/user-attachments/assets/f38f2533-a6d9-441f-9182-4470c872d7e0)

![Screenshot 2025-05-05 224525](https://github.com/user-attachments/assets/49800e1d-d946-4fc4-a8f4-6362401182bb)

![Screenshot 2025-05-05 224537](https://github.com/user-attachments/assets/aa2041b6-2f6b-4b22-9db9-71bab8a3dacd)

## Interface After Login Using Face Based Authentication for Presenting the Slides

![Screenshot 2025-05-05 224613](https://github.com/user-attachments/assets/ac1eab38-4548-402e-b092-02a073297b58)

## ☝️ (Index finger): Next slide

![Screenshot 2025-05-05 224703](https://github.com/user-attachments/assets/79363003-b71c-4d59-a790-32fad43ea441)

## ✌️ (Index + Middle): Previous slide

![Screenshot 2025-05-05 224842](https://github.com/user-attachments/assets/7e032fbc-9701-4941-9b77-d94402f24efc)

## If Face is not Detected then Gesture Blocked

![Screenshot 2025-05-05 224741](https://github.com/user-attachments/assets/6e0a79ef-e420-47e2-b67a-ea411cb77162)


### 2️⃣ 🎬 Media Player Control using Hand Gesture

The second component, the **Media Control Module**, allows users to:

- ▶️ Manage video/audio playback  
- ☝️ Detect number of fingers shown to perform actions like play, pause, forward, rewind, Volume up and Volum Down

✅ This module operates **independently**  
🚫 Does **not require face authentication**

---
## FLOWCHART OF MEDIA PLAYER CONTROL

![image](https://github.com/user-attachments/assets/2a00ebf4-3339-4a3d-888a-9f5af5c4bf11)

## This is Interface of Media Player Control

![Screenshot 2025-05-06 001558](https://github.com/user-attachments/assets/268d08cd-b90b-43ea-8c84-e8fc33d3c9c6)

## Now Start the Module

## 1. ✋ Open/Close Palm ==> Play/Pause

![Screenshot 2025-04-10 164424](https://github.com/user-attachments/assets/d94c355a-2abd-45d4-bab6-535509723d36)

![Screenshot 2025-04-10 164920](https://github.com/user-attachments/assets/429541b8-aa8b-4f5b-8b4c-37447d870327)


## 2. ☝️ Index Finger ==> + 5s Forward

![Screenshot 2025-04-10 165044](https://github.com/user-attachments/assets/b739f549-8977-4562-835a-4bb40739de0b)

![Screenshot 2025-04-10 164920](https://github.com/user-attachments/assets/57591a91-194d-4dc4-a84a-76209bb2b9fa)

## 3. ✌️ Index + Middle Finger ==> -5s Backward

![Screenshot 2025-04-10 165056](https://github.com/user-attachments/assets/3b2f06c8-49c7-4e83-895e-d7d19bea548a)

![Screenshot 2025-04-10 165030](https://github.com/user-attachments/assets/53bff543-8747-440f-8c22-17535d7b940f)

## 4. 🤟 Index + Middle + Ring (Finger) ==> +4 System Volume

![Screenshot 2025-04-10 165112](https://github.com/user-attachments/assets/a776d038-efc1-41a0-ae08-b442e7e21c49)

![Screenshot 2025-05-05 225357](https://github.com/user-attachments/assets/60cdfec7-a2f6-4bf1-8794-3cbe5482667d)

## 5. 🖖 All Four Fingers Except Thumb ==> -4 System Volume

![Screenshot 2025-04-10 165200](https://github.com/user-attachments/assets/1af358e7-3bc6-44fb-95f5-db0490f85fae)

![Screenshot 2025-05-05 225641](https://github.com/user-attachments/assets/0b48f004-4176-45c5-82b8-5e2b971405c3)


## 🖥️Installation

## Clone the repository:
git clone https://github.com/rachitrai05/VisionaryControl-Project.git
cd visionaryControl-project

## Install dependencies
pip install -r requirements.txt

## Run the Flask server
python app.py

Access the web interface:
Open in Browser
Navigate to: http://127.0.0.1:5000

## 👨‍🏫 Ideal Use Cases

Smart classrooms and e-learning environments
Professional presentations at conferences or offices
Accessible systems for physically challenged individuals
Modern, contactless media player setups

## 🙌 Team Members

Rachit Rai
Anuj Gupta
Shafa-At-Ali

## ✅ Result

The Visionary Control system successfully achieved its objective of enabling touchless interaction using hand gestures and face-based authentication. The system performed reliably during testing, accurately recognizing predefined gestures for both presentation and media control.

- The Presentation Control module, secured with face-based login, ensured authorized access while allowing smooth slide navigation and on-screen drawing.
- The Media Player Control module accurately interpreted finger gestures to perform playback operations without physical contact.
- 
Overall, the system delivered a seamless, secure, and intuitive user experience, demonstrating its effectiveness for academic and professional use cases.


🤝Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to create an issue or submit a pull request.
