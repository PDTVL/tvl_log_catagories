import pandas as pd
path = "./LogExamples.xlsx"
writer=pd.ExcelWriter(path, engine='xlsxwriter')
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('MobiControl_68900482_search_results.csv')
df1=pd.concat([df[['Message']], df['Message'].str.split(r"\[|\]", expand=True)], axis=1)
df2=df1[1]
df5=df2.groupby(df2.tolist()).size().reset_index().rename(columns={0:'records'})
df3=df2.drop_duplicates()
df3=df3.sort_values()

MobiControlResultsList=[]
for category in df5['index']:
    idx = 0
    search=df.loc[(df["Message"].str.contains(category))]
    search.insert(loc=idx, column='Category', value=category)
    firstrow=search.head(1)
    MobiControlResultsList.append(firstrow)
    
MobiControlResultsList=pd.concat(MobiControlResultsList)

MobiControlResultsList.to_excel(writer, sheet_name="MobiControl", index=False)

writer.close()