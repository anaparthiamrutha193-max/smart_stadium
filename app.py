import streamlit as st
import random
import time

st.set_page_config(page_title="Smart Stadium", layout="wide")

st.title("🏟️ Smart Stadium System")
st.write("This system helps stadium attendees avoid crowd congestion, reduce waiting time, and improve overall event experience using smart recommendations.")
st.write("AI-powered system to manage crowd flow, reduce wait times, and improve stadium experience.")

# ----------- Simulated Crowd Data -----------
sections = {
    "A": random.randint(20, 100),
    "B": random.randint(20, 100),
    "C": random.randint(20, 100),
    "D": random.randint(20, 100),
}

# ----------- Dashboard Layout -----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Live Crowd Levels")
    st.bar_chart(sections)

with col2:
    st.subheader("🚀 Smart Suggestion")
    least_crowded = min(sections, key=sections.get)
    st.info(f"👉 Move to Section {least_crowded}")
    col1, col2 = st.columns(2)

# ----------- Crowd Status -----------
st.subheader("📍 Crowd Status")

for sec, val in sections.items():
    if val > 80:
        st.error(f"Section {sec}: Overcrowded")
    elif val > 50:
        st.warning(f"Section {sec}: Moderate")
    else:
        st.success(f"Section {sec}: Comfortable")


# ----------- Smart Suggestion -----------
least_crowded = min(sections, key=sections.get)
st.info(f"👉 Best area to move: Section {least_crowded}")

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
st.subheader("🛒 In-Seat Ordering")

menu = {
    "Pizza 🍕": 200,
    "Burger 🍔": 150,
    "Popcorn 🍿": 100,
    "Cold Drink 🥤": 80
}

# Select item
food_item = st.selectbox("Select Food Item", list(menu.keys()))

# Quantity
quantity = st.slider("Select Quantity", 1, 5, 1)

# Total price
total_price = menu[food_item] * quantity
st.write(f"Total Price: ₹{total_price}")

# Order button
st.markdown("---")
st.header("🍔 Food & Services")
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
st.subheader("🚨 Emergency Support")

if st.button("Request Help"):
    st.error("🚑 Help request sent! Staff will reach you shortly.")

# ----------- Auto Refresh -----------
time.sleep(3)
st.rerun()