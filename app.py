import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ওয়েবসাইটের পেজ কনফিগারেশন
st.set_page_config(page_title="SimuLab - Virtual Physics", layout="wide")
st.title("⚛️ SimuLab: Interactive Physics Laboratory")

# সাইডবার মেনু
st.sidebar.title("🎛️ Control Panel")
experiment = st.sidebar.selectbox("Select Chapter:", ["Ohm's Law", "Magnetic Field (Helix)"])

# এক্সপেরিমেন্ট ১: ওহমের সূত্র
if experiment == "Ohm's Law":
    st.header("🔌 ওহমের সূত্র (Ohm's Law)")
    
    # ১. সূত্রের সংজ্ঞা
    st.subheader("১. সূত্রের সংজ্ঞা (Definition)")
    st.info("""
    **সূত্র:** উষ্ণতা ও অন্যান্য ভৌত অবস্থা (যেমন পরিবাহীর উপাদান, দৈর্ঘ্য, প্রস্থচ্ছেদ ইত্যাদি) অপরিবর্তিত থাকলে, 
    কোনো পরিবাহীর মধ্য দিয়ে তড়িৎপ্রবাহমাত্রা ওই পরিবাহীর দুই প্রান্তের বিভবপ্রভেদের সমানুপাতিক হয়।
    """)
    
    # ২. বিজ্ঞানী সম্বন্ধে
    st.subheader("২. বিজ্ঞানী পরিচিতি (About the Scientist)")
    st.write("""
    জার্মান পদার্থবিদ **জর্জ সাইমন ওহম (Georg Simon Ohm)** ১৮২৭ সালে পরিবাহীর দুই প্রান্তের বিভবপ্রভেদ এবং 
    তার মধ্য দিয়ে প্রবাহিত তড়িৎপ্রবাহের সম্পর্কের এই সূত্রটি আবিষ্কার করেন। তাঁর নামানুসারেই রোধের এস.আই (SI) একককে 'ওহম' বলা হয়।
    """)
    
    # ৩. গাণিতিক প্রমাণ
    st.subheader("৩. গাণিতিক প্রমাণ (Mathematical Derivation)")
    st.write("ধরা যাক, একটি পরিবাহীর দুই প্রান্তের বিভব যথাক্রমে $V_A$ এবং $V_B$ ($V_A > V_B$)। পরিবাহীর দুই প্রান্তের বিভবপ্রভেদ ($V$) হবে:")
    st.latex(r"V = V_A - V_B")
    st.write("পরিবাহীর মধ্য দিয়ে প্রবাহমাত্রা $I$ হলে, ওহমের সূত্রানুযায়ী:")
    st.latex(r"V \propto I \quad \text{(উষ্ণতা ও অন্যান্য ভৌত অবস্থা ধ্রুবক থাকলে)}")
    st.write("সমানুপাতিক চিহ্ন তুলে দিলে একটি ধ্রুবক ($R$) আসে:")
    st.latex(r"V = R \cdot I")
    st.write("এখানে $R$-কে ওই পরিবাহীর **রোধ (Resistance)** বলা হয়।")
    
    # ৪. গাণিতিক উদাহরণ
    st.subheader("৪. গাণিতিক উদাহরণ (Solved Examples)")
    st.markdown("""
    **উদাহরণ ১:** একটি পরিবাহীর রোধ 5 Ω এবং পরিবাহীর দুই প্রান্তের বিভবপ্রভেদ 10 V হলে, প্রবাহমাত্রা কত?  
    * **সমাধান:** সূত্র অনুযায়ী, $V = IR \implies I = \frac{V}{R}$  
    * এখানে, $V = 10\text{ V}$, $R = 5\ \Omega$  
    * অতএব, $I = \frac{10}{5} = 2\text{ A}$ (অ্যাম্পিয়ার)।
    
    **উদাহরণ ২:** কোনো পরিবাহীর মধ্য দিয়ে 3 A তড়িৎ প্রবাহিত হচ্ছে এবং পরিবাহীর রোধ 4 Ω হলে বিভবপ্রভেদ কত?  
    * **সমাধান:** $V = IR$  
    * এখানে, $I = 3\text{ A}$, $R = 4\ \Omega$  
    * অতএব, $V = 3 \times 4 = 12\text{ V}$ (ভোল্ট)।
    """)
    
    st.divider()
    
    # ৫. টুডি এবং থ্রিডি গ্রাফ
    st.subheader("৫. স্লাইডার যুক্ত গ্রাফ পর্যবেক্ষণ (2D & 3D Graphs)")
    
    # ৫.১ ২ডি গ্রাফ
    st.write("### ৫.১ ২ডি ওহমিক লেখচিত্র (2D V-I Graph)")
    st.markdown("নির্দিষ্ট উষ্ণতায় পরিবাহীর বিভবপ্রভেদ ($V$) এবং তড়িৎপ্রবাহমাত্রা ($I$) এর লেখচিত্র একটি **মূলবিন্দুগামী সরলরেখা** হয়। স্লাইডার টেনে রোধের মান পরিবর্তন করে সরলরেখার নতি (Slope) পর্যবেক্ষণ করো:")
    
    selected_R = st.slider("পরিবাহীর রোধ পরিবর্তন করো (Resistance, R):", 1, 20, 5, key="normal_2d_r")
    current_range = np.linspace(0, 10, 100)
    voltage_range = current_range * selected_R
    
    fig_2d = go.Figure()
    fig_2d.add_trace(go.Scatter(x=current_range, y=voltage_range, mode='lines', line=dict(color='orange', width=4)))
    fig_2d.update_layout(xaxis_title="তড়িৎপ্রবাহমাত্রা (Current, I)", yaxis_title="বিভবপ্রভেদ (Voltage, V)", margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_2d, use_container_width=True)
    
    # ৫.২ ৩ডি গ্রাফ
    st.write("### ৫.২ ৩ডি ইন্টারেক্টিভ ল্যাব (3D Simulation Graph)")
    st.markdown("স্লাইডার দুটি পরিবর্তন করে ভোল্টেজ, কারেন্ট এবং রোধের ত্রিমাত্রিক সমতলটি পর্যবেক্ষণ করো।")
    
    max_R = st.slider("সর্বোচ্চ রোধ নির্ধারণ করো (Max Resistance, R)", 5, 20, 10, key="ohm_r")
    max_I = st.slider("সর্বোচ্চ প্রবাহমাত্রা নির্ধারণ করো (Max Current, I)", 5, 20, 10, key="ohm_i")
    
    R_val, I_val = np.meshgrid(np.linspace(0, max_R, 20), np.linspace(0, max_I, 20))
    V_val = I_val * R_val
    fig_3d = go.Figure(data=[go.Surface(x=R_val, y=I_val, z=V_val, colorscale='Viridis')])
    fig_3d.update_layout(scene=dict(xaxis_title="Resistance (R)", yaxis_title="Current (I)", zaxis_title="Voltage (V)"), margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig_3d, use_container_width=True)
    
    st.divider()
    
    # ৬. ১০টি মাল্টিপল চয়েস কোশ্চেনস
    st.subheader("৬. আত্মমূল্যায়ন কুইজ (MCQ)")
    
    questions = [
        {"q": "১. ওহমের সূত্রে কোন ভৌত রাশিটি ধ্রুবক থাকে?", "o": ["বিভবপ্রভেদ", "তড়িৎপ্রবাহ", "উষ্ণতা", "রোধ"], "a": "উষ্ণতা"},
        {"q": "২. রোধের এস.আই (SI) একক কী?", "o": ["ভোল্ট", "ওহম", "অ্যাম্পিয়ার", "ওয়াট"], "a": "ওহম"},
        {"q": "৩. ওহমের গাণিতিক রূপটি কী?", "o": ["V = I/R", "I = VR", "V = IR", "R = VI"], "a": "V = IR"},
        {"q": "৪. বিভবপ্রভেদ স্থির রেখে রোধ অর্ধেক করলে তড়িৎপ্রবাহ কী হবে?", "o": ["অর্ধেক হবে", "দ্বিগুণ হবে", "চারগুণ হবে", "একই থাকবে"], "a": "দ্বিগুণ হবে"},
        {"q": "৫. পরিবাহীর তাপমাত্রা বাড়ালে সাধারণত রোধের কী পরিবর্তন হয়?", "o": ["কমে", "বাড়ে", "একই থাকে", "শূন্য হয়"], "a": "বাড়ে"},
        {"q": "৬. ওহমের সূত্রটি নিচের কোনটির ক্ষেত্রে প্রযোজ্য নয়?", "o": ["তামার তার", "অ্যালুমিনিয়াম", "অর্ধপরিবাহী (Semiconductor)", "লোহা"], "a": "অর্ধপরিবাহী (Semiconductor)"},
        {"q": "৭. ১ ভোল্ট / ১ অ্যাম্পিয়ার = কত?", "o": ["১ ওয়াট", "১ ওহম", "১ কুলম্ব", "১ জুল"], "a": "১ ওহম"},
        {"q": "৮. তড়িৎপ্রবাহ পরিমাপ করার যন্ত্রের নাম কী?", "o": ["ভোল্টমিটার", "অ্যামিটার", "গ্যালভানোমিটার", "থার্মোমিটার"], "a": "অ্যামিটার"},
        {"q": "৯. একটি আদর্শ পরিবাহীর রোধ কত হওয়া উচিত?", "o": ["অসীম", "খুব বেশি", "শূন্য", "১ ওহম"], "a": "শূন্য"},
        {"q": "১০. V-I লেখচিত্রের নতি বা ঢাল কী নির্দেশ করে?", "o": ["পরিবাহীর রোধ", "পরিবাহীর পরিবাহিতা", "মোট আধান", "ব্যয়িত ক্ষমতা"], "a": "পরিবাহীর রোধ"}
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.write(f"**{q['q']}**")
        user_ans = st.radio("উত্তর বেছে নাও:", q['o'], key=f"q_{i}", index=None)
        if user_ans == q['a']:
            st.success("সঠিক উত্তর!")
            score += 1
        elif user_ans is not None:
            st.error(f"ভুল উত্তর। সঠিক উত্তর: {q['a']}")
        st.write("")
        
    if st.button("কুইজের ফাইনাল স্কোর দেখাও"):
        st.metric(label="তোমার মোট স্কোর", value=f"{score} / 10")

# এক্সপেরিমেন্ট ২: চৌম্বক ক্ষেত্র
elif experiment == "Magnetic Field (Helix)":
    st.header("Magnetic Field Simulation")
    st.markdown("চৌম্বক ক্ষেত্রে একটি আহিত কণার থ্রিডি গতিপথ (হেলিক্স)।")
    
    radius = st.sidebar.slider("Radius (r):", 1.0, 5.0, 2.0, key="mag_r")
    pitch = st.sidebar.slider("Pitch (p):", 1.0, 5.0, 2.0, key="mag_p")
    
    t = np.linspace(0, 20, 500)
    fig = go.Figure(data=[go.Scatter3d(x=radius*np.cos(t), y=radius*np.sin(t), z=pitch*t, mode='lines', line=dict(color=pitch*t, colorscale='Rainbow', width=6))])
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig, use_container_width=True)
