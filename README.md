# 概要
本リポジトリは、筆者の平易化に関する研究内容と実験プログラムをまとめたものです。


# pkg_version
package.txtは、本プログラム群の動作環境確認用のpip listの出力結果を示しています。


# snow_preprocessing
snow_file_splitter.pyは、やさしい日本語の文対のみを抽出し、訓練:開発:評価=8:1:1になるように分割した上で、訓練データをtransformersのfine-tuningに用いるためのdatasetsの形に整形したプログラムです。

SNOW T15及びSNOW T23については、[言語商会のサイト](https://www.jnlp.org/GengoHouse/snow/t15]) からダウンロードして作業用ディレクトリに保存してください。

'''bash
python ./transformers/examples/pytorch/language-modeling/run_clm.py --model_name_or_path=rinna/japanese-gpt2-medium  --train_file=dataset/dataset3.txt      --validation_file=dataset/dataset3.txt      --do_train  --do_eval --num_train_epochs=10  --save_steps=10000 --per_device_eval_batch_size=1  --output_dir=output/  --use_fast_tokenizer=False --per_device_train_batch_size=1
