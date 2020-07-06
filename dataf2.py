import pandas as pd
my_fvrt={
    'Movie':[' witcher',' mermaid'],
    'Hobbi':['traveling','sleeping']

}
fvrt=pd.DataFrame(my_fvrt)
fvrt.to_excel('my_fvrt.xlsx','sheet1', index =False )
df1=pd.read_excel('my_fvrt.xlsx','sheet1')
print(df1)