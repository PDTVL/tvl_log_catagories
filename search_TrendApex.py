import pandas as pd
path = "./LogExamples.xlsx"
writer=pd.ExcelWriter(path, engine='xlsxwriter')
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('trendApex.csv')
df1=pd.concat([df[['Message']], df['Message'].str.split("|", expand=True)], axis=1)
df2=df1[5]
df5=df2.groupby(df2.tolist()).size().reset_index().rename(columns={0:'records'})
df3=df2.drop_duplicates()
df3=df3.sort_values()

ApexResultsList=[]
for category in df5['index']:
    idx = 0
    search=df.loc[(df1[5].str.contains(category))]
    search.insert(loc=idx, column='Category', value=category)
    firstrow=search.head(1)
    ApexResultsList.append(firstrow)
    
ApexResultsList=pd.concat(ApexResultsList)

ApexResultsList.to_excel(writer, sheet_name="Apex", index=False)

writer.close()

