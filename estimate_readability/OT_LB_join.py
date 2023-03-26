import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    # ファイル読み込み
    LB_df = pd.read_csv("LB_sep_sentence.csv")
    OT_df = pd.read_csv("OT_sep_sentence.csv")
        
    # データの結合
    merged_df = pd.concat([LB_df, OT_df], axis=0)
    
    return merged_df

def shuffle_and_split_data(data_df, test_size=0.1, random_state=42):
    # データのシャッフルと分割
    train_dev, test = train_test_split(data_df, test_size=test_size, random_state=random_state)
    train, dev = train_test_split(train_dev, test_size=1/9, random_state=random_state)

    return train, dev, test

def main():
    # データの読み込みと結合
    merged_df = load_data()

    # データのシャッフルと分割
    train, dev, test = shuffle_and_split_data(merged_df)

    # 分割したデータを保存
    train.to_csv("OT_LB_join_datasets/train.csv", index=False)
    dev.to_csv("OT_LB_join_datasets/dev.csv", index=False)
    test.to_csv("OT_LB_join_datasets/test.csv", index=False)

if __name__ == "__main__":
    main()
