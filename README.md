# RemoteRocketship Scraper

![Scraping Demo](Scraping_about_remoterocketship.gif)

This Python script scrapes the [RemoteRocketship](https://www.remoterocketship.com/advice) advice section, extracts questions and answers, and saves them as individual PDF files. The script navigates through the website using a breadth-first search (BFS) algorithm, ensuring each page is only visited once.

## Features

- **Automated Scraping**: Efficiently scrapes questions and answers from RemoteRocketship.
- **PDF Generation**: Saves each question and its corresponding answer(s) as a separate PDF file.
- **BFS Navigation**: Utilizes a BFS algorithm to navigate the website and avoid revisiting pages.
- **Progress Updates**: Prints progress updates after every 10 PDF files are saved.

## Requirements

- Python 3.6+
- The following Python packages:
  - `requests`
  - `beautifulsoup4`
  - `fpdf`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/remoterocketship-scraper.git
   cd remoterocketship-scraper
   ```
2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required packages:**
   ```bash
   pip install requests beautifulsoup4 fpdf
   ```
