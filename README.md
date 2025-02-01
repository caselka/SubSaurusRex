# 🦖 Sub Saurus Rex

**Caselka's Multi-Host Async Dino Scanner with Subdomains & Web Dashboard**

🔍 **Sub Saurus Rex** is an advanced **asynchronous port scanner** that:
- Supports **multi-host scanning** 🏠  
- Automatically finds and scans **subdomains** 🌍  
- Includes a **Flask-powered web dashboard** for results 📊  
- Offers **stealth mode** for better evasion 🕵️‍♂️  
- Saves results in **JSON & CSV formats** 📁  
- Features a **dark mode UI** 🌙  

---

## **📌 Features**
✅ **Asynchronous & Fast:** Scans multiple ports in parallel.  
✅ **Subdomain Enumeration:** Finds subdomains using `crt.sh`.  
✅ **Live Web Dashboard:** View scan results in a browser.  
✅ **Stealth Mode:** Randomized delays to evade detection.  
✅ **Banner Grabbing:** Identifies services running on open ports.  
✅ **Dark Mode UI:** Toggle between light and dark themes.  

---

## **⚖️ Legal Disclaimer**

🚨 **Important Notice:**  
This tool is intended for **educational** and **lawful cybersecurity research only**.  
Unauthorized scanning or hacking attempts without explicit permission from the owner of the system **is illegal** and may result in **severe legal consequences**.

📌 **You MUST follow these guidelines:**
✅ Only scan **systems you own** or have **written permission** for.  
✅ **Comply** with all applicable **laws** and **regulations** in your country.  
✅ Use this tool **responsibly and ethically**.  
✅ Follow **responsible disclosure** guidelines.  
❌ **DO NOT** use this tool for **illegal activities**, hacking, or unauthorized access.  

**By using this software, you accept full responsibility for any actions taken with it.**  
**The author (Caselka) is not responsible for any misuse.**  

---

## **📦 Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/caselka/SubSaurusRex.git
cd SubSaurusRex
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **(Optional) 4️⃣ Automated Setup Using `setup.sh`**
Instead of manually setting up everything, just run:

```bash
bash setup.sh
```

This will:  
✅ Create the **virtual environment**  
✅ Activate it  
✅ Install **dependencies**  

---

## **🚀 How to Run the Scanner**

### **🔍 Scan a Single Host**
```bash
python3 scanner.py example.com 20 1000 --json --csv --web
```
✅ Scans `example.com` from **port 20 to 1000**  
✅ Saves results in **JSON & CSV formats**  
✅ Starts the **web dashboard**  

---

### **🌍 Scan Multiple Hosts**
```bash
python3 scanner.py example.com test.com 20 1000 --subdomains
```
✅ Scans multiple domains (`example.com` & `test.com`)  
✅ Finds **subdomains** and scans them  

---

### **🕵️‍♂️ Stealth Mode (Evade Detection)**
```bash
python3 scanner.py example.com 20 1000 --stealth
```
✅ **Adds random delays** to scans to **avoid detection**  

---

### **📊 Enable the Web Dashboard**
```bash
python3 scanner.py example.com 20 1000 --web
```
✅ Then visit:  
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  

---

## **🌍 Web Dashboard (Live Results)**

The scanner includes a **Flask-powered web dashboard** to view results in **real-time**.

### **📌 Running the Web Dashboard**
To start the dashboard:
```bash
python3 scanner.py example.com 20 1000 --web
```
✅ Visit:  
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  

🔹 Example Screenshot:  
*(Insert a screenshot of your dashboard here)*  

---

## **🌐 API Endpoints**

The scanner provides **API endpoints** for fetching scan results.

| **Endpoint**         | **Method** | **Description**                           |
|----------------------|-----------|-------------------------------------------|
| `/`                 | **GET**    | Displays the **web UI**.                  |
| `/api/scan-results` | **GET**    | Returns the **latest scan results** in JSON. |
| `/learning`         | **GET**    | Provides **cybersecurity learning resources**. |

---

## **📌 Fetching Scan Results via API**

### **🛠 Using `cURL`**
```bash
curl http://127.0.0.1:5000/api/scan-results
```

### **🐍 Using Python**
```python
import requests

response = requests.get("http://127.0.0.1:5000/api/scan-results")
data = response.json()

print(data)
```

### **📝 Example Output**

#### **📌 Terminal Output**
```plaintext
🔍 Scanning example.com from port 20 to 1000...
✅ Open ports on example.com: [22, 80, 443]

📁 Results saved to scan_results.json
📁 Results saved to scan_results.csv
🌍 Web Dashboard running at http://127.0.0.1:5000/
```

#### **📌 JSON API Response**
```json
{
  "results": [
    {"host": "example.com", "port": 22, "service": "SSH"},
    {"host": "example.com", "port": 80, "service": "HTTP"},
    {"host": "example.com", "port": 443, "service": "HTTPS"}
  ]
}
```

---

## **📜 License**
### **📌 Legal Compliance**
By using this software, you agree to the following:  

✅ You **will not** use it for illegal purposes.  
✅ You **will obtain explicit permission** before scanning any system.  
✅ You **understand** that unauthorized access to systems is **against the law**.  
✅ You **are solely responsible** for any consequences of misuse.  

---

## **👨‍💻 Author**
**Developed by [Caselka](https://github.com/caselka)** 🚀🔥  

---

## **🤝 Contributing**
**Contributions are welcome!** Follow these steps:

### **1️⃣ Fork the repository on GitHub.**
```bash
git clone https://github.com/your-username/SubSaurusRex.git
```

### **2️⃣ Create a new branch.**
```bash
git checkout -b feature-name
```

### **3️⃣ Make your changes and commit.**
```bash
git add .
git commit -m "Added new feature"
```

### **4️⃣ Push the branch and create a Pull Request.**
```bash
git push origin feature-name
```

---

## **❓ Need Help?**
- Open an issue on **GitHub Issues**.  
- Contact **Caselka** for further support.  

🚀 **Happy Legal & Ethical Hacking!** 🔥  

---

