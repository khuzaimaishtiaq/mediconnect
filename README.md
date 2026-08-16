# MediConnect 🏥

MediConnect is an elevated, premium mobile-first healthcare platform built to streamline the way patients interact with medical professionals. It features a full **FastAPI (Python)** backend, an extremely polished **React (CDN) Single Page Application** frontend with stunning glassmorphism UI, and a fully native **Android Studio Project** that seamlessly wraps the frontend for native mobile deployments.

## ✨ Features
- **Instant Authentication:** Zero-friction login and registration using custom Username bindings to **Supabase Auth**. (No pesky email confirmations required during testing).
- **Beautiful Mobile Interface:** Hand-crafted using Tailwind CSS featuring micro-animations, glassmorphism shadows, and vibrant gradients. Built robustly inside a single `index.html`.
- **Specialist Directory:** Browse categories of top specialists with smooth tab interactions.
- **Appointment Management:** Real-time scheduling views for upcoming vs historical consultations.
- **Ready-to-Deploy Android App:** An included native Android wrapper using `WebView` to instantly port the web application to the Android Emulator or Google Play.

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.9+** (For running the API server)
- **Android Studio** (Optional, for building the APK)

### 2. Run the Backend & Frontend
The frontend `index.html` file is served statically by the FastAPI server, so you just need to start the backend!
First, inside the `backend` folder, you may want to install the requirements:
```bash
pip install -r backend/requirements.txt
```

Then, run the server from the root of the repository on port 8765 *(or any unused port)*:
```bash
cd backend
python -m uvicorn main:app --port 8765
```
Open your browser exactly at: **http://127.0.0.1:8765**

### 3. Run on Android Studio (Emulator)
To test the native Android version:
1. Open **Android Studio**
2. Click **Open** and select the `/android` folder from this repository.
3. Wait for Gradle to sync.
4. Click the **Run (Play) Button** to view the app directly on your emulator.

## 🛠 Tech Stack
- **Frontend**: React 18 & ReactDOM (CDN via Babel), Tailwind CSS, Phosphor Icons.
- **Backend**: Python, FastAPI, Uvicorn, Pydantic.
- **Database / Auth**: Supabase (PostgreSQL).
- **Mobile**: Java, Android SDK (Native WebView Wrapper).
