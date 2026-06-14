import streamlit as st
import numpy as np
import plotly.graph_objects as go

def run():
    st.header("🧲 চৌম্বক ক্ষেত্র ও আহিত কণার গতিপথ (Magnetic Field & Helical Path)")
    
    st.subheader("১. গতিপথের সংজ্ঞা (Definition)")
    st.info("""
    **হেলিকাল গতিপথ:** যখন কোনো গতিশীল আধানযুক্ত কণা একটি সুষম চৌম্বক ক্ষেত্রের সাথে সমান্তরাল বা লম্ব না হয়ে যেকোনো কোণে প্রবেশ করে, তখন কণাটির গতিপথ কুন্ডলাকার বা হেলিকাল (Helical) রূপ নেয়।
    """)
    
    st.subheader("২. বিজ্ঞানী পরিচিতি (About the Scientist)")
    st.write("""
    ওলন্দাজ পদার্থবিদ হেন্ড্রিক লরেন্টজ (Hendrik Lorentz) চৌম্বক ক্ষেত্রের এই বলের সমীকরণটি আবিষ্কার করেন, যাকে 'লরেন্টজ বল' বলা হয়।
    """)
    
    st.subheader("৩. গাণিতিক প্রমাণ (Mathematical Derivation)")
    st.write("হেলিক্সের ব্যাসার্ধ ($r$) এবং অক্ষ বরাবর অতিক্রান্ত দূরত্ব বা পিচ ($p$) এর সমীকরণ:")
    st.latex(r"r = \frac{m \cdot v \sin\theta}{q \cdot B}")
    st.latex(r"p = \frac{2\pi \cdot m \cdot v \cos\theta}{q \cdot B}")
    
    st.subheader("৪. গাণিতিক উদাহরণ (Solved Examples)")
    st.markdown("""
    **उदाहरण ১:** চৌম্বক ক্ষেত্রে আধানের বেগ দ্বিগুণ করা হলে ব্যাসার্ধের কী পরিবর্তন হবে?  
    * **সমাধান:** সূত্র অনুযায়ী $r \propto v$, তাই ব্যাসার্ধও **দ্বিগুণ** হবে।
    """)
    
    st.divider()
    
    st.subheader("৫. স্লাইডার যুক্ত গ্রাফ পর্যবেক্ষণ (2D & 3D Graphs)")
    st.write("### ৫.১ ২ডি লেখচিত্র (2D Pitch vs Velocity)")
    v_range = np.linspace(1, 10, 100)
    selected_factor = st.slider("ভর ও আধানের অনুপাত পরিবর্তন করো:", 0.5, 3.0, 1.0, key="mag_2d_slider")
    pitch_range = v_range * selected_factor
    fig_mag_2d = go.Figure()
    fig_mag_2d.add_trace(go.Scatter(x=v_range, y=pitch_range, mode='lines', line=dict(color='cyan', width=4)))
    fig_mag_2d.update_layout(xaxis_title="কণার বেগ (Velocity, v)", yaxis_title="হেলিক্সের পিচ (Pitch, p)")
    st.plotly_chart(fig_mag_2d, use_container_width=True)
    
    st.write("### ৫.২ ৩ডি অ্যানিমেশন ও সিমুলেশন (3D Interactive Helix Graph)")
    radius = st.slider("হেলিক্সের ব্যাসার্ধ পরিবর্তন করো (Radius, r):", 1.0, 5.0, 2.0, key="mag_r")
    pitch = st.slider("হেলিক্সের পিচ পরিবর্তন করো (Pitch, p):", 1.0, 5.0, 2.0, key="mag_p")
    
    t = np.linspace(0, 20, 500)
    fig_mag_3d = go.Figure(data=[go.Scatter3d(x=radius*np.cos(t), y=radius*np.sin(t), z=pitch*t, mode='lines', line=dict(color=pitch*t, colorscale='Rainbow', width=6))])
    fig_mag_3d.update_layout(scene=dict(xaxis_title="X Axis", yaxis_title="Y Axis", zaxis_title="Z Axis"), margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig_mag_3d, use_container_width=True)
    
    st.divider()
    
    st.subheader("৬. কুইজ (MCQ)")
    questions_mag = [
        {"q": "১. চৌম্বক ক্ষেত্রে গতিশীল আধানের উপর প্রযুক্ত বলকে কী বলা হয়?", "o": ["কুলম্ব বল", "লরেন্টজ বল", "নিউটনীয় বল", "নিউক্লীয় বল"], "a": "লরেন্টজ বল"}
    ]
    score_mag = 0
    for i, q in enumerate(questions_mag):
        st.write(f"**{q['q']}**")
        user_ans = st.radio("উত্তর বেছে নাও:", q['o'], key=f"q_mag_{i}", index=None)
        if user_ans == q['a']: score_mag += 1
    if st.button("চৌম্বক ক্ষেত্রের ফাইনাল স্কোর দেখাও"): st.metric("তোমার মোট স্কোর", f"{score_mag} / 1")
