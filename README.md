# 概要
本リポジトリは、筆者の平易化に関する研究内容と実験プログラムをまとめたものです。


# pkg_version
package.txtは、本プログラム群の動作環境確認用のpip listの出力結果を示しています。


# snow_preprocessing
snow_file_splitter.pyは、やさしい日本語の文対のみを抽出し、訓練:開発:評価=8:1:1になるように分割した上で、訓練データをtransformersのfine-tuningに用いるためのdatasetsの形に整形したプログラムです。

SNOW T15及びSNOW T23については、[言語商会のサイト](https://www.jnlp.org/GengoHouse/snow/t15]) からダウンロードして作業用ディレクトリに保存してください。

