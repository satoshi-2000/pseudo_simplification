import os
import pandas as pd
import re

def read_file(file_path):
    df = pd.read_csv(file_path, sep='\t',encoding='utf-8')
    return df

def extract_sentence(df, dir_path):
    merged_df = pd.DataFrame(columns ={'sample_id','sentence','label'})
    
    new_rows = []    
    for row in df.itertuples():
        sample_id = row[1]
        file_path = os.path.join(dir_path, str(sample_id) + '.txt')
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

            new_rows.append({'sample_id': sample_id, 'sentence': s, 'label' : row[5]})

    merged_df = pd.DataFrame(new_rows)
    return merged_df
    
def save_file(df, file_path):
    df.to_csv(file_path, index=False)

def main():
    # ファイル読み込み
    df = read_file('OT_labeled.txt')
    # 分割    
    sep_df = extract_sentence(df, 'OT4/')
    # ファイル保存
    save_file(sep_df, 'OT_sep_sentence.csv')

if __name__ == '__main__':
    main()
