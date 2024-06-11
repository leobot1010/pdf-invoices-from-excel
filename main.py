import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")        # imports all .xlsx files in a list

# A NEW PDF IS CREATES IN EACH ITERATION
for filepath in filepaths:

    filename = Path(filepath).stem
    invoice_no, the_date = filename.split("-")                      # double variable created in order [0] and [1]

    pdf = FPDF(orientation="P", unit="mm", format="A4")             # setup pdf object
    pdf.add_page()                                                  # add a page to the pdf object

    pdf.set_font(family="Times", size=16, style="B")                # begin setting up the content
    pdf.cell(w=50, h=8, txt=f"Invoice no: {invoice_no}", ln=1)      # add invoice number to pdf
    pdf.cell(w=50, h=8, txt=f"Date {the_date}", ln=1)               # add date to pdf

    # READ IN THE EXCEL DATA
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # ADD THE HEADER OF THE INVOICE
    columns = list(df.columns)      # list(df.columns) returns a list of all the values from row 1 of Excel document
    columns = [i.replace('_', ' ').title() for i in columns]   # removes the _ and capitalizes each word

    pdf.set_font(family="Times", size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # ADD THE PRODUCT ROW
    for index, columns in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(columns["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(columns["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(columns["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(columns["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(columns["total_price"]), border=1, ln=1)   # ** ln=1 drops to new line for next item

    pdf.output(f"PDFs/Invoice_no_{invoice_no}.pdf")                 # NOTE: you must manually create the PDFs folder
