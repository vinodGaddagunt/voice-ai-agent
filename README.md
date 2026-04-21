# FastAPI Real-Time Agent (WebSocket + REST)

## 🚀 Project Overview

This project is a backend service built using FastAPI. It supports both REST APIs and real-time communication using WebSockets.

The system processes user input and extracts intent such as booking, canceling, or rescheduling an appointment using simple rule-based logic.

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone <your-repo-link>
cd project
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the server:

```
uvicorn main:app --reload
```

4. Open in browser:

* REST APIs: http://127.0.0.1:8000/docs
* WebSocket: ws://127.0.0.1:8000/ws

---

## 🧠 Architecture Overview

* FastAPI handles HTTP and WebSocket requests
* WebSocket enables real-time communication
* Agent logic processes user input and extracts intent
* Configuration is managed using environment variables

---

## 🔄 API Endpoints

### GET /

Returns API status

### GET /test

Returns test response

### WebSocket /ws

Handles real-time communication:

* Receives user input
* Processes intent
* Sends JSON response

---

## 🧩 Memory Design

* Stateless session handling using session_id
* Each request is processed independently
* No persistent storage used

---

## ⚡ Latency Breakdown

* FastAPI provides low-latency responses
* WebSocket enables real-time communication
* Processing time depends on input handling logic

---

## ⚖️ Tradeoffs

* Used rule-based intent detection instead of ML for simplicity
* No database integration to keep system lightweight
* Single-user session handling

---

## ⚠️ Known Limitations

* Intent detection is basic and keyword-based
* No authentication implemented
* Requires API key for external integrations
* No persistent memory or database

---

## 📦 Requirements

```
fastapi
uvicorn
python-dotenv
```

---

## 🎥 Demo

The Loom video demonstrates:

* Running the server
* Testing endpoints via Swagger UI
* WebSocket interaction

---

## ✅ Final Notes

* Make sure API key is not exposed in code
* Ensure project runs using `uvicorn main:app --reload`
* Keep repository clean and structured

---
