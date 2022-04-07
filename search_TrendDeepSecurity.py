import pandas as pd
path = "./LogExamples.xlsx"
writer=pd.ExcelWriter(path, engine='xlsxwriter')
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('TrendDeepSecurity_68900482_search_results.csv')
df1=pd.concat([df[['Message']], df['Message'].str.split("|", expand=True)], axis=1)
#df2=pd.concat([df1[['Message']], df1[7].str.split(r" |{|}|,", expand=True)], axis=1)
df2=df1[5]
df5=df2.groupby(df2.tolist()).size().reset_index().rename(columns={0:'records'})
df3=df2.drop_duplicates()
df3=df3.sort_values()

DeepSecurityResultsList=[]
for category in df5['index']:
    idx = 0
    search=df.loc[(df1[5].str.contains(category))]
    search.insert(loc=idx, column='Category', value=category)
    firstrow=search.head(1)
    DeepSecurityResultsList.append(firstrow)
    
DeepSecurityResultsList=pd.concat(DeepSecurityResultsList)

DeepSecurityResultsList.to_excel(writer, sheet_name="DeepSecurity", index=False)

writer.close()