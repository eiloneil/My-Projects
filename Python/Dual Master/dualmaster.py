import pandas as pd

def df_to_sql(df, rtrn='str', query_type='SELECT'):  # AKA DualMaster
    """
    Turn Excel or any other Data-Frame into executable SQL

    Parameters:
    - df (pandas.DataFrame): DataFrame of any kind. This will be the desired Table over which the user wishes to query.
    - rtrn (str): Optionable for the user to chose whether the function will return the SQL query as a 'list', 'str' or a 'df'.
    - query_type (str/int): Optionable for the user to chose whether the function will return the SELECT query for the
                            input data (query_type='SELECT' or 0), or the INSERT query to append it to an
                            existing table (query_type='INSERT' or 1)

    Return:
    (list/pandas.DataFrame): Return the initial Table as a SQL query in the selected format (depends on the param 'rtrn' and 'query_type')
    """

    df = df.fillna('NULL')
    df.columns = (col.replace('  ', '_').replace(' ', '_').replace("'", '').replace('"', '') for col in df.columns)
    final_query_txt = []

    if query_type in ('SELECT', 0):
        for i, row in df.iterrows():
            txt = 'select '
            for col in df.columns:
                val = row[col]

                # IF STRING: Duplicate all apostrophes to preserve SQL syntax consistency
                if val != 'NULL' and not str(val).isdigit():
                    val = str(val).replace("'", "''")
                    val = "'" + (val) + "'"
                txt += str(val) + ' as ' + col + ', '

            txt = txt[:-2] + ' UNION ALL'
            final_query_txt.append(txt)

        # Eliminate the last 'union all' statement
        final_query_txt[-1] = final_query_txt[-1][:-10]

    elif query_type in ('INSERT', 1):
        txt = f'INSERT INTO TABLE_NAME ({", ".join(list(df.columns))})\nVALUES \n'
        final_query_txt.append(txt)
        for i, row in df.iterrows():

            str_lst = map(str,list(row))
            lst_str = ", ".join(map(lambda x: "'" + x.replace("'", "''") + "'" if (not x.lstrip("-").isdigit()) and x!='NULL' else x,str_lst))
            val = f'( {lst_str} ),\n'

            final_query_txt.append(val)

        # Eliminate the last ','
        final_query_txt[-1] = final_query_txt[-1][:-2]

    # Turn nan into NULL
    for i in range(len(final_query_txt)):
        final_query_txt[i] = final_query_txt[i].replace(' nan ', ' NULL ')
        # Define optional formats for the function to return, based on the user's selection (param 'rtrn')
    df_SQL = pd.DataFrame({'SQL': final_query_txt})
    results = {'list': final_query_txt
        , 'df': df_SQL
        , 'str': ' '.join(final_query_txt)}

    return results[rtrn]



df = pd.read_clipboard()
df_sql = df_to_sql(df)
df_sql.to_clipboard(index=False, header=False)
