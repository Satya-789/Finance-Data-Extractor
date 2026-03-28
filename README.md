
# 📊 Financial Data Extractor

A Streamlit-based web application that extracts key financial metrics like **Revenue** and **EPS (Earnings Per Share)** from unstructured news articles using **LLMs (Groq + LangChain)**.

---

## 🚀 Features

* 🔍 Extracts:

  * Revenue (Actual vs Expected)
  * EPS (Actual vs Expected)
* 🤖 Powered by **Groq LLM (LLaMA 3)**
* ⚡ Fast and interactive UI with **Streamlit**
* 📊 Displays results in a structured table
* 🔐 Secure API key handling using environment variables

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **LLM**: Groq (LLaMA 3.3 70B)
* **Framework**: LangChain
* **Data Handling**: Pandas

---

## 📂 Project Structure

```
finance-data-extractor/
│
├── app.py                  # Streamlit UI
├── data_extractor.py       # LLM extraction logic
├── requirements.txt        # Dependencies
├── .env.example            # Environment variables template
├── .gitignore
└── README.md
```

---



## 📌 Example Input

```
Apple reported quarterly revenue of $90 billion, beating expectations of $85 billion. 
EPS came in at $1.50 compared to estimates of $1.30.
```

---

## 📊 Example Output

| Measure | Estimated | Actual |
| ------- | --------- | ------ |
| Revenue | 85B       | 90B    |
| EPS     | 1.30      | 1.50   |

---
Link to the app- https://finance-data-extractor-i9.streamlit.app/


---
