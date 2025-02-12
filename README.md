Job Listings Web Scraper 🕵️‍♂️🔍

📌 Project Overview

This project is a Python-based web scraper that extracts job listings from TimesJobs.com using BeautifulSoup. The extracted data includes:
	•	✅ Company Name
	•	✅ Required Skills
	•	✅ Posted Date

The scraped job details are saved into a CSV file, making it easy to analyze job trends and required skills.

📁 Job-Scraper
│── main.py            # Main script to scrape job data
│── requirements.txt   # List of required Python packages
│── jobs_data.csv      # Output CSV file containing job listings
│── README.md          # Project documentation


⚙️ Technologies Used
	•	Python 🐍
	•	BeautifulSoup 🌐 (for web scraping)
	•	Requests 📡 (to fetch webpage data)
	•	Pandas 🏗️ (to store and save data in CSV format)

 📜 How It Works

1️⃣ Sends a request to the TimesJobs website.
2️⃣ Parses the HTML content using BeautifulSoup.
3️⃣ Extracts job details like company name, required skills, and post date.
4️⃣ Stores the extracted data in a Pandas DataFrame.
5️⃣ Saves the data as a CSV file for further analysis.

