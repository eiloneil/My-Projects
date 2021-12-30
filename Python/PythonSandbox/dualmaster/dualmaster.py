import pandas as pd
# import pyperclip # If I could install the Pyperclip Module


final_query_txt = []
df = pd.read_clipboard()
for i, row in df.iterrows():
    txt = 'select '
    for col in df.columns:
        val = row[col]
        if type(val) in [type(5), type(5.1)]:
            val = val
        else:
            val = "'"+val.replace("'", "\'\'")+"'"
        
        txt += str(val) + ' as [' + col + '], '
    txt = txt[:-2] + ' UNION ALL'
    final_query_txt.append(txt)
final_query_txt[-1] = final_query_txt[-1][:-10]
for row in final_query_txt:
    print(row)
    
import subprocess
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

copy2clip(' '.join(final_query_txt))
    

# pyperclip.copy('\n'.join(final_query_txt)) # If I could install the Pyperclip Module
