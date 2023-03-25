import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    # 2つのExcelファイルを連結してデータフレームを作成する
    df = concatenate_excel_files('T15.xlsx', 'T23.xlsx')

    # データをtrain、dev、testに分割する
    df_train, df_dev, df_test = split_dataframe(df)
    
    # データ抽出
    train = df_train.iloc[:, 1:3]
    dev = df_dev.iloc[:, 1:3]
    test = df_test.iloc[:, 1:3]

    # 分割したデータをそれぞれファイルに保存する
    train.to_excel('snow_datasets/train.xlsx', index=False)
    dev.to_excel('snow_datasets/dev.xlsx', index=False)
    test.to_excel('snow_datasets/test.xlsx', index=False)
    
    # 訓練データについて、[SEP}トークンで分割して保存する
    sep_txt_file(train, 'snow_datasets/snow_dataset.txt')

def concatenate_excel_files(file1, file2):
    # 2つのExcelファイルを読み込む
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # 2つのデータフレームを連結する
    df = pd.concat([df1, df2], ignore_index=True)

    return df

def sep_txt_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for row in data.itertuples():
            f.write(f'{row[1]} [SEP] {row[2]}\n')

def split_dataframe(df):
    # データをtrain、dev、testに分割する
    train_dev, test = train_test_split(df, test_size=0.1, random_state=42)
    train, dev = train_test_split(train_dev, test_size=0.111, random_state=42)

    return train, dev, test

if __name__ == '__main__':
    main()

    