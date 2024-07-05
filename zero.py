import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from fpdf import FPDF
from collections import deque

base_url = "https://www.remoterocketship.com/advice"
visited = set()
savedPdf = 0

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_font('Arial', '', 12)  # Set default font for body text

    def chapter_body(self, body, is_question=False):
        if is_question:
            self.set_text_color(51, 102, 153)  # Weak blue color for questions
            self.set_font('Arial', 'B', 14)
        else:
            self.set_text_color(0, 0, 0)  # Black color for answers
            self.set_font('Arial', '', 12)
        
        body = body.encode('latin1', 'replace').decode('latin1')
        self.multi_cell(0, 10, body)
        self.ln()

    def chapter_title(self, title):
        self.chapter_body(title, is_question=True)  # Just use the title directly

def save_full_page_to_pdf(dir_path, file_name, questions):
    # Ensure the directory exists
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    # Construct file path
    file_path = os.path.join(dir_path, file_name + ".pdf")
    
    # Create PDF and save questions
    pdf = PDF()
    for question in questions:
        pdf.add_page()
        pdf.chapter_title(question['title'])
        pdf.chapter_body(question['content'], is_question=False)
    pdf.output(file_path)

    global savedPdf
    savedPdf += 1
    if savedPdf % 10 == 0:
        print("Saved", savedPdf, "pdf files")

def bfs(start_url, base_dir):
    queue = deque([(start_url, base_dir)])
    visited.add(start_url)

    while queue:
        url, dir = queue.popleft()

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        file_name = urlparse(url).path.split('/')[-1]

        # Check for content indicating leaf URLs
        flatContentCheckingLeafUrl = "Looking for a remote tech job? Search our job board for 30,000+ remote jobs"
        if flatContentCheckingLeafUrl in response.text:
            # Store information about current page
            h3_tags = soup.find_all('h3')
            questions = []
            for h3 in h3_tags:
                question = {'title': h3.get_text(), 'content': ''}
                next_elem = h3.find_next_sibling()
                while next_elem and next_elem.name != 'h3':
                    question['content'] += next_elem.get_text() + "\n"
                    next_elem = next_elem.find_next_sibling()
                questions.append(question)
            
            save_full_page_to_pdf(dir, file_name, questions)
            continue

        subDir = os.path.join(dir, file_name)

        # Enqueue all sub-URLs
        for a in soup.find_all('a', href=True):
            full_url = urljoin(base_url, a['href'])
            if full_url.startswith(base_url) and full_url not in visited:
                visited.add(full_url)
                queue.append((full_url, subDir))

if __name__ == "__main__":
    bfs(base_url, "")

    print("Saved", savedPdf, "pdf files")
