import streamlit as st
import numpy as np
import plotly.graph_objects as go

def run():
    st.header("🔌 ওহমের সূত্র (Ohm's Law)")
    
    st.subheader("১. সূত্রের সংজ্ঞা (Definition)")
    st.info("""
    **সূত্র:** উষ্ণতা ও অন্যান্য ভৌত অবস্থা অপরিবর্তিত থাকলে, কোনো পরিবাহীর মধ্য দিয়ে তড়িৎপ্রবাহমাত্রা ওই পরিবাহীর দুই প্রান্তের বিভবপ্রভেদের সমানুপাতিক হয়।
    """)
    
    st.subheader("২. বিজ্ঞানী পরিচিতি (About the Scientist)")
    st.write("""
    জার্মান পদার্থবিদ जॉर्ज साइमन ओहम (Georg Simon Ohm) ১৮২৭ সালে এই সূত্রটি আবিষ্কার করেন। তাঁর নামানুসারেই রোধের একককে 'ওহম' বলা হয়।
    """)
    
    st.subheader("৩. গাণিতিক প্রমাণ (Mathematical Derivation)")
    st.write("পরিবাহীর দুই প্রান্তের বিভবপ্রভেদ $V$ এবং প্রবাহমাত্রা $I$ হলে, ওহমের সূত্রানুযায়ী:")
    st.latex(r"V \propto I")
    st.latex(r"V = R \cdot I")
    st.write("এখানে $R$ একটি ধ্রুবক, যাকে পরিবাহীর **রোধ (Resistance)** বলা হয়।")
    
    st.subheader("৪. গাণিতিক উদাহরণ (Solved Examples)")
    st.markdown("""
    **उदाहरण ১:** রোধ 5 Ω এবং বিভবপ্রভেদ 10 V হলে, প্রবাহমাত্রা কত?  
    * **সমাধান:** $I = \frac{V}{R} = \frac{10}{5} = 2\text{ A}$
    """)
    
    st.divider()
    
    st.subheader("৫. স্লাইডার যুক্ত গ্রাফ পর্যবেক্ষণ (2D & 3D Graphs)")
    st.write("### ৫.১ ২ডি ওহমিক লেখচিত্র (2D V-I Graph)")
    selected_R = st.slider("পরিবাহীর রোধ পরিবর্তন করো (Resistance, R):", 1, 20, 5, key="normal_2d_r")
    current_range = np.linspace(0, 10, 100)
    voltage_range = current_range * selected_R
    fig_2d = go.Figure()
    fig_2d.add_trace(go.Scatter(x=current_range, y=voltage_range, mode='lines', line=dict(color='orange', width=4)))
    fig_2d.update_layout(xaxis_title="তড়িৎপ্রবাহমাত্রা (Current, I)", yaxis_title="বিভবপ্রভেদ (Voltage, V)")
    st.plotly_chart(fig_2d, use_container_width=True)
    
    st.write("### ৫.২ ৩ডি ইন্টারেক্টিভ ল্যাব (3D Simulation Graph)")
    max_R = st.slider("সর্বোচ্চ রোধ নির্ধারণ করো (Max Resistance, R)", 5, 20, 10, key="ohm_r")
    max_I = st.slider("সর্বোচ্চ প্রবাহমাত্রা নির্ধারণ করো (Max Current, I)", 5, 20, 10, key="ohm_i")
    R_val, I_val = np.meshgrid(np.linspace(0, max_R, 20), np.linspace(0, max_I, 20))
    V_val = I_val * R_val
    fig_3d = go.Figure(data=[go.Surface(x=R_val, y=I_val, z=V_val, colorscale='Viridis')])
    fig_3d.update_layout(scene=dict(xaxis_title="Resistance (R)", yaxis_title="Current (I)", zaxis_title="Voltage (V)"))
    st.plotly_chart(fig_3d, use_container_width=True)
    
    st.divider()
    
    st.subheader("৬. কুইজ (MCQ)")
    questions_ohm = [
        {"q": "১. ওহমের সূত্রে কোন ভৌত রাশিটি ধ্রুবক থাকে?", "o": ["বিভবপ্রভেদ", "তড়িৎপ্রবাহ", "উষ্ণতা", "রোধ"], "a": "উষ্ণতা"},
        {"q": "২. রোধের এস.আই (SI) একক কী?", "o": ["ভোল্ট", "ওহম", "অ্যাম্পিয়াৰ", "ওয়াট"], "a": "ওহম"}
    ]
    score_ohm = 0
    for i, q in enumerate(questions_ohm):
        st.write(f"**{q['q']}**")
        user_ans = st.radio("উত্তর বেছে নাও:", q['o'], key=f"q_ohm_{i}", index=None)
        if user_ans == q['a']: score_ohm += 1
    if st.button("ওহমের সূত্রের ফাইনাল স্কোর দেখাও"): st.metric("তোমার মোট স্কোর", f"{score_ohm} / 2")
