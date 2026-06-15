import streamlit as st

# ওয়েবসাইটের পেজ কনফিগারেশন
st.set_page_config(page_title="SimuLab - Virtual Physics", layout="wide")

# Session State তৈরি করা (কোন বক্সে ক্লিক হয়েছে তা মনে রাখার জন্য)
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None

# ================= সাইডবার (Control Panel) =================
st.sidebar.title("🎛️ Physics Panel")

# ১. ক্লাস বা কোর্স সিলেক্ট করা
category = st.sidebar.selectbox("Class / Target:", ["Class 10 (CBSE)", "Class 11 (CBSE)", "Class 12 (CBSE)", "JEE Main/Adv", "NEET"])

# ২. সিলেক্ট করা ক্লাসের ওপর ভিত্তি করে চ্যাপ্টারগুলো দেখানো
chapters = []
if category == "Class 10 (CBSE)":
    chapters = ["Electricity", "Magnetic Effects of Electric Current", "Light - Reflection & Refraction", "The Human Eye"]
elif category == "Class 11 (CBSE)":
    chapters = ["Kinematics", "Laws of Motion", "Work, Energy and Power", "Gravitation"]
elif category == "Class 12 (CBSE)":
    chapters = ["Electrostatics", "Current Electricity", "Magnetism", "Optics"]
else:
    chapters = ["Syllabus Update in Progress..."]

chapter = st.sidebar.selectbox("Select Chapter:", chapters)

# যদি সাইডবার থেকে চ্যাপ্টার পরিবর্তন করা হয়, তবে বক্সের পেজে ফিরে আসার জন্য
if st.sidebar.button("🔄 Refresh / Home"):
    st.session_state.selected_topic = None
    st.rerun()

# ================= মূল পেজ (Home Page / Box Grid) =================

# যদি কোনো বক্সে ক্লিক না হয়ে থাকে, তবে ফ্লিপকার্টের মতো বক্সগুলো দেখাবে
if st.session_state.selected_topic is None:
    st.title(f"📚 {category}")
    st.subheader(f"Chapter: {chapter}")
    st.markdown("নিচের যেকোনো টপিক বক্সে ক্লিক করে বিস্তারিত ল্যাব, থিওরি এবং থ্রিডি সিমুলেশন দেখো:")
    st.divider()

    # Class 10 এর চ্যাপ্টার অনুযায়ী বক্স তৈরি (ফ্লিপকার্ট স্টাইল)
    if chapter == "Electricity":
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
                st.button("Coming Soon...", disabled=True) # এটি পরে তৈরি করা হবে
                
        with col3:
            with st.container(border=True):
                st.subheader("🔥 Joule's Law")
                st.write("তড়িৎপ্রবাহের তাপীয় ফল।")
                st.button("Coming Soon...", key="btn_joule", disabled=True)

    elif chapter == "Magnetic Effects of Electric Current":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            with st.container(border=True):
                st.subheader("🧲 Magnetic Field")
                st.write("চৌম্বক ক্ষেত্রে আহিত কণার থ্রিডি গতিপথ (Helix)।")
                if st.button("ল্যাব খুলুন", key="btn_mag"):
                    st.session_state.selected_topic = "Magnetic Field (Helix)"
                    st.rerun()

    elif chapter == "Light - Reflection & Refraction":
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
# যদি বক্সে ক্লিক করা হয়ে থাকে, তবে সেই নির্দিষ্ট ল্যাবটি খুলবে
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
