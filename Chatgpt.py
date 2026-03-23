import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Friction Vision",
    page_icon="⚙️",
    layout="wide"
)

# ─────────────────────────────────────────────
# Title
# ─────────────────────────────────────────────
st.title("⚙️ Friction Vision")
st.subheader("Interactive Friction Analysis Tool for Engineering Mechanics")

# ─────────────────────────────────────────────
# Sidebar Inputs
# ─────────────────────────────────────────────
st.sidebar.header("🔧 Input Parameters")

m = st.sidebar.slider("Mass (kg)", 1, 100, 10)
mu = st.sidebar.slider("Coefficient of Friction (μ)", 0.1, 1.0, 0.5)
theta = st.sidebar.slider("Angle (degrees)", 0, 60, 10)

g = 9.81
theta_rad = np.radians(theta)

# ─────────────────────────────────────────────
# Core Calculations
# ─────────────────────────────────────────────
N = m * g * np.cos(theta_rad)
F_friction = mu * N
F_down = m * g * np.sin(theta_rad)

# ─────────────────────────────────────────────
# Metrics
# ─────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

col1.metric("Normal Reaction (N)", f"{N:.2f}")
col2.metric("Friction Force (N)", f"{F_friction:.2f}")
col3.metric("Downward Force (N)", f"{F_down:.2f}")

# ─────────────────────────────────────────────
# Motion Decision
# ─────────────────────────────────────────────
if F_down > F_friction:
    st.error("🚨 Object WILL MOVE (Sliding)")
else:
    st.success("✅ Object will NOT move (Static)")

# ─────────────────────────────────────────────
# Critical Angle
# ─────────────────────────────────────────────
theta_critical = np.degrees(np.arctan(mu))
st.info(f"Critical Angle = {theta_critical:.2f}°")

# ─────────────────────────────────────────────
# GRAPH 1: Friction vs Normal Force
# ─────────────────────────────────────────────
st.subheader("📊 Friction vs Normal Force")

N_vals = np.linspace(0, 500, 100)
F_vals = mu * N_vals

fig1, ax1 = plt.subplots()
ax1.plot(N_vals, F_vals)
ax1.set_xlabel("Normal Force (N)")
ax1.set_ylabel("Friction Force (N)")
ax1.set_title("F = μN")

st.pyplot(fig1)

# ─────────────────────────────────────────────
# GRAPH 2: Angle vs Motion
# ─────────────────────────────────────────────
st.subheader("📈 Angle vs Motion Behavior")

angles = np.linspace(0, 60, 100)
motion = []

for ang in angles:
    ang_rad = np.radians(ang)
    Fd = m * g * np.sin(ang_rad)
    Ff = mu * m * g * np.cos(ang_rad)
    motion.append(Fd - Ff)

fig2, ax2 = plt.subplots()
ax2.plot(angles, motion)
ax2.axhline(0, linestyle='--')
ax2.set_xlabel("Angle (degrees)")
ax2.set_ylabel("F_down - F_friction")
ax2.set_title("Motion Condition Graph")

st.pyplot(fig2)

# ─────────────────────────────────────────────
# VISUAL SIMULATION
# ─────────────────────────────────────────────
st.subheader("🎮 Visual Simulation")

fig3, ax3 = plt.subplots()

# Inclined plane line
x = np.linspace(0, 5, 100)
y = np.tan(theta_rad) * x
ax3.plot(x, y)

# Block position
block_x = 2
block_y = np.tan(theta_rad) * block_x

ax3.scatter(block_x, block_y, s=200)

# Arrow (force)
ax3.arrow(block_x, block_y, 0.5, -0.5, head_width=0.1)

ax3.set_title("Block on Inclined Plane")
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)

st.pyplot(fig3)

# ─────────────────────────────────────────────
# MATERIAL COMPARISON
# ─────────────────────────────────────────────
st.subheader("🧪 Material Comparison")

materials = {
    "Rubber": 0.8,
    "Steel": 0.6,
    "Wood": 0.4,
    "Ice": 0.1
}

mat_choice = st.selectbox("Select Material", list(materials.keys()))
mu_mat = materials[mat_choice]

F_mat = mu_mat * N

st.write(f"μ = {mu_mat}")
st.write(f"Friction Force = {F_mat:.2f} N")

# ─────────────────────────────────────────────
# Real Life Insight
# ─────────────────────────────────────────────
st.subheader("🚗 Real Life Insight")

if mu < 0.3:
    st.warning("Low friction → Risk of slipping (like wet roads)")
elif mu < 0.6:
    st.info("Moderate friction → Normal conditions")
else:
    st.success("High friction → Strong grip (like racing tires)")

# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown("### 👨‍💻 Engineered by You")
