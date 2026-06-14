import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ওয়েবসাইটের পেজ ডিজাইন
st.set_page_config(page_title="SimuLab - Virtual Physics", layout="wide")
st.title("⚛️ SimuLab: Interactive Physics")

# ওয়েবসাইটের সাইডবার (Control Panel)
st.sidebar.title("🎛️ Control Panel")
experiment = st.sidebar.selectbox("Select Experiment:", ["Magnetic Field (Helix)", "Ohm's Law"])

# এক্সপেরিমেন্ট ১: চৌম্বক ক্ষেত্র
if experiment == "Magnetic Field (Helix)":
    st.header("Magnetic Field Simulation")
    st.markdown("চৌম্বক ক্ষেত্রে একটি আহিত কণার থ্রিডি গতিপথ (হেলিক্স)। নিচের স্লাইডার দিয়ে মান পরিবর্তন করো।")
    
    radius = st.sidebar.slider("Radius (r):", 1.0, 5.0, 2.0)
    pitch = st.sidebar.slider("Pitch (p):", 1.0, 5.0, 2.0)
    
    t = np.linspace(0, 20, 500)
    fig = go.Figure(data=[go.Scatter3d(x=radius*np.cos(t), y=radius*np.sin(t), z=pitch*t, mode='lines', line=dict(color=pitch*t, colorscale='Rainbow', width=6))])
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig, use_container_width=True)

# এক্সপেরিমেন্ট ২: ওহমের সূত্র
elif experiment == "Ohm's Law":
    st.header("Ohm's Law (V = IR) 3D Plane")
    st.markdown("ভোল্টেজ, কারেন্ট এবং রোধের মধ্যকার সম্পর্কের থ্রিডি সমতল।")
    
    max_R = st.sidebar.slider("Max Resistance (R)", 5, 20, 10)
    max_I = st.sidebar.slider("Max Current (I)", 5, 20, 10)
    
    R_val, I_val = np.meshgrid(np.linspace(0, max_R, 20), np.linspace(0, max_I, 20))
    V_val = I_val * R_val
    fig = go.Figure(data=[go.Surface(x=R_val, y=I_val, z=V_val, colorscale='Viridis')])
    fig.update_layout(scene=dict(xaxis_title="Resistance (R)", yaxis_title="Current (I)", zaxis_title="Voltage (V)"), margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig, use_container_width=True)
  
