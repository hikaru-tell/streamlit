import streamlit as st

# タイトル
st.title("MBTI診断ツール")

# 質問リスト
questions = [
    ("あなたは一人で過ごすことが多いですか？", "はい", "いいえ"),
    ("新しいアイデアをすぐに実行に移しますか？", "はい", "いいえ"),
    ("怒ったときは？", "怒鳴る、泣く", "理詰め"),
    ("計画を立てて行動する派？", "はい", "いいえ")
]

# 回答リスト
answers = []

# 質問を表示
for question, option1, option2 in questions:
    answers.append(st.radio(question, (option1, option2)))

# 診断結果表示ボタン
if st.button("診断結果を見る"):
    result = ""

    # 回答に基づいてMBTIタイプを簡単に決定
    if answers[0] == "はい":
        result += "I"  # 内向型
    else:
        result += "E"  # 外向型

    if answers[1] == "はい":
        result += "N"  # 直感型
    else:
        result += "S"  # 現実型

    if answers[2] == "はい":
        result += "F"  # 感情型
    else:
        result += "T"  # 思考型

    if answers[3] == "はい":
        result += "J"  # 判断型
    else:
        result += "P"  # 観察型

    # 診断結果の表示
    st.write(f"あなたのMBTIタイプは: {result}です！")
