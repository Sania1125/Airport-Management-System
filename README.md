
# 🛫 Airport Management System

A Python-based Airport Management System built using **Object-Oriented Programming (OOP)** and **Streamlit** for real-time dashboard interaction. It allows managing flights, booking passengers, storing data dynamically, and displaying flight manifests in a clean web interface.

---

## 🚀 Features

- ✈️ Add and manage multiple flights  
- 🧍 Book passengers by name and passport number  
- 📋 View live flight manifest  
- 💾 Data saved automatically to JSON (`flights.json` & `passengers.json`)  
- ✅ Prevents overbooking  
- 🌐 Interactive web dashboard with Streamlit

---

## 📂 Project Structure

```
airport-management-system/
├── airport.py                # OOP classes for flights and passengers
├── app.py                    # Command-line runner (optional)
├── streamlit_app.py          # Streamlit dashboard
├── data/
│   ├── flights.json          # Stores flight details
│   └── passengers.json       # Stores passenger bookings
├── utils/
│   └── helpers.py            # Utility functions (logging, summaries)
├── requirements.txt          # Dependencies
└── README.md                 # Project overview
```

---

## ▶️ How to Run the Streamlit App

### 1. Install requirements

```bash
pip install streamlit
```

### 2. Run the app

```bash
streamlit run streamlit_app.py
```

### 3. Open in browser

Visit: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Sample Flights in `flights.json`

```json
[
  {
    "flight_number": "PK303",
    "origin": "Karachi",
    "destination": "Lahore",
    "capacity": 2,
    "passenger_count": 2
  },
  {
    "flight_number": "PK404",
    "origin": "Islamabad",
    "destination": "Quetta",
    "capacity": 3,
    "passenger_count": 0
  }
]
```

---

## ✍️ Author

**Sania Irshad**  
GitHub: [@sania1125](https://github.com/sania1125)

---

