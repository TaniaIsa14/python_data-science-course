import pandas as pd
my_fvrt={
    ('kacci','hindi','chokerbali'),
    ('pulo','bangla','nishirat'),
    ('birani','robindro','gpyenda')

}
frvt_tuple=pd.DataFrame(data=my_fvrt,columns=['Food','Song','Book'])
print(frvt_tuple)