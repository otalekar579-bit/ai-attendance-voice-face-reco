import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="
            background: linear-gradient(145deg, rgba(31, 48, 51, 0.96), rgba(19, 30, 33, 0.96));
            border-left: 5px solid;
            border-image: linear-gradient(180deg, #f27f59, #55c6bd) 1;
            padding: 25px;
            border-radius: 20px;
            border-top: 1px solid rgba(215, 224, 223, 0.14);
            border-right: 1px solid rgba(215, 224, 223, 0.14);
            border-bottom: 1px solid rgba(215, 224, 223, 0.14);
            margin-bottom: 20px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.22);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        ">
        <h3 style="margin:0; color: #f3f7f5; font-size: 1.5rem ">{name}</h3>
        <p style="color:#9aabaa; margin:10px 0;">Code : <span style="background:rgba(85,198,189,0.14); color:#71d6ce; padding:2px 10px; border-radius:8px; font-weight:600;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: rgba(255,255,255,0.06); color:#c9d5d3; padding:6px 14px; border-radius:12px; font-size:0.9rem; font-weight:500; border: 1px solid rgba(215,224,223,0.12);">{icon} <b style="color:#f3f7f5;">{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
