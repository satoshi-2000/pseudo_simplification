import pandas as pd
from bert_score import score

def read_csv(input_path):
    # 平易化文として変換された文対が格納されているCSVファイルを読み込む
    df = pd.read_csv(input_path, header=None,encoding='utf-8')
    return df

def calculate_bertscore(df):
    P_list = []
    R_list = []
    F1_list = []

    # 冒頭に空白を含む場合に空白を除去
    orig_sen = [str.replace(' ','') for str in df['original'].values]
    simp_sen = [str.replace(' ','') for str in df['simp_rem'].values]

    # BERTScoreを求める
    P_list,R_list,F1_list = score(orig_sen,simp_sen,lang="ja",verbose=True)

    # P,R,F1を連結させる
    # # https://note.nkmk.me/python-list-flatten/ (2022/07/14参照)
    P_flat = [x for row in P_list for x in row]
    R_flat = [x for row in R_list for x in row]
    F1_flat = [x for row in F1_list for x in row]
    
    # torch.tensorから要素を取り出す
    P_val = [tensor.item() for tensor in P_flat]
    R_val = [tensor.item() for tensor in R_flat]
    F1_val = [tensor.item() for tensor in F1_flat]

    # P,R,F1をdfに格納する
    df_bert_score = pd.DataFrame({'precision': P_val,
                             'recall' : R_val,
                             'f1-score' : F1_val})
    
    # 入出力文と結合させる
    df_concat = pd.concat([df,df_bert_score],axis=1)

    return df_concat

def save_csv(df,output_path,output_describe_path):
    # 抽出したデータをCSVファイルに保存
    df.to_csv(output_path, index=False)
    df.describe().to_csv(output_describe_path, index=False)

def main():
    # CSVファイルを読み込み、条件に従って抽出・保存
    num = 1     # 各難易度を指定
    input_path = 'generate_simp_1000_' + num +'_rem_ans.csv'
    output_path = 'generate_simp_1000_' + num +'_rem_ans_bertscore.csv'
    output_describe_path = 'generate_simp_1000_' + num +'_rem_ans_bertscore_describe.csv'
    
    df = read_csv(input_path)
    df_out = calculate_bertscore(df)
    save_csv(df_out,output_path,output_describe_path)

if __name__ == '__main__':
    main()