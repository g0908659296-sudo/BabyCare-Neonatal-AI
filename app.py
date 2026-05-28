import streamlit as st

# ==========================
# 頁面設定
# ==========================

st.set_page_config(
    page_title="新生兒照護小助手",
    layout="wide"
)

# ==========================
# 對話記憶
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.stApp{
    background-color:#FAF8F5;
}

.main-title{
    text-align:center;
    padding:15px;
    margin-bottom:20px;
}

.main-title h1{
    color:#5C4B51;
    font-size:40px;
    margin-bottom:5px;
}

.main-title p{
    color:#7A6A70;
    font-size:18px;
}

.left-panel{
    background:white;
    padding:20px;
    border-radius:18px;
    border:1px solid #EFE7E7;
}

.chat-box{
    background:white;
    border-radius:18px;
    padding:20px;
    min-height:600px;
    border:1px solid #EFE7E7;
}

.hot-question{
    background:#FFF7F6;
    padding:10px;
    border-radius:10px;
    margin-bottom:8px;
}

.user-msg{
    background:#EAF4FF;
    padding:12px;
    border-radius:12px;
    margin-bottom:10px;
}

.ai-msg{
    background:#FFF7F6;
    padding:12px;
    border-radius:12px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# 標題
# ==========================

st.markdown("""
<div class="main-title">
<h1>BabyCare 新生兒照護平台</h1>

<p>
嘉義基督教醫院 × 靜宜大學
<br>
提供專業且可信賴的新生兒衛教資訊查詢服務
</p>
</div>
""", unsafe_allow_html=True)
# ==========================
# 左右欄
# ==========================

left, right = st.columns([1,3])

# ==========================
# 左側
# ==========================

with left:

    st.markdown("### 參考資料")

    source1 = st.checkbox(
        "新生兒照護手冊",
        value=True
    )

    source2 = st.checkbox(
        "母乳哺育衛教資料",
        value=True
    )

    source3 = st.checkbox(
        "新生兒黃疸照護指引",
        value=True
    )

    source4 = st.checkbox(
        "疫苗接種資訊"
    )

    source5 = st.checkbox(
        "新生兒常見問題彙整"
    )

    selected_sources = []

    if source1:
        selected_sources.append("新生兒照護手冊")

    if source2:
        selected_sources.append("母乳哺育衛教資料")

    if source3:
        selected_sources.append("新生兒黃疸照護指引")

    if source4:
        selected_sources.append("疫苗接種資訊")

    if source5:
        selected_sources.append("新生兒常見問題彙整")

    st.divider()

    st.success(
        f"目前選擇 {len(selected_sources)} 份資料"
    )

# ==========================
# 右側聊天區
# ==========================

with right:

    st.markdown("### 智慧問答")

    chat_container = st.container()

    with chat_container:

        for msg in st.session_state.messages:

            if msg["role"] == "user":

                st.markdown(
                    f"""
                    <div class="user-msg">
                    <b>您：</b><br>
                    {msg["content"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="ai-msg">
                    <b>照護建議：</b><br>
                    {msg["content"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    question = st.chat_input(
        "例如：寶寶半夜一直哭怎麼辦？"
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        # =====================
        # 未來這裡接 RAG + GPT
        # =====================

        answer = f"""
目前為介面展示版本。

您詢問的是：

{question}

未來此處將由 GPT-OSS 與 RAG
根據新生兒衛教知識庫產生回答。
"""

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()

# ==========================
# 參考資料區
# ==========================

st.divider()

st.subheader("參考資料")

st.info("""
目前顯示範例資料來源

• 新生兒照護手冊 第12頁

• 母乳哺育衛教資料 第5頁

未來將由 RAG 自動顯示實際引用來源
""")

# ==========================
# 頁尾
# ==========================

st.caption(
    "本系統僅供衛教資訊查詢參考，如有緊急狀況或醫療需求，請立即洽詢醫療專業人員。"
)
