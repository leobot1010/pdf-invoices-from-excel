import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")   # imports all .xlsx files in a list

# a new pdf in created in each iteration
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    filename = Path(filepath).stem
    invoice_no, the_date = filename.split("-")                      # double variable created in order [0] and [1]

    pdf = FPDF(orientation="P", unit="mm", format="A4")             # setup pdf object
    pdf.add_page()                                                  # add a page to the pdf object

    pdf.set_font(family="Times", size=16, style="B")                # begin setting up the content
    pdf.cell(w=50, h=8, txt=f"Invoice no: {invoice_no}", ln=1)      # add invoice number to pdf
    pdf.cell(w=50, h=8, txt=f"Date {the_date}", ln=1)               # add date to pdf

    pdf.output(f"PDFs/Invoice_no_{invoice_no}.pdf")                 # you must manually create the PDFs folder

