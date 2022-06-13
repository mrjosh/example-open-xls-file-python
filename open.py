import pandas as pd

file_name = "./file_example_XLS_10.xls" # path to file + file name
sheet = "Sheet1" # sheet name or sheet number or list of sheet numbers and names

df = pd.read_excel(io=file_name, sheet_name=sheet)

print(df.head(5))  # print first 5 rows of the dataframe
