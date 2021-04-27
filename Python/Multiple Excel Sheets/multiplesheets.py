import pandas as pd
import os
import glob

def multipleSheets():

    dir_path = input('Insert folder path: ')

    print('\nExcels in chosen folder: ')

    files_dict = {}
    i = 1
    for filename in glob.glob(os.path.join(dir_path, '*.xlsx')):
        # sliced_name = filename[(filename[::-1].find('\\'))*(-1):]
        sliced_name = filename.replace(dir_path+'\\', "")
        files_dict[i] = sliced_name
        print(i, '-', sliced_name)
        i += 1

    print()

    excel_number = int(input('Insert Excel NUMBER: '))

    print()
    chosen_excel = files_dict[excel_number]
    path = dir_path +'\\'+ chosen_excel

    print('\nSheets in chosen Excel: ')

    xl_sheets = pd.ExcelFile(path).sheet_names
    sheets_dict = {}
    for i in range(1, len(xl_sheets)+1):
        sheets_dict[i] = xl_sheets[i-1]
        print(i, "-", xl_sheets[i-1])

    sheet_number = int(input('Insert Sheet NUMBER: '))

    print()
    chosen_sheet = sheets_dict[sheet_number]

    main_df = pd.read_excel(path, sheet_name=chosen_sheet)

    print('\nColumns in chosen Excel: ')

    cols_list = list(main_df.columns)

    cols_dict = {}
    for i in range(1, len(cols_list)+1):
        cols_dict[i] = cols_list[i-1]
        print(i, "-", cols_list[i-1])


    chosen_col_num = int(input('Choose column NUMBER to group by which: '))
    chosen_col = cols_dict[chosen_col_num]
    cats = list(main_df[chosen_col].unique())
    print(cats)

    output_path = dir_path+f'/{chosen_excel.replace(".xlsx", "")} by {chosen_col}.xlsx'
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')


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
            print(f"There are some errors{e}")
            print("#######")

if __name__ == "__main__":
    main()
