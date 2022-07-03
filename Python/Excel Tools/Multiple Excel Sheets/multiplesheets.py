import pandas as pd
import os
import glob


BOOL_DICT = {'y':True, 'n':False, 'v':True, 's':True, 'f':False}
CHARS_TO_AVOID = '[]:*?/\\'

def remove_chars(txt):
    valid_txt = ''.join([char for char in txt if char not in CHARS_TO_AVOID])
    return valid_txt

def list_to_dict(lst):
    new_dict = {}
    for i in range(len(lst)):
        new_dict[i+1] = lst[i]

    return new_dict


def print_dict(dict):
    for key in dict.keys():
        print(key, '-', dict[key])
    print()

    
def choose_file(dir_path):
    # Get all Excel Files
    print('\nExcels in chosen folder: ')

    filenames_lst = [filename.replace(dir_path+'/', "") for filename in glob.glob(os.path.join(dir_path, '*.xlsx'))]
    filenames_dict = list_to_dict(filenames_lst)
    print_dict(filenames_dict)
    # Choose Excel
    excel_number = int(input('Insert Excel NUMBER: '))
    return filenames_dict[excel_number]

    
def choose_sheet(path):
    # Get all Excel Sheets
    print('\nSheets in chosen Excel: ')
    
    xl_sheets = pd.ExcelFile(path).sheet_names
    sheets_dict = list_to_dict(xl_sheets)
    print_dict(sheets_dict)
    sheet_number = int(input('Insert Sheet NUMBER: '))
    return sheets_dict[sheet_number]


def split_by_col_vals(df, cols_dict):
    dfs = {}
    
    print('\nColumns in chosen Excel: ')
    print_dict(cols_dict)
    
    # Choose Column
    chosen_col_num = int(input('Choose column NUMBER to group by which: '))
    chosen_col = cols_dict[chosen_col_num]
    split_title = chosen_col
    cats = list(df[chosen_col].unique())
    print(cats)
    
     # Create new sheet for each of the chosen category's value
    for cat in cats:
        cat_name = remove_chars(str(cat))
        print(cat_name)
        dfs[cat_name] = df[df[chosen_col] == cat]
     
    return dfs, split_title


def split_by_col_names(df, cols_dict):
    dfs = {}
    
    print('All columns:\n')
    print_dict(cols_dict)
    
    # Choose Columns
    num_common_cols = int(input('How many columns do you always want to keep?: '))
    cols_list = list(cols_dict.values())
    dim_cols = cols_list[:num_common_cols]
    changed_cols = cols_list[num_common_cols:]

    split_title = input('What is the splitting title?: ')
    print(changed_cols)

    for col in changed_cols:
        output_cols = dim_cols + [col]
        col_name = remove_chars(str(col))
        print(col_name)
        dfs[col_name] = df[output_cols]
        
    return dfs, split_title


def multipleSheets():    
    dir_path = input('Insert folder path: ')

    # Choose Excel
    chosen_excel = choose_file(dir_path)
    
    # Choose Sheet
    file_path = os.path.join(dir_path, chosen_excel)
    chosen_sheet = choose_sheet(file_path)
    
    #Check if needs to skip rows:
    sample_df = pd.read_excel(file_path, sheet_name=chosen_sheet)
    display(sample_df.head())

    # Skip Rows/Columns?
    y_n_skip = input('Do you want to skip rows?  [y,n] : ').strip().lower()
    skip = BOOL_DICT[y_n_skip]
    
    skip_rows = 0
    if skip:
        skip_rows = int(input('How many ROWS to skip?: '))    
    
    # Get all Sheet's Columns
    main_df = pd.read_excel(file_path, sheet_name=chosen_sheet, skiprows=skip_rows, usecols=lambda x: 'Unnamed' not in x)
    display(main_df.head())
    cols_list = list(main_df.columns)
    cols_dict = list_to_dict(cols_list)

    
    # Validate data
    if len(main_df) == 0:
        raise Exception('Data has 0 rows!')
    
        
    # Split to Sheets or Files?
    val_or_name = input('Do you want to Split by Column Value or by Column Name?  [v,n] : ').strip().lower()
    by_val = BOOL_DICT[val_or_name] # True >>> By val ; False >>> By name
    

    
    if by_val:
        
        dfs, split_title = split_by_col_vals(main_df, cols_dict)   
    
    else:
        
        dfs, split_title = split_by_col_names(main_df, cols_dict)       
    
        
    # Split by Column name or by values?
    sheet_or_file = input('Do you want to Split to different Sheets or Files?  [s,f] : ').strip().lower()
    to_sheet = BOOL_DICT[sheet_or_file] # True >>> To sheets ; False >>> To files
    
    
    if to_sheet: # Split to multiple sheets in the same file
        
        output_path = os.path.join(dir_path, f'{chosen_excel.replace(".xlsx", "")} by {split_title}.xlsx')
        writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

        for title, data in dfs.items():
            data.to_excel(writer, sheet_name=title, index=False)
            
        writer.save()
            
    else: # Split to multiple xlsx files
        
        for title, data in dfs.items():            
            output_path = os.path.join(dir_path, f'{chosen_excel.replace(".xlsx", "")} - {title}.xlsx')
            writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

            data.to_excel(writer, sheet_name=title, index=False)
            writer.save()
            writer.close()
        

    print('DONE - Export with Multiple Sheets')
    return False


def main():
    ind = True
    while ind:
        try:
            ind = multipleSheets()
        except Exception as e:
            print("#######")
            print(f"There are some errors: {e}")
            print("#######")
            


if __name__ == "__main__":
    main()
