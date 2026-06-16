import streamlit as st

# ওয়েবসাইটের পেজ কনফিগারেশন
st.set_page_config(page_title="SimuLab - Virtual Physics", page_icon="logo.jpeg", layout="wide")

# Session State তৈরি করা (কোন বক্সে ক্লিক হয়েছে তা মনে রাখার জন্য)
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None

# ================= সাইডবার (Control Panel) =================
st.sidebar.title("🎛️ Physics Panel")

# ১. প্রধান ক্যাটাগরি বা টার্গেট সিলেক্ট করা
category = st.sidebar.selectbox("Target / Exam:", ["Class 10 (CBSE)", "JEE Main & Advanced", "NEET"])

# ২. সাব-ক্যাটাগরি (Class 11 বা Class 12) এবং চ্যাপ্টার সিলেক্ট করা
chapters = []
selected_class_label = category # ডিফল্ট লেবেল

if category == "Class 10 (CBSE)":
    chapters = ["Electricity", "Magnetic Effects of Electric Current", "Light - Reflection & Refraction", "The Human Eye"]
else:
    # JEE বা NEET সিলেক্ট করলে Class 11 এবং Class 12 এর ড্রপডাউন আসবে
    sub_class = st.sidebar.selectbox("Select Class:", ["Class 11", "Class 12"])
    selected_class_label = f"{category} - {sub_class}"
    
    if sub_class == "Class 11":
        chapters = ["Kinematics", "Laws of Motion", "Work, Energy and Power", "Gravitation"]
    elif sub_class == "Class 12":
        chapters = ["Electrostatics", "Current Electricity", "Magnetism", "Optics"]

# ৩. চ্যাপ্টার সিলেক্ট করা
chapter = st.sidebar.selectbox("Select Chapter:", chapters)

# Refresh বাটন
if st.sidebar.button("🔄 Refresh / Home"):
    st.session_state.selected_topic = None
    st.rerun()

# ================= মূল পেজ (Home Page / Box Grid) =================

# যদি কোনো বক্সে ক্লিক না হয়ে থাকে, তবে বক্সগুলো দেখাবে
if st.session_state.selected_topic is None:
    st.title(f"📚 {selected_class_label}")
    st.subheader(f"Chapter: {chapter}")
    st.markdown("নিচের যেকোনো টপিক বক্সে ক্লিক করে বিস্তারিত ল্যাব, থিওরি এবং থ্রিডি সিমুলেশন দেখো:")
    st.divider()

    # Class 10 এর চ্যাপ্টার অনুযায়ী বক্স তৈরি
    if chapter == "Electricity" and category == "Class 10 (CBSE)":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            with st.container(border=True):
                st.subheader("🔌 Ohm's Law")
                st.write("ভোল্টেজ, কারেন্ট ও রোধের সম্পর্ক এবং গ্রাফ।")
                if st.button("ল্যাব খুলুন", key="btn_ohm"):
                    st.session_state.selected_topic = "Ohm's Law"
                    st.rerun()
                    
        with col2:
            with st.container(border=True):
                st.subheader("⚡ Resistance")
                st.write("রোধের সমবায় (Series & Parallel)।")
                st.button("Coming Soon...", disabled=True)
                
        with col3:
            with st.container(border=True):
                st.subheader("🔥 Joule's Law")
                st.write("তড়িৎপ্রবাহের তাপীয় ফল।")
                st.button("Coming Soon...", key="btn_joule", disabled=True)

    elif chapter == "Magnetic Effects of Electric Current" and category == "Class 10 (CBSE)":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            with st.container(border=True):
                st.subheader("🧲 Magnetic Field")
                st.write("চৌম্বক ক্ষেত্রে আহিত কণার থ্রিডি গতিপথ (Helix)।")
                if st.button("ল্যাব খুলুন", key="btn_mag"):
                    st.session_state.selected_topic = "Magnetic Field (Helix)"
                    st.rerun()

    elif chapter == "Light - Reflection & Refraction" and category == "Class 10 (CBSE)":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            with st.container(border=True):
                st.subheader("🔦 Optics (Mirrors)")
                st.write("দর্পণের সূত্র, ফোকাস দৈর্ঘ্য ও বিবর্ধন।")
                if st.button("ল্যাব খুলুন", key="btn_opt"):
                    st.session_state.selected_topic = "Optics"
                    st.rerun()

    else:
        st.info("এই চ্যাপ্টারের ল্যাবগুলো খুব তাড়াতাড়ি যুক্ত করা হবে!")

# ================= ল্যাব পেজ (Lab Page) =================
# যদি বক্সে ক্লিক করা হয়ে থাকে
else:
    # ফিরে যাওয়ার বাটন
    if st.button("⬅️ Back to Topics Grid"):
        st.session_state.selected_topic = None
        st.rerun()
    
    st.divider()

    # নির্দিষ্ট ফাইল লিঙ্ক করা
    topic = st.session_state.selected_topic
    
    if topic == "Ohm's Law":
        import ohms_law
        ohms_law.run()
    elif topic == "Magnetic Field (Helix)":
        import magnetic_field
        magnetic_field.run()
    elif topic == "Optics":
        import optics
        optics.run()
