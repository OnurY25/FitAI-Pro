import streamlit as st
import requests

# Sayfa Yapılandırması
st.set_page_config(page_title="FitAI Global Pro", page_icon="⚡", layout="centered")

# Görsel Tasarımı Düzelten Bölüm (Hata Buradaydı)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True) # <-- Burası 'unsafe_allow_html' olmalı

st.title("⚡ FitAI Professional Coach")
st.write("Get your elite 7-day transformation plan instantly.")

# Sol Panel: Satın Al ve Bilgi
with st.sidebar:
    st.header("Premium Access")
    # LEMON SQUEEZY LİNKİNİ BURAYA YAPIŞTIR
    st.link_button("🚀 Unlock Full Access ($19)", "https://onur.lemonsqueezy.com/...", type="primary")
    st.divider()
    st.info("Your data is processed by Gemini 1.5 AI.")

# Ana Form
with st.container():
    name = st.text_input("Client Full Name", placeholder="Alex Johnson")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", 40, 150, 75)
    with col2:
        goal = st.selectbox("Transformation Goal", ["Fat Loss", "Muscle Gain", "Lean Bulk"])

    if st.button("Generate My Professional Plan"):
        if name:
            # WEBHOOK URL'Nİ BURAYA YAPIŞTIR (TIRNAK İÇİNDE!)
            WEBHOOK_URL = "https://sciatic-jacinta-nonsecretionary.ngrok-free.dev/webhook-test/5bcfa3a5-3435-4120-bf18-ad2c6636b8eb"
            
            payload = {"name": name, "weight": weight, "goal": goal}
            
            with st.spinner("AI is architecting your plan..."):
                try:
                    r = requests.post(WEBHOOK_URL, json=payload)
                    if r.status_code == 200:
                        st.balloons()
                        st.success(f"Done! Here is your custom plan, {name}:")
                        st.markdown(r.text) 
                    else:
                        st.error("AI Server unreachable. Check n8n.")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
        else:
            st.warning("Please enter a name.")

st.divider()

st.caption("© 2026 FitAI Global SaaS - Professional Edition")





