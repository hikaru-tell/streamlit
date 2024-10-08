import streamlit as st

st.title('hello')
st.header('見出し1')
st.subheader('見出し2')
st.write('これは文字列')
st.write(12345)
text = st.text_input('名前を入力してください:')
st.write(f'こんにちは、{text}さん！')
if st.checkbox('表示しますか？'):
    st.write('なにもないよ')
option = st.selectbox(
    '何にする？', 
    ('ごはん', 'お風呂', '私')
)
if option == "私":
    st.write(f'あなたは {option} を選びました！お楽しみください。')
else:
    st.error("私にしなさい")
gakka = st.radio("学科を選択してください",('物理','化学','数学'))
if gakka != '化学':
    st.warning("センスないわ")
else:
    st.write("素晴らしい")
btn = st.button('自爆', type="primary")
if btn:
    st.write('自爆スイッチが押されました')
