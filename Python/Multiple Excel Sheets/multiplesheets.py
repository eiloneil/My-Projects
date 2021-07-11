import pandas as pd
import os
import glob


def list_to_dict(lst):
    new_dict = {}
    for i in range(len(lst)):
        new_dict[i+1] = lst[i]

    return new_dict


def print_dict(dict):
    for key in dict.keys():
        print(key, '-', dict[key])


def multipleSheets():

    dir_path = input('Insert folder path: ')

    print('\nExcels in chosen folder: ')
    # Get all Excel Files
    filenames_lst = [filename.replace(dir_path+'\\', "") for filename in glob.glob(os.path.join(dir_path, '*.xlsx'))]
    filenames_dict = list_to_dict(filenames_lst)
    print_dict(filenames_dict)
    print()
    # Choose Excel
    excel_number = int(input('Insert Excel NUMBER: '))
    print()
    chosen_excel = filenames_dict[excel_number]

    # Get all Excel Sheets
    path = dir_path +'\\'+ chosen_excel
    print('\nSheets in chosen Excel: ')
    xl_sheets = pd.ExcelFile(path).sheet_names
    sheets_dict = list_to_dict(xl_sheets)
    print_dict(sheets_dict)
    # Choose Sheet
    sheet_number = int(input('Insert Sheet NUMBER: '))
    print()
    chosen_sheet = sheets_dict[sheet_number]
    
    # Get all Sheet's Columns
    main_df = pd.read_excel(path, sheet_name=chosen_sheet)
    print('\nColumns in chosen Excel: ')
    cols_list = list(main_df.columns)
    cols_dict = list_to_dict(cols_list)
    print_dict(cols_dict)
    # Choose Column
    chosen_col_num = int(input('Choose column NUMBER to group by which: '))
    chosen_col = cols_dict[chosen_col_num]
    cats = list(main_df[chosen_col].unique())
    print(cats)

    output_path = dir_path+f'/{chosen_excel.replace(".xlsx", "")} by {chosen_col}.xlsx'
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

    # Create new sheet for each of the chosen category's value
    for cat in cats:
        main_df[main_df[chosen_col] == cat].to_excel(writer, sheet_name=str(cat).replace('/', '').replace('\\', ''), index=False)

    writer.save()

    print('DONE - Export with Multiple Sheets')
    return False

def main():
    ind = True
    while ind:
        try:
            ind = multipleSheets()
        except Exception as e:
            print("#######")
            print(f"There are some errors {e}")
            print("#######")


if __name__ == "__main__":
    main()
