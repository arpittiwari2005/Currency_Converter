# Currency_Converter
The Real-Time Currency Converter is a Python-based desktop application designed to provide instant and accurate currency conversions using live exchange rates. It has been developed with the Tkinter library for a user-friendly graphical interface and integrates real-time data through external APIs, making it reliable and practical for everyday use.


# 💱 Real-Time Currency Converter

A **Python-based desktop application** built with **Tkinter** to convert currencies in real time using live exchange rates from online APIs.  
This project supports more than **150 international currencies** (ISO 4217 standard) and provides a clean, user-friendly interface.

---

## 🚀 Features
- 🌍 Supports 150+ world currencies  
- 🔄 Real-time exchange rates using online APIs  
- 🛡️ Fallback API support for reliability (`open.er-api.com` and `exchangerate.host`)  
- ⚡ Instant conversion with a single click  
- 🎨 User-friendly Tkinter-based GUI  
- ❌ Error handling for invalid inputs or no internet connection  

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Libraries:**  
  - `tkinter` – GUI framework  
  - `requests` – API requests for exchange rates


currency-converter/
│── venv/                   # Virtual environment folder (should NOT be pushed to GitHub)
│── currency_converter.py   # Main application file
│── README.md               # Documentation
🔧 Steps to Create & Use Virtual Environment


1. Create Virtual Environment
Run in your project folder:

python -m venv venv


2. Activate Virtual Environment
Windows (PowerShell):

bash
Copy code
.\venv\Scripts\activate


Linux / macOS:

bash
Copy code
source venv/bin/activate


3. Install Dependencies
bash
Copy code
pip install requests


5. Freeze Dependencies into requirements.txt
bash
Copy code
pip freeze > requirements.txt
This will create a file like:

txt
Copy code
requests==2.31.0


bash
Copy code
python -m venv venv
source venv/bin/activate   # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
And the project will run perfectly.

