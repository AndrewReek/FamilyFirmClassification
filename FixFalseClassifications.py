import pandas as pd

df = pd.read_csv('test1.csv', encoding='latin1')
df_fixes = pd.read_csv('ClassificationFixes.csv', encoding='latin1')

for i in range(len(df_fixes)):
    Id = df_fixes['BvDID Number'].iloc[i]
    Year = df_fixes['Year'].iloc[0]
    Founder = df_fixes['Founder'].iloc[i]
    ICF = df_fixes['ICF'].iloc[i]
    FFF = df_fixes['FFF'].iloc[i]
    Source = df_fixes['Source'].iloc[i]
    Comment = df_fixes['Comment'].iloc[i]

    df.loc[(df['BvDIDnumber'] == Id) & (df['year'] == Year), 'Founder Name'] = Founder
    df.loc[(df['BvDIDnumber'] == Id) & (df['year'] == Year), 'ICF'] = ICF
    df.loc[(df['BvDIDnumber'] == Id) & (df['year'] == Year), 'FFF'] = FFF
    df.loc[(df['BvDIDnumber'] == Id) & (df['year'] == Year), 'Source'] = Source
    df.loc[(df['BvDIDnumber'] == Id) & (df['year'] == Year), 'Comment'] = Comment

df.to_csv('FixedClassifications.csv', columns = ['BvDIDnumber', 'year', 'Founder Name', 'ICF', 'FFF', 'Source', 'Comment'], encoding = 'latin1')   