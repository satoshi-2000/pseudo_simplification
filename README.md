# 概要
本リポジトリは、筆者の平易化に関する研究内容と実験プログラムをまとめたものです。
本来はpythonのenvでやった方が良いとは思いますが、実験時点ではanacondaで実行していたため、その環境で実行するためのコードを記述しておきます。


# pkg_version
package.txtは、本プログラム群の動作環境確認用のpip listの出力結果を示しています。


# snow_preprocessing
snow_file_splitter.pyは、やさしい日本語の文対のみを抽出し、訓練:開発:評価=8:1:1になるように分割した上で、訓練データをtransformersのfine-tuningに用いるためのdatasetsの形に整形したプログラムです。

SNOW T15及びSNOW T23については、[言語商会のサイト](https://www.jnlp.org/GengoHouse/snow/t15]) からダウンロードして作業用ディレクトリに保存してください。

## package install
[rinna/japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium)をfine-tuningするために、次のパッケージをインストールする必要があります(Requirements already satisfiedになる場合もあります)。
```bash
pip install transformers
pip install datasets
pip install SentencePiece
```

## fine-tuning
次のような形でGPT-2モデルのfine-tuningを実行します。ここで、バッチサイズには適当な数値を設定してください。

```bash
python ./transformers/examples/pytorch/language-modeling/run_clm.py --model_name_or_path=rinna/japanese-gpt2-medium  --train_file=snow_datasets/dataset.txt      --validation_file=snow_datasets/dataset.txt      --do_train  --do_eval --num_train_epochs=10  --save_steps=10000 --per_device_eval_batch_size=1  --output_dir=output/  --use_fast_tokenizer=False --per_device_train_batch_size=1
```

ただし、元のAutoTokenizerでは上手く読み込めないため、[/transformers/examples/pytorch/language-modeling/run_clm.py](https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_clm.py)の54行目及び340-347行目を次のように変更します。

```python
from transformers import T5Tokenizer
```

```python
    if model_args.tokenizer_name:
        #tokenizer = AutoTokenizer.from_pretrained(model_args.tokenizer_name, **tokenizer_kwargs)
        tokenizer = T5Tokenizer.from_pretrained(model_args.tokenizer_name, **tokenizer_kwargs)
    elif model_args.model_name_or_path:
        tokenizer = T5Tokenizer.from_pretrained(model_args.model_name_or_path, **tokenizer_kwargs)
        #tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path, **tokenizer_kwargs)
    else:
        raise ValueError(
```

また、GPUサーバーの使用状況によっては希望のGPUが利用できない可能性があるため、次のようなコードで適宜使用するGPUの番号を指定してみてください。
```bash
export CUDA_VISIBLE_DEVICES=0,1,2
```

## 平易文生成例
generate_example.pyを用いて平易化文の生成を行うと、次のような文が生成されます。
2文目が平易化文になっており、やや平易な言い換えを行っています。一方で、「獅子奮迅」と「勇気ある行動」で、やや意味が異なっているように、平易化前後で十分な同義性が確保出来ない場合がある、という問題があります。

```bash
今回の成果は偏に彼の獅子奮迅の働きの賜物でしょう。 彼の勇気ある行動は我々に大きな助けになったことでしょう。
```


# estimate_readability
OT_remove_tags.pyは、[BCCWJ](https://clrd.ninjal.ac.jp/bccwj/doc.html)に含まれている教科書コーパス(OT)に対してxmlタグと改行を除去し、.txt形式で保存するプログラムです。

OT_labeling.pyは、教科書コーパスに対して、小学校低学年 : 0、中学年 : 1、高学年 : 2、中学生 : 3、高校生 : 4としてラベリングを行うプログラムです。

OT_sep_sentence.pyは、ラベリングされた教科書コーパスに対して、文単位(。区切り)に分割します。その後、ノイズとなる6文字以下や漢字が含まれる割合が75%以上の文を除去します。

# Reference
[1] 郷原聖士, 綱川隆司, 西田昌史, 西村雅史. BERT によ
る日本語文章の難易度推定. 第 21 回情報科学技術
フォーラム, 2022

[2] 郷原聖士, 綱川隆司, 西田昌史, 西村雅史. 疑似データを用いた GPT-2 による日本語文章の多段階平易化. 言語処理学会 第29回年次大会 発表論文集. 2023
