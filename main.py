import pandas as pd

df = pd.read_excel("planilha.xlsx")
print(df.head(n=3))

# f = open("new_file.txt", "x")

f = open("new_file.txt", "a")
f.write("Now the file has more content!")
f.close()

