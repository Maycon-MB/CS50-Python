# conversor.py
import tabula
import pandas as pd
from fpdf import FPDF

class Conversor:
    def __init__(self):
        pass

    def converter_pdf_para_csv(self, pdf_arquivo, csv_arquivo):
        # Converter PDF para CSV
        try:
            df = tabula.read_pdf(pdf_arquivo)
            df.to_csv(csv_arquivo, index=False)
            print(f"Arquivo CSV '{csv_arquivo}' gerado com sucesso!")
        except Exception as e:
            print(f"Erro ao converter PDF para CSV: {e}")

    def converter_csv_para_pdf(self, csv_arquivo, pdf_arquivo):
        # Converter CSV para PDF
        try:
            df = pd.read_csv(csv_arquivo)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for index, row in df.iterrows():
                texto = ", ".join(str(cell) for cell in row)
                pdf.cell(200, 10, txt=texto, ln=True, align="L")

            pdf.output(pdf_arquivo)
            print(f"Arquivo PDF '{pdf_arquivo}' gerado com sucesso!")
        except Exception as e:
            print(f"Erro ao converter CSV para PDF: {e}")
