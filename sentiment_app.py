import streamlit as st
import joblib as jb
import time
# streamlit run sentiment_app.py

NLP = jb.load('NLP.pkl')

st.title('MÔ HÌNH ĐÁNH GIÁ PHẢN HỒI CỦA KHÁCH HÀNG ')

st.divider()
# give info
text = st.text_area('Nhập nhận xét (Kết quả đánh giá NEG: Tệ, POS: Tốt, NEU: Trung Lập):')
st.divider()
if st.button('Click to Analyze'):
    with st.status("Analyzing......"):
                st.write("DONE!")
                time.sleep(1.5)
    if text:
        
        try:
            results = NLP(text)
            st.write(f'Đánh giá của bạn là: {results[0]['label']}')
            st.write(f'Tỷ lệ chính xác của đánh giá : {round(results[0]['score']*100, 2)}%')
        except Exception as e:
            st.error(f'Error: {e}')
    else:
        st.warning('Please enter text.')

