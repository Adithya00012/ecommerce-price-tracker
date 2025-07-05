import pandas as pd
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load latest scraped prices
latest_df = pd.read_csv('data/latest_prices.csv')
latest_df['Date'] = datetime.today().strftime('%Y-%m-%d')

# Prepare historical CSV
history_path = 'data/price_history.csv'
if os.path.exists(history_path):
    history_df = pd.read_csv(history_path)
    updated_df = pd.concat([history_df, latest_df], ignore_index=True)
else:
    updated_df = latest_df

# Save updated history
updated_df.to_csv(history_path, index=False)

# Find price drops
if os.path.exists(history_path):
    previous = updated_df.groupby('Title').nth(-2).reset_index()
    current = updated_df.groupby('Title').nth(-1).reset_index()
    merged = pd.merge(previous, current, on='Title', suffixes=('_old', '_new'))
    merged['Price_Drop'] = merged['Price_old'] > merged['Price_new']
    dropped = merged[merged['Price_Drop']]

    if not dropped.empty:
        print("\n📉 Price Drops Detected:\n")
        print(dropped[['Title', 'Price_old', 'Price_new']])

        # Send email alert
        sender_email = "your_email@gmail.com"
        receiver_email = "receiver_email@gmail.com"
        password = "your_app_password"

        subject = "📉 Price Drop Alert!"
        body = """<h3>Price Drop Detected:</h3><ul>"""
        for _, row in dropped.iterrows():
            body += f"<li><strong>{row['Title']}</strong>: £{row['Price_old']} → £{row['Price_new']}</li>"
        body += "</ul>"

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.attach(MIMEText(body, "html"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                print("\n📧 Email alert sent!")
        except Exception as e:
            print(f"\n⚠️ Failed to send email: {e}")
    else:
        print("\n✅ No price drops today.")
