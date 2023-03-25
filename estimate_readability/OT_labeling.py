import pandas as pd

def read_file(file_path):
    # ファイル読み込み
    df = pd.read_csv(file_path, sep='\t', header=1)
    # カラム名を指定
    df.columns = ['sample_id', 'bibliographic_id', 'title', 'subtitle', 'volume', 'author', 'publisher', 'publication_year', 'isbn', 'sampling_page', 'genre1', 'genre2', 'genre3', 'genre4', 'author_id', 'person_id', 'person_name', 'birth_year', 'gender', 'corpus_name']
    # OTの行のみを抽出
    ot_df = df[df['corpus_name'] == 'OT']
    return ot_df

def labeling(ot_df):
    # 学年ラベルの付与
    ot_df['label'] = ot_df.apply(lambda row: 0 if row['genre2'] == '小' and (row['genre3'] == '1' or row['genre3'] == '2') else \
                                          1 if row['genre2'] == '小' and (row['genre3'] == '3' or row['genre3'] == '4') else \
                                          2 if row['genre2'] == '小' and (row['genre3'] == '5' or row['genre3'] == '6') else \
                                          3 if row['genre2'] == '中' else \
                                          4 if row['genre2'] == '高' else \
                                          None, axis=1)
    return ot_df

def save_file(df, file_path):
    # ファイル出力
    df.to_csv(file_path, sep='\t', index=False)

def main():
    # ファイル読み込み
    ot_df = read_file('Joined_info.txt')
    # ラベル付与
    labeled_df = labeling(ot_df)
    
    #必要なカラムのみを残す
    save_df = labeled_df.loc[:,['sample_id','title','genre2','genre3','label']]
    # ファイル保存
    save_file(save_df, 'OT_labeled.txt')

if __name__ == '__main__':
    main()
