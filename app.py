import streamlit as st

# ওয়েবসাইটের পেজ কনফিগারেশন
st.set_page_config(page_title="SimuLab - Virtual Physics", layout="wide")

# সাইডবার মেনু
st.sidebar.title("🎛️ Control Panel")
experiment = st.sidebar.selectbox("Select Chapter:", ["Home", "Ohm's Law", "Magnetic Field (Helix)"])

# হোম পেজ কাঠামো
if experiment == "Home":
    st.title("⚛️ SimuLab: Interactive Physics Laboratory")
    st.write("ভার্চুয়াল ফিজিক্স ল্যাবরেটরিতে স্বাগতম। বাঁদিকের কন্ট্রোল প্যানেল থেকে যেকোনো অধ্যায় সিলেক্ট করে পড়া এবং থ্রিডি সিমুলেশন দেখা শুরু করো।")

# ওহমের সূত্র ফাইল লিঙ্ক করা
elif experiment == "Ohm's Law":
    import ohms_law
    ohms_law.run()

# ম্যাগনিফিকেশন বা ম্যাগনেটিক ফিল্ড ফাইল লিঙ্ক করা
elif experiment == "Magnetic Field (Helix)":
    import magnetic_field
    magnetic_field.run()
