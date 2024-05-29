import streamlit as st
import pickle
from streamlit_option_menu import option_menu

def load_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Tải mô hình trực tiếp từ file
model = load_model("model.pkl")

# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of patients with cognitive impairment (EEG data for multiple sclerosis)',
                           ['Disease Prediction'],
                           icons=['activity'], default_index=0)

if selected == 'Disease Prediction':
    st.title("Disease Prediction using XGBoost model")
    st.header("Vui lòng nhập thông tin cho 19 kênh, mỗi kênh có 5 feature")

    # List để lưu trữ các giá trị nhập vào
    input_data = []

    # Tạo form nhập liệu
    with st.form(key='prediction_form'):
        for i in range(19):
            st.subheader(f"Kênh {i+1}")
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                center_frequency = st.number_input(f"Center Frequency (Kênh {i+1})", key=f"cf_{i+1}")
                input_data.append(center_frequency)
            with col2:
                power = st.number_input(f"Power (Kênh {i+1})", key=f"power_{i+1}")
                input_data.append(power)
            with col3:
                bandwidth = st.number_input(f"Bandwidth (Kênh {i+1})", key=f"bw_{i+1}")
                #input_data.append(bandwidth)
            with col4:
                offset = st.number_input(f"Offset (Kênh {i+1})", key=f"offset_{i+1}")
                input_data.append(offset)
            with col5:
                exponent = st.number_input(f"Exponent (Kênh {i+1})", key=f"exp_{i+1}")
                input_data.append(exponent)

        # Nút dự đoán
        submit_button = st.form_submit_button(label='Dự đoán')

    # Prediction
    if submit_button:
        prediction = model.predict([input_data])
        if prediction[0] == 1:
            predicts = 'This person has cognitive impairment'
        else:
            predicts = 'This person does not have cognitive impairment'
        st.success(predicts)
