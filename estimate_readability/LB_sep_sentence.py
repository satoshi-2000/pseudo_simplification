import os
import pandas as pd
import re

def read_file(file_path):
    df = pd.read_csv(file_path, encoding='shift-jis')
    return df

def extract_sentence(df, dir_path):
    merged_df = pd.DataFrame(columns ={'sample_id','sentence','label'})
    
    #print(df.head())
    new_rows = []    
    for row in df.itertuples():
        #print(row)
        sample_id = row[1]
        file_path = os.path.join(dir_path, str(sample_id) + '.txt')
        
        #print(file_path)
        if not os.path.exists(file_path):            
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # 全角スペースなどを除去
        text = text.strip().replace('　', '')
        # 文単位で区切る
        sentences = text.split('。')
        
        for s in sentences:            
            # 6文字以下 or 漢字が含まれる割合が75%以上の文を除去
            if len(s) <= 6 or sum(c >= u'\u4e00' and c <= u'\u9fff' for c in s)/len(s) >= 0.75:
                continue

            new_rows.append({'sample_id': sample_id, 'sentence': s, 'label' : row[2]})

    merged_df = pd.DataFrame(new_rows)
    return merged_df
    
def save_file(df, file_path):
    df.to_csv(file_path, index=False)

def main():
    # ファイル読み込み
    df = read_file('LB_labeled.csv')
    # 分割    
    sep_df = extract_sentence(df, 'LB_ALL2/')
    # ファイル保存
    save_file(sep_df, 'LB_sep_sentence.csv')

if __name__ == '__main__':
    main()