import pandas as pd
import glob
from fpdf import FPDF
import os

filepaths = glob.glob("invoices/*.xlsx")   # imports all .xlsx files in a list


# we are creating a separate pdf for each iteration
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    invoice = os.path.basename(filepath)                    # extract invoice number from filepath
    idx_dash = invoice.index('-')
    invoice_no = invoice[:idx_dash]

    pdf = FPDF(orientation="P", unit="mm", format="A4")     # setup pdf object
    pdf.add_page()                                          # add a page to the pdf object
    pdf.set_font(family="Times", size=16, style="B")        # begin setting up the content
    pdf.cell(w=50, h=8, txt=f"Invoice no: {invoice_no}")
    pdf.output(f"PDFs/Invoice_no_{invoice_no}.pdf")         # you must manually create a PDFs folder first

