#  Finance Assistant Chatbot – Real-Time Expense Tracker 

This project is a simple and smart expense tracker powered by an AI chatbot. You can type in messages like "Add $50 for groceries today", and the app will understand it, extract the details, send them through Kafka, store everything in Azure SQL, and help you see your spending habits through a visual dashboard.

---

## Features 🚀 
-  AI Chatbot to understand natural language inputs
- Real-time stream processing with Apache Kafka
- Azure SQL for persistent expense storage
- D3.js dashboard for visual analytics (browser-based)
- Flask-based web UI

---

## Project Structure
```
finance-assistant-chatbot/
 app.py                 # Flask app
 chatbot.py             # NLP logic
 kafka_producer.py      # Sends parsed messages to Kafka
 kafka_consumer.py      # Reads from Kafka and writes to Azure SQL
 azure_sql.py           # DB connector
 templates/index.html   # Web UI with chatbot + dashboard placeholder
 static/                # (For future CSS/JS assets)
 requirements.txt
 README.md
```

---

##  Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/finance-assistant-chatbot.git
cd finance-assistant-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start local Kafka (for simulation)
Make sure Apache Kafka is installed. Then:
```bash
# In one terminal
bin/zookeeper-server-start.sh config/zookeeper.properties

# In another terminal
bin/kafka-server-start.sh config/server.properties

# Create topic
bin/kafka-topics.sh --create --topic expenses --bootstrap-server localhost:9092
```

### 4. Run the Flask app
```bash
python app.py
```

### 5. Run the Kafka consumer
```bash
python kafka_consumer.py
```

---

## Sample Input
You can type natural language like:
> Add $75 for shopping today  
> Add $20 for transport on 3rd April
- The app will figure out the category, amount, and date.
---

## ☁Azure SQL Setup
In `azure_sql.py` update your connection string like this:
```python
connect_to_azure():
    DRIVER={ODBC Driver 17 for SQL Server};
    SERVER=your_server.database.windows.net;
    DATABASE=your_db;
    UID=your_user;
    PWD=your_password
```

Create `expenses` table:
```sql
CREATE TABLE expenses (
    id INT IDENTITY(1,1) PRIMARY KEY,
    amount FLOAT,
    category VARCHAR(100),
    date DATE
);
```

---

##  Dashboard Preview
A basic D3.js dashboard is included in the frontend. You can extend it to create more interactive charts and graphs based on your expense data.

---

##  Contributions
If you have ideas to improve the chatbot’s understanding, make the dashboard better, or just want to help out, feel free to send a pull request!

---

##  Contact
Created by Jayanth Manthrigalla. For questions or feedback, reach out via GitHub.

## Note
 Azure SQL and Kafka credentials are excluded for security reasons.
