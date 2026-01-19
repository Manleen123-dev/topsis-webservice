# topsis-webservice
 Repo for rendering my Topsis package
 # TOPSIS Web Service

A production-ready **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** REST API built with Flask and deployed on Render.

## 🔗 Live URL

[https://topsis-webservice.onrender.com](https://topsis-webservice.onrender.com)

> **Note (Free Tier):** First request may take ~30–50 seconds due to cold start.

---

## 🚀 Features

* Textbook-correct TOPSIS implementation
* JSON REST API
* Deployed with Gunicorn on Render
* Auto-deploy via GitHub

---

## 🧮 API

### Health Check

**GET /**

**Response**

```
TOPSIS web service running
```

---

### TOPSIS Prediction

**POST /predict**

#### Request Body (JSON)

```json
{
  "matrix": [[250,16,12],[200,20,8],[300,12,16]],
  "weights": [0.4,0.3,0.3],
  "impacts": ["+","-","+"],
  "labels": ["A1","A2","A3"]
}
```

#### Response (JSON)

```json
{
  "scores": {
    "A1": 0.5,
    "A2": 0.0,
    "A3": 1.0
  },
  "ranking": ["A3", "A1", "A2"]
}
```

---

## 🛠️ Tech Stack

* **Python**
* **Flask** (API)
* **NumPy** (TOPSIS math)
* **Gunicorn** (Production WSGI)
* **Render** (Deployment)

---

## 📦 Local Setup

```bash
pip install -r requirements.txt
python app.py
```

Test locally:

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "matrix": [[250,16,12],[200,20,8],[300,12,16]],
  "weights": [0.4,0.3,0.3],
  "impacts": ["+","-","+"],
  "labels": ["A1","A2","A3"]
}'
```

---

## 🎓 Notes

* Follows standard TOPSIS steps used in academic syllabi.
* Weights are used as provided (no forced normalization unless required by instructor).

---

## 👤 Author

Manleen Kaur

