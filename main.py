import fitz  # PyMuPDF
import pandas as pd

def extract_text_from_pdf(pdf_path):
    """Extracts text from each page of the specified PDF."""
    doc = fitz.open(pdf_path)
    texts = [page.get_text() for page in doc]
    doc.close()
    return texts

def process_text_to_qa(texts):
    """
    Process the list of texts to extract or create question-answer pairs.
    This function needs to be adapted based on the structure of your PDF.
    """
    qa_pairs = []
    # Example: Assume each line in the text is a new Q&A, question and answer separated by a question mark
    for text in texts:
        lines = text.split('\n')
        for line in lines:
            if '?' in line:  # Simple heuristic to find questions
                parts = line.split('?')
                if len(parts) == 2:  # Simple Q&A format
                    question, answer = parts[0] + '?', parts[1].strip()
                    qa_pairs.append((question, answer))
    return qa_pairs

def create_anki_csv(qa_pairs, csv_path="anki_cards.csv"):
    """Saves the question-answer pairs to a CSV file."""
    df = pd.DataFrame(qa_pairs, columns=['Front', 'Back'])
    df.to_csv(csv_path, index=False, sep=";")  # Anki expects semicolon by default

# Example usage



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pdf_path = "CPCU3_550_1e_PM_FC.pdf"  # Change this to the path of your PDF
    texts = extract_text_from_pdf(pdf_path)
    qa_pairs = process_text_to_qa(texts)
    create_anki_csv(qa_pairs)

    print("Anki cards CSV generated successfully.")
    print("Start processing")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
