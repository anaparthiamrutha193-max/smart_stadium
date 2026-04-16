import streamlit as st
import random
import time

# MUST be first Streamlit command
st.set_page_config(page_title="Smart Stadium", layout="wide")

st.title("🏟️ Smart Stadium System")

st.success("✅ Live system active - monitoring stadium")

# ----------- Problem Statement ----------- 
st.header("🎯 Problem Solution")
st.write("""
This system solves real stadium challenges:
- Crowd congestion
- Long waiting times
- Poor coordination

It provides:
- Real-time crowd monitoring
- Smart navigation suggestions
- Queue prediction
- In-seat ordering
""")

st.write("AI-powered system to manage crowd flow, reduce wait times, and improve stadium experience.")

# ----------- Simulated Crowd Data ----------- 
@st.cache_data
def get_data():
    return {
        "A": random.randint(20, 100),
        "B": random.randint(20, 100),
        "C": random.randint(20, 100),
        "D": random.randint(20, 100),
    }

sections = get_data()

# ----------- Dashboard ----------- 
col1, col2 = st.columns(2)

with col1:
    st.caption("📊 Shows crowd density in each section")
    st.subheader("📊 Live Crowd Levels")
    st.bar_chart(sections)

with col2:
    st.caption("🚀 Suggests less crowded area")
    st.subheader("🚀 Smart Suggestion")
    least_crowded = min(sections, key=sections.get)
    st.info(f"👉 Move to Section {least_crowded}")

# ----------- Crowd Status ----------- 
st.subheader("📍 Crowd Status")

for sec, val in sections.items():
    if val > 80:
        st.error(f"Section {sec}: Overcrowded")
    elif val > 50:
        st.warning(f"Section {sec}: Moderate")
    else:
        st.success(f"Section {sec}: Comfortable")

# ----------- Queue Prediction ----------- 
st.subheader("🍔 Food Stall Wait Time")

people = random.randint(5, 50)
service_rate = 5
wait_time = people // service_rate

st.write(f"People in queue: {people}")
st.write(f"Estimated wait time: {wait_time} mins")

if wait_time > 8:
    st.warning("⚠️ High wait time! Try another stall.")
else:
    st.success("✅ Queue is manageable.")

# ----------- In-Seat Ordering ----------- 
st.markdown("---")
st.header("🛒 In-Seat Ordering")

menu = {
    "Pizza 🍕": 200,
    "Burger 🍔": 150,
    "Popcorn 🍿": 100,
    "Cold Drink 🥤": 80
}

food_item = st.selectbox("Select Food Item", list(menu.keys()))
quantity = st.slider("Select Quantity", 1, 5, 1)

total_price = menu[food_item] * quantity
st.write(f"Total Price: ₹{total_price}")

if "order" not in st.session_state:
    st.session_state["order"] = False

if st.button("Place Order"):
    st.session_state["order"] = True

if st.session_state["order"]:
    st.success(f"✅ Order placed: {food_item} x {quantity}")
    st.info("⏱️ Estimated delivery time: 10 mins")

if st.button("Cancel Order"):
    st.session_state["order"] = False
    st.warning("❌ Order cancelled")

# ----------- Emergency Feature ----------- 
st.markdown("---")
st.header("🚨 Safety & Support")

if st.button("Request Help"):
    st.error("🚑 Help request sent! Staff will reach you shortly.")

# ----------- Auto Refresh ----------- 
time.sleep(3)
st.rerun()
