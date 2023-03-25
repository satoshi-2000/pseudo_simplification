import os
import re

def remove_tags_and_newlines(input_dir, output_dir):
    # ディレクトリが存在しない場合は作成する
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # ディレクトリ内のファイルを順に処理する
    for filename in os.listdir(input_dir):
        # .xmlファイルでない場合はスキップ
        if not filename.endswith('.xml'):
            continue

        # ファイルを読み込む
        with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as f:
            text = f.read()

        # xmlタグと改行を除去する
        text = ''.join(line.strip() for line in text.split('\n'))
        text = re.sub(r'<[^>]+>', '', text)

        # ファイル名を変更して保存する
        new_filename = os.path.splitext(filename)[0] + '.txt'
        with open(os.path.join(output_dir, new_filename), 'w', encoding='utf-8') as f:
            f.write(text)

if __name__ == '__main__':
    input_dir = 'OT'
    output_dir = 'OT2'
    remove_tags_and_newlines(input_dir, output_dir)
