import tabula
import pandas as pd
import numpy as np
file="E:\scrape\SanchayPar.pdf"

table=tabula.read_pdf(file,pages=2)

tabula.convert_into("SanchayPar.pdf","output_h.csv",output_format="csv",pages=2)

