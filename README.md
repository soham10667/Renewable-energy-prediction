# Renewable Energy Forecasting Frontend

Professional frontend application for solar / wind power prediction using Machine Learning.

## 🎯 Architecture

This is a **pure Vanilla JavaScript frontend** (HTML, CSS, JS) without any heavy frameworks.


```text
Hydrogen-Energy-ML-Project/
│
├── frontend/
│   ├── index.html                 # UI layout (HTML)
│   ├── styles.css                 # Styling (dark theme, responsive)
│   └── script.js                  # JavaScript logic (form + API calls)
│
├── backend/                       # Flask API + ML model
│   ├── app.py                     # REST API endpoints (/predict, /health)
│   ├── model.py                   # Loads ML model + scaler
│   ├── Linear_Regression_model.pkl
│   ├── scaler.pkl
│   └── requirements.txt           # Backend dependencies
│
└── data/
    └── renewable_energy_cleaned.csv   # Training dataset (features + target)
```


## 🚀 Quick Start

### Option 1: Run Locally (No Deployment)

**Backend (Flask API)**


1) Create and activate virtual environment (optional but recommended)
cd backend
pip install -r requirements.txt
2) Start Flask API
python app.py
API will be available at http://127.0.0.1:5000
text

**Frontend**


Open the UI directly
cd frontend
Option 1: double–click index.html and open in browser
Option 2: start simple static server
python -m http.server 8000
then open http://localhost:8000/frontend/index.html
text

Enter weather values (temperature, wind speed, humidity, solar irradiance) and click **Predict Energy Output** to see the predicted power output from the trained model.

### Option 2: Production Setup (Recommended)

- Host **backend** on a cloud platform (e.g. Render, Railway, Koyeb).  
- Host **frontend** on GitHub Pages or Netlify.

When backend has a public URL, update `API_BASE` in `frontend/script.js`:


// script.js
const API_BASE = "https://your-backend-service.onrender.com/api";
text

Commit and push, then your live GitHub Pages site will call the cloud Flask API.

## 📦 Dependencies

### Frontend

- HTML5 (structure)
- CSS3 (styling, responsive layout, dark theme)
- Vanilla JavaScript (form handling + Fetch API)

### Backend

- Python 3.x
- Flask
- NumPy
- scikit‑learn
- pickle / joblib

(See `backend/requirements.txt` for exact versions.)

## 🔧 Configuration

For local development, no `.env` file is required.  
If you deploy the backend, configure environment variables (like `PORT` or debug flags) on your hosting platform and set the frontend `API_BASE` URL accordingly in `script.js`.

## 📁 File Breakdown

### `frontend/index.html` (Structure)

- Semantic HTML5 layout  
- Two main cards: **Input Weather Data** and **Prediction Result**  
- Form fields for temperature, wind speed, humidity, solar irradiance  
- One primary button: **Predict Energy Output**

### `frontend/styles.css` (Styling)

- Dark, glassmorphism‑style UI (similar to modern AI dashboards)  
- Responsive grid layout for cards  
- Focus styles and hover effects for better UX  

### `frontend/script.js` (Logic)

- Reads values from form inputs  
- Sends `POST /api/predict` request to Flask backend with JSON body  
- Displays prediction text or error message in the **Prediction Result** panel  
- Prevents full‑page refresh using `event.preventDefault()`  

### `backend/app.py` (API)

- `GET /api/health` – Health check endpoint  
- `POST /api/predict` – Accepts weather values and returns predicted power output as JSON  

### `backend/model.py` (ML Model Wrapper)

- Loads `Linear_Regression_model.pkl` and `scaler.pkl`  
- Maps frontend inputs to the trained feature vector (`Feature_1` … `Feature_10`)  
- Applies scaler and runs model prediction  

## 🎨 Features

- ✅ Responsive design (desktop & mobile)  
- ✅ Dark UI optimized for dashboards  
- ✅ Clean separation between frontend and backend  
- ✅ Real‑time prediction for different weather scenarios  
- ✅ Ready for API deployment (CORS + JSON responses)  
- ✅ Pure HTML/CSS/JS (no frameworks)  

## 🌐 Deployment

### GitHub Pages (Static Frontend Hosting)


git push origin main
In GitHub repo settings → Pages:
- Source: main branch
- Folder: /(root) or /frontend (depending on your structure)
text

Your live site will be available at:

`https://<your-username>.github.io/Renewable-energy-prediction/`

### Backend Hosting (Flask API)

Example with Render:


Push code to GitHub
git push origin main
On Render:
- Create new Web Service from this repo
- Root directory: backend
- Build command: pip install -r requirements.txt
- Start command: python app.py
text

Update `API_BASE` in `script.js` to the Render service URL.

## 🔌 API Integration

The frontend integrates with the Flask backend using JSON.

**Endpoints**

- `POST /api/predict`  
  - Body:  
    ```
    {
      "temperature": 25.0,
      "wind_speed": 3.2,
      "humidity": 45.0,
      "solar_irradiance": 300.0
    }
    ```
  - Response:  
    ```
    {
      "prediction": 1.67
    }
    ```

- `GET /api/health`  
  - Returns `{"status": "ok"}` if the backend is running.

## 🧪 Testing

- Test locally by running backend + opening `frontend/index.html`.  
- For deployed backend, test `/api/health` in browser or Postman, then test frontend hosted on GitHub Pages.  

## 📊 Model & Data

- Input features: 10 engineered features (`Feature_1` … `Feature_10`) derived from weather and energy data.  
- Target: `Target` – renewable power output for a given time step.  
- Current model: Linear Regression with preprocessing via `scaler.pkl`.  

(You can replace with other models later, such as Random Forest, Gradient Boosting, or LSTM.)

## 📚 Future Work

- Add charts for actual vs predicted power curves  
- Integrate live weather API (Open‑Meteo, etc.)  
- Add model comparison page (Linear Regression vs Random Forest vs XGBoost)  

## 📄 License

MIT License – free to use, modify, and share.

## 👨‍💻 Author

- GitHub: `soham10667  
- Project: Renewable Energy Forecasting with Machine Learning

Made with ❤️ for sustainable energy .
