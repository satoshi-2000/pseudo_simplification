import torch
from transformers import T5Tokenizer, AutoModelForCausalLM

def generate_text(prompt):
    # モデルとトークナイザーの読み込み
    tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
    model = AutoModelForCausalLM.from_pretrained("output/")

    # GPU
    if torch.cuda.is_available():
        model = model.to("cuda")

    # テキスト生成のパラメーターの設定
    length = 100  # 生成するテキストの長さ
    temperature = 1.0  # テキスト生成の多様性の度合い

    # トークナイズされた入力文をモデルに渡してテキスト生成
    token_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    with torch.no_grad():
        output = model.generate(
            token_ids.to(model.device),
            max_length=50,
            min_length=30,
            do_sample=True,
            top_k=500,
            top_p=0.95,
            pad_token_id=tokenizer.pad_token_id,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            bad_word_ids=[[tokenizer.unk_token_id]]
        )

    # 生成されたテキストをデコードして返す
    return tokenizer.decode(output[0], skip_special_tokens=True)


def main():
    prompt = "今回の成果は偏に彼の獅子奮迅の働きの賜物でしょう。[SEP]"
    generated_text = generate_text(prompt)
    print(generated_text)


if __name__ == "__main__":
    main()
