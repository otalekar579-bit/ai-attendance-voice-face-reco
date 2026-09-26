import streamlit as st


def header_home():
    
    st.markdown("""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <div style="
                width:90px; height:90px;
                background: linear-gradient(135deg, #7C3AED, #06B6D4);
                border-radius: 24px;
                display:flex; align-items:center; justify-content:center;
                box-shadow: 0 8px 32px rgba(124,58,237,0.4);
                margin-bottom: 16px;
                font-size: 48px;
            ">🎙️</div>
            <h1 style='text-align:center; background: linear-gradient(135deg, #C4B5FD, #67E8F9); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin:0; letter-spacing: 2px;'>FaceVox</h1>
            <p style="color: #C4B5FD; font-size: 0.95rem; margin-top: 8px; letter-spacing: 3px; text-transform: uppercase;">AI-Powered Attendance</p>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():
    
    st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; gap:14px">
            <div style="
                width:55px; height:55px;
                background: linear-gradient(135deg, #7C3AED, #06B6D4);
                border-radius: 14px;
                display:flex; align-items:center; justify-content:center;
                box-shadow: 0 4px 16px rgba(124,58,237,0.3);
                font-size: 28px;
            ">🎙️</div>
            <h2 style='text-align:left; background: linear-gradient(135deg, #7C3AED, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin:0;'>FaceVox</h2>
        </div>   
                
                """, unsafe_allow_html=True)
