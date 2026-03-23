import streamlit as st
import numpy as np

# ─────────────────────────────
# Page config
# ─────────────────────────────
st.set_page_config(page_title="Friction Vision", layout="wide")

st.title("⚙️ Friction Vision")
st.subheader("No-error version (Mobile Friendly)")

# ─────────────────────────────
# Inputs
# ─────────────────────────────
m = st.slider("Mass (kg)", 1, 100, 10)
mu = st.slider("Coefficient of friction (μ)", 0.1, 1.0, 0.5)
theta = st.slider("Angle (degrees)", 0, 60, 10)

g = 9.81
theta_rad = np.radians(theta)

# ─────────────────────────────
# Calculations
# ─────────────────────────────
N = m * g * np.cos(theta_rad)
F_friction = mu * N
F_down = m * g * np.sin(theta_rad)

# ─────────────────────────────
# Metrics
# ─────────────────────────────
c1, c2, c3 = st.columns(3)
c1.metric("Normal Force", f"{N:.2f} N")
c2.metric("Friction", f"{F_friction:.2f} N")
c3.metric("Downward Force", f"{F_down:.2f} N")

# ─────────────────────────────
# Motion
# ─────────────────────────────
if F_down > F_friction:
    st.error("🚨 Object WILL MOVE")
else:
    st.success("✅ Object will NOT move")

# ─────────────────────────────
# Critical Angle
# ─────────────────────────────
theta_c = np.degrees(np.arctan(mu))
st.info(f"Critical Angle: {theta_c:.2f}°")

# ─────────────────────────────
# Graph 1 (No matplotlib)
# ─────────────────────────────
st.subheader("📊 Friction vs Normal Force")

N_vals = np.linspace(0, 500, 100)
F_vals = mu * N_vals

st.line_chart({"Normal Force": N_vals, "Friction": F_vals})

# ─────────────────────────────
# Graph 2 (Angle vs Motion)
# ─────────────────────────────
st.subheader("📈 Angle vs Motion")

angles = np.linspace(0, 60, 100)
motion = []

for ang in angles:
    ang_rad = np.radians(ang)
    motion.append(m*g*np.sin(ang_rad) - mu*m*g*np.cos(ang_rad))

st.line_chart({"Angle": angles, "Motion Condition": motion})

# ─────────────────────────────
# Material Comparison
# ─────────────────────────────
st.subheader("🧪 Material Comparison")

materials = {
    "Rubber": 0.8,
    "Steel": 0.6,
    "Wood": 0.4,
    "Ice": 0.1
}

mat = st.selectbox("Material", list(materials.keys()))
mu_mat = materials[mat]

st.write(f"μ = {mu_mat}")
st.write(f"Friction = {mu_mat * N:.2f} N")

# ─────────────────────────────
# Real-life Insight
# ─────────────────────────────
st.subheader("🚗 Real-life Insight")

if mu < 0.3:
    st.warning("⚠️ Slippery (wet roads)")
elif mu < 0.6:
    st.info("Normal condition")
else:
    st.success("High grip (racing tires)")

st.markdown("---")
st.markdown("### 👨‍💻 Engineered by You")
