# Project Description

This is an app that creates PDF invoices out of Excel Files.

# Notes

- openpyxl module need to be installed for pandas to be able to import excel files

# Errors

AttributeError: 'int' object has no attribute 'replace'. <br/>
This occurred when first attempting to write some of the invoice data to pdf. <br/>
The product_id column as well as other columns contain information as integers but <br/>
the pdf format only accepts strings. 

So I converted all cells to strings EG: <br/>

pdf.cell(w=30, h=8, txt=row["product_id"])  <br/>
to   <br/>
pdf.cell(w=30, h=8, txt=str(row["product_id"]))   <br/>
