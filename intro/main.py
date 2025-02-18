import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done'

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')

# if button:
#     right_column.write('ここは右カラムです。')

# expander = st.expander('問合せ')
# expander.write('問い合わせ内容')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# st.write('あなたの趣味:',text)
# 'コンディション：',condition

# option = st.selectbox(
#     'あなが好きな数字を教えてください。',
#     list(range(1,11))
# )

# st.write('あなたが好きな数字は',option,'です。')

# if st.checkbox('Show Image'):
#     img = Image.open('sample.JPG')
#     st.image(img, caption = 'Sample', use_column_width =True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )

# st.map(df)
# st.dataframe(df.style.highlight_max(axis=0))#,width=100,height=100)

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """