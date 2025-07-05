# ecommerce-price-tracker/README.md

# 🛒 E-commerce Price Tracker & Scraper

This project scrapes product data from [books.toscrape.com](http://books.toscrape.com), tracks daily prices, and sends email alerts when price drops are detected. It’s a great showcase for web scraping, automation, and freelance data processing skills.

---

## 🚀 Features

- 🔎 Scrapes product titles, prices, availability, and ratings
- 🗃 Logs daily prices into a historical CSV file
- 📉 Detects and reports price drops
- 📧 Sends automated email alerts for dropped prices

---

## 🛠 Tech Stack

- Python
- BeautifulSoup (Web Scraping)
- pandas (Data Handling)
- smtplib (Email Notification)

---

## 📂 Folder Structure
```
📁 ecommerce-price-tracker
├── scraper.py          # Scrapes and saves latest product prices
├── price_tracker.py    # Tracks price changes, sends email alerts
├── data/
│   ├── latest_prices.csv   # Today's scraped prices
│   └── price_history.csv   # Historical price data
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/ecommerce-price-tracker.git
cd ecommerce-price-tracker
```

2. **Install dependencies**:
```bash
pip install requests beautifulsoup4 pandas
```

3. **Run scraper & tracker**:
```bash
python scraper.py
python price_tracker.py
```

4. **Configure Email Alerts**:
- Edit `price_tracker.py`
- Replace with your credentials:
```python
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_app_password"  # Use Gmail App Password
```

---

## 💼 Freelancing Use Case
This project demonstrates skills in:
- Web scraping and data collection
- Data processing and automation
- Real-world business use (e.g., price monitoring)

Perfect to showcase on your Upwork/Freelancer portfolio to attract clients in e-commerce, analytics, or automation.

---

## ✅ Future Improvements
- Support multiple e-commerce sites (Flipkart, Amazon, etc.)
- Store data in a database (e.g., SQLite, Firebase)
- Add dashboard with Streamlit or Flask
- Schedule auto-run using cron or Task Scheduler

---

## 📬 Contact
For project inquiries or freelance collaboration:
**Your Name**  
[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername) | your_email@gmail.com
