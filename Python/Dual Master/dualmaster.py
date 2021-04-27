import pandas as pd

def df_to_sql(df, rtrn='list', export=False):
    """
    Turn Excel or any other Data-Frame into executable SQL
    
    Parameters:
    df (pandas.DataFrame): DataFrame of any kind. This will be the desired Table over which the user wishes to query.
    rtrn (str): Optionable for the user to chose whether the function will return the SQL query as a 'list' or a 'df'.
    export (bool): Optionable for the user to chose whether the function will export the sql df or not.
    
    Return:
    (list/pandas.DataFrame): Return the initial Table as a SQL query in the selected format (depends on the param 'rtrn')
    """
    
    df = df.fillna('NULL')
    final_query_txt = []
    
    for i, row in df.iterrows():
        txt = 'select '
        for col in df.columns:
            val = row[col]
            
            # IF STRING: Duplicate all apostrophes to preserve SQL syntax consistency
            if type(val) == type('string') and val != 'NULL': 
                val = "'"+val.replace("'", "\'\'")+"'"

            txt += str(val) + ' as [' + col + '], '
            
        txt = txt[:-2] + ' UNION ALL'
        final_query_txt.append(txt)

        # Eliminate the last 'union all' statement
    final_query_txt[-1] = final_query_txt[-1][:-10] 
        # Turn nan into NULL
    for i in range(len(final_query_txt)):
        final_query_txt[i] = final_query_txt[i].replace(' nan ', ' NULL ')
        # Define optional formats for the function to return, based on the user's selection (param 'rtrn')
    df_SQL = pd.DataFrame({'SQL':final_query_txt})
    results = {'list': final_query_txt
             , 'df':df_SQL}
    if export: # OPTIONAL: Export pd.df of SQL statements to current Folder
        df_SQL.to_excel('output_sql.xlsx')

    return results[rtrn]



df = pd.read_clipboard()
df_sql = df_to_sql(df, 'df', export=True)
df_sql.to_clipboard(index=False, header=False)
