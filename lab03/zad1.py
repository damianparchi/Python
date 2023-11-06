import PyPDF2

def zlacz_pdf(input_file1, input_file2, output_file):
    # Otwórz oba pliki do połączenia w trybie binarnym
    with open(input_file1, 'rb') as file1, open(input_file2, 'rb') as file2:
        # Utwórz obiekty PdfReader dla obu plików wejściowych
        pdf1 = PyPDF2.PdfReader(file1)
        pdf2 = PyPDF2.PdfReader(file2)

        # Utwórz obiekt PdfWriter do zapisania połączonych plików
        pdf_writer = PyPDF2.PdfWriter()

        # Dodaj strony z pierwszego pliku
        for page_num in range(len(pdf1.pages)):
            page = pdf1.pages[page_num]
            pdf_writer.add_page(page)

        # Dodaj strony z drugiego pliku
        for page_num in range(len(pdf2.pages)):
            page = pdf2.pages[page_num]
            pdf_writer.add_page(page)

        # Zapisz połączony plik PDF
        with open(output_file, 'wb') as output:
            pdf_writer.write(output)

# Przykład użycia
file1 = 'projekty.pdf'
file2 = 'app-prop-pickle.pdf'
output_file1_plus_2 = 'opcja1.pdf'
output_file2_plus_1 = 'opcja2.pdf'

zlacz_pdf(file1, file2, output_file1_plus_2)  # plik1 + plik2
zlacz_pdf(file2, file1, output_file2_plus_1)  # plik2 + plik1
