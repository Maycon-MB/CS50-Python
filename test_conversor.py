# test_conversor.py
import os
import pytest
from conversor import Conversor

def test_converter_pdf_para_csv():
    conversor = Conversor()
    pdf_arquivo = "exemplo.pdf"
    csv_arquivo = "exemplo.csv"

    conversor.converter_pdf_para_csv(pdf_arquivo, csv_arquivo)

    assert os.path.exists(csv_arquivo)

def test_converter_csv_para_pdf():
    conversor = Conversor()
    csv_arquivo = "exemplo.csv"
    pdf_arquivo = "exemplo.pdf"

    conversor.converter_csv_para_pdf(csv_arquivo, pdf_arquivo)

    assert os.path.exists(pdf_arquivo)
