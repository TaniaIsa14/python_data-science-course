import pandas as pd
my_fvrt={
    'Movie':[' witcher',' mermaid'],
    'Hobbi':['traveling','sleeping']

}
fvrt=pd.DataFrame(my_fvrt)
fvrt.to_csv('my_fvrt.csv',index=False)
df=pd.read_csv('my_fvrt.csv')
print(df)