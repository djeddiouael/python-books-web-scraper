# 📚 Python Books Web Scraper

A simple Python web scraping project that extracts book information from [Books to Scrape](https://books.toscrape.com/) and saves the collected data into a CSV file.

This project was built to practice web scraping fundamentals using Python, Requests, and BeautifulSoup.

## 🚀 Features

- Extracts book titles
- Extracts book prices
- Extracts book ratings
- Extracts book availability
- Automatically navigates through all pages
- Saves the results into a CSV file
- Includes a delay between requests

## 🛠️ Technologies Used

- **Python 3**
- **Requests** – to send HTTP requests
- **BeautifulSoup** – to parse HTML content
- **CSV** – to store extracted data

## 📁 Project Structure

```text
python-books-web-scraper/
│
├── scraper.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── data/
    └── books.csv
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/djeddiouael/python-books-web-scraper.git
```

### 2. Navigate to the project directory

```bash
cd python-books-web-scraper
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the scraper:

```bash
python scraper.py
```

The extracted data will be saved automatically to:

```text
data/books.csv
```

## 📊 Extracted Data

The scraper collects the following information:

| Field | Description |
|---|---|
| Title | Book title |
| Price | Book price |
| Rating | Book rating |
| Availability | Stock availability |

**Result:** 1,000 books extracted from 50 pages.

## 🌐 Target Website

[Books to Scrape](https://books.toscrape.com/)

This website is designed specifically for practicing web scraping.

## 🎯 Learning Objectives

Through this project, I practiced:

- Sending HTTP requests with Python
- Parsing HTML using BeautifulSoup
- Finding HTML elements with CSS selectors
- Extracting structured information
- Navigating multiple pages
- Saving data into CSV files
- Organizing a Python project using Git and GitHub

## 🔮 Future Improvements

- Store extracted books in a PostgreSQL database
- Add error handling and logging
- Implement retry mechanisms
- Schedule automatic scraping
- Export data to JSON and Excel

## 👨‍💻 Author

**Ouael Djeddi**

- GitHub: [@djeddiouael](https://github.com/djeddiouael)

---

⭐ If you find this project useful, feel free to star the repository!
