import pandas as pd
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('GoogleWorkspace_68900482_log_results.csv')
df1=pd.concat([df[['message']], df['message'].str.split(r',', expand=True)], axis=1)
df2=df1[3]
df5=df2.groupby(df2.tolist()).size().reset_index().rename(columns={0:'records'})
df3=df2.drop_duplicates()
df3=df3.sort_values()

drive_df=df.loc[(df['message'].str.contains('applicationName":"drive"',na=False))]
drive=pd.concat([drive_df[['message']], drive_df['message'].str.split(r'{|}', expand=True)], axis=1)
shared_external=df.loc[(df['message'].str.contains('shared_externally',na=False))]
externalsplit=pd.concat([shared_external[['message']], shared_external['message'].str.split(r'"name":"doc_title","value":"|"},{"', expand=True)], axis=1)
df.where(df.apply(lambda x: x.str.contains('hello')))

dfcheck=externalsplit.apply(lambda row: row.astype(str).str.contains('"name":"doc_title"').any(), axis=1)
