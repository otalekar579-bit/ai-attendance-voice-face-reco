import streamlit as st


def footer_home():
    
    st.markdown("""
        <div style="margin-top:2.5rem; display:flex; gap:6px; justify-content:center; align-items:center; flex-direction:column;">
        <p style="font-weight:500; color:rgba(255,255,255,0.7); font-size:0.85rem; margin:0;">Created with ❤️ by</p>
        <p style="font-weight:700; color:white; font-size:1.1rem; margin:0; background: linear-gradient(135deg, #C4B5FD, #67E8F9); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Omkar</p>
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    
    st.markdown("""
        <div style="margin-top:2.5rem; display:flex; gap:6px; justify-content:center; align-items:center; flex-direction:column;">
        <p style="font-weight:500; color:rgba(255,255,255,0.45); font-size:0.85rem; margin:0;">Created with ❤️ by</p>
        <p style="font-weight:700; font-size:1.05rem; margin:0; background: linear-gradient(135deg, #7C3AED, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Omkar</p>
        </div>
                
                """, unsafe_allow_html=True)
