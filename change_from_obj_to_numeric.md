If the coulmn of the DataFrame needs to be int64, but it includes some none numerical data, now it needs to get the data without the NaN data.  

First, use error='coerce' to force the none numerical data into NaN, then use notnull to get the None null data,  
then use astype to change it to int64:  

df=df[pd.to_numeric(df['col1'],error='coerce').notnull()]
df['col1']=df['col1'].astype('int')
df.dtypes
