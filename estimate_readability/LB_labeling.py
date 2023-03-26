import pandas as pd

def read_csv(input_path):
    # CSVファイルを読み込み、特徴量を指定してDataFrameを作成
    names = ['number','sample_id', 'ndc', 'c_code', 'sur_feature1', 'sur_feature2', 'sur_feature3', 'sur_feature4', 'con_feature1', 'con_feature2', 'con_feature3', 'con_feature4', 'con_feature5', 'con_feature6', 'con_feature7', 'speciality', 'objectivity', 'hardness', 'softness', 'narrativity']
    df = pd.read_csv(input_path, names=names, header=None,encoding='shift-jis')
    return df

def extract_rows(df):
    # NaNを含む行を除外
    df = df.dropna(subset=['speciality'])
    # "speciality"列に2が含まれる行を抽出
    df = df[df['speciality'].astype(str).str.contains('2')]
    # 必要な列のみを抽出
    df = df[['number']]    
    df['label'] = 5
    return df

def save_csv(df,output_path):
    # 抽出したデータをCSVファイルに保存
    df.to_csv(output_path, index=False)

def main():
    # CSVファイルを読み込み、条件に従って抽出・保存
    input_path = 'LB_all.csv'
    output_path = 'LB_labeled.csv'
    df = read_csv(input_path)
    df = extract_rows(df)
    save_csv(df,output_path)

if __name__ == '__main__':
    main()
