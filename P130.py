import pandas as pd
import csv
df=pd.read_csv("total_stars.csv")
df
df.columns
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
finalData=df.dropna()
finalData.reset_index(drop=True,inplace=True)
finalData.to_csv("finalData.csv")
finalData.info()
finalData.describe
finalData.head(5)
finalData.dtypes(130)

