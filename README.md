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
git clone https://github.com/gitzero728/240705-Scraping-about-remoterocketship.git
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

## Usage

1. **Run the script:**

```bash
python scraper.py
```

The script will start from the base URL (https://www.remoterocketship.com/advice) and navigate through the website, scraping questions and answers, and saving them as PDF files in a directory structure that mirrors the website's structure.

2. **Output:**

- PDF files will be saved in the specified directory structure.
- The script will print progress updates after every 10 PDF files are saved.

## Customization

- Base URL: Change the starting URL by modifying the base_url variable in the script.
- Directory Structure: Customize the directory where PDF files are saved by modifying the base_dir variable in the script.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for suggestions, bug reports, or feature requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- requests library for HTTP requests.
- beautifulsoup4 library for parsing HTML content.
- fpdf library for PDF generation.

### Explanation

1. **Introduction**: Briefly explains the purpose of the script with an eye-catching GIF demonstrating the script in action.
2. **Features**: Highlights the main features of the script.
3. **Requirements**: Lists the required Python version and packages.
4. **Installation**: Provides step-by-step instructions for setting up the environment and installing dependencies.
5. **Usage**: Describes how to run the script and the expected output.
6. **Customization**: Offers guidance on modifying the base URL and directory structure.
7. **Contributing**: Encourages contributions and provides guidelines.
8. **License**: Specifies the project's license.
9. **Acknowledgements**: Credits the libraries used in the script.
