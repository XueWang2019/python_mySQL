#### Case1: choose a specific value in a certaincolumns to create another DataFrame:
df:DataFrame  
df_1=df[df.col1=="Yes"] # df_1 is DataFrame too

#### Case2: check a specific value in a certain column
(df['cols']=="Yes).sum  # this will show the detail information for each record, like False, True  
(df['cols']=="Yes).sum() # this will show the result for the column named cols with value Yes, like 100

#### Case3: follow the case1:
Here df_1 might inherite the index from df, but as only choose part of original data, you might want to delete the original index and create new:  
use drop and reset_index  
df_1.reset_index(drop=True)  

#### case4: show a specific value in a certain column
df[df['col1']=='Yes'] (DF) or df[df['col].isna()] (DF) or df[df['col].isna()].shape

### case 5: how to merge different rows into one
df_postcodes = df_html.groupby(['Postal Code','Borough']).Neighborhood.agg([('Neighborhood', ', '.join)])
