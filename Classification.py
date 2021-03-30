import pandas as pd

###### Import Data
df_2020 = pd.read_csv('Osiris_20_Full_EU17_NonmiGUOTypecopy.csv', na_values = ['n.a.'], encoding='cp1252')
df_prev = pd.read_csv('Osiris_171819_Full_EU17_NonmiGUOType_Bearbeitet_Ausgefullt.csv', encoding='cp1252')

### Set Export File's Columns
export_cols = ['BvDIDnumber', 'Companyname', 'year', 'GUOName', 'GUOType', 'GUODirect', 'ICF', 'FFF'] 


companies = df_2020['BvDIDnumber'].unique()

firm_dfs = []
for company in companies:
    df_firm = df_2020.loc[df_2020['BvDIDnumber'] == company]

    ###### Classification
    ### Firms Controlled by Individuals
    df_firm.loc[(df_firm['GUOType'] == 'One or more named individuals or families') | (df_firm['GUOType'] == 'Employees, managers, directors'), 'ICF'] = 1
    df_firm.loc[df_firm['ICF'] != 1, 'ICF'] = 0

    ### Family Founding Firms
    df_firm.loc[:, 'FFF'] = ''
    df_firm.loc[df_firm['ICF'] == 0, 'FFF'] = 0

    firm_dfs.append(df_firm)

firm_dfs.append(df_prev)
df_total = pd.concat(firm_dfs)
df_total = df_total[export_cols]
df_total = df_total.sort_values(by = ['BvDIDnumber', 'year', 'GUODirect'], ascending = True)

### Carry over Classification from 2019
companies = df_total['BvDIDnumber'].unique()
for company in companies:
    df_firm = df_total.loc[df_total['BvDIDnumber'] == company]
    # print(df_firm)
    if len(df_firm.loc[df_firm['year'] == 2019]) >= 1 and len(df_firm.loc[df_firm['year'] == 2020]) >= 1:
        if df_firm.loc[df_firm['year'] == 2019, 'FFF'].values[0] == 1:
            GUOname_2019 = df_firm.loc[df_firm['year'] == 2019, 'GUOName'].values[0]
            GUOname_2020 = df_firm.loc[df_firm['year'] == 2020, 'GUOName'].values[0]
            if GUOname_2019 == GUOname_2020:
                df_total.loc[(df_total['year'] == 2020) & (df_total['BvDIDnumber'] == company), 'FFF'] = 1
                df_total.loc[(df_total['year'] == 2020) & (df_total['BvDIDnumber'] == company), 'ICF'] = 0
    else:
        pass

df_total.to_csv('test1.csv')

print('Finished')