import pandas as pd

file_name = "./file_example_XLS_10.xls" # path to file + file name
sheet = "Sheet1" # sheet name or sheet number or list of sheet numbers and names

df = pd.read_excel(io=file_name, sheet_name=sheet)

data = []

for index, row in df.iterrows():
    data.append({
        "id": int(row["Id"]),
        "first_name": row["First Name"],
        "last_name": row["Last Name"],
        "gender": row["Gender"],
        "country": row["Country"],
        "age": int(row["Age"]),
    })

print(data)
