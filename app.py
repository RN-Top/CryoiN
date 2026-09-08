import os
from datetime import datetime, timedelta
from google import genai
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# Page Setup & Aesthetic Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="Eyerin View & Cryoin | 13-Node Planar Array",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0e14;
        color: #e6edf3;
    }
    div[data-testid="stMetricValue"] {
        font-family: monospace;
        color: #58a6ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# API Initialization
# ---------------------------------------------------------
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error(
        "Missing GEMINI_API_KEY. Configure it in your Streamlit Cloud app settings under Secrets."
    )
    st.stop()

client = genai.Client(api_key=api_key)

# ---------------------------------------------------------
# 13 Nodes: Sophia Center + 12 Outer Stations
# ---------------------------------------------------------
NODES = [
    {
        "id": 0,
        "name": "Sophia (The Apex)",
        "feature": "Central Convergence & Divine Keystone",
        "r": 0.00,
        "theta": 0.0,
        "color": "#ffffff",
        "freq": 963,
    },
    {
        "id": 1,
        "name": "Giza Plateau",
        "feature": "Pyramidal Horizon & Cardinal Gateway",
        "r": 0.33,
        "theta": 31.13,
        "color": "#ffd700",
        "freq": 432,
    },
    {
        "id": 2,
        "name": "Stonehenge",
        "feature": "Megalithic Solstice Transit",
        "r": 0.22,
        "theta": 358.17,
        "color": "#76ff03",
        "freq": 528,
    },
    {
        "id": 3,
        "name": "Hessdalen Valley",
        "feature": "Atmospheric Ion Light Station",
        "r": 0.15,
        "theta": 11.19,
        "color": "#00e5ff",
        "freq": 639,
    },
    {
        "id": 4,
        "name": "Mount Kailash",
        "feature": "Trans-Himalayan Spire & Axis Mundi",
        "r": 0.33,
        "theta": 81.31,
        "color": "#b388ff",
        "freq": 852,
    },
    {
        "id": 5,
        "name": "Teotihuacan",
        "feature": "Solar Avenue of the Ancestors",
        "r": 0.39,
        "theta": 261.16,
        "color": "#ff9100",
        "freq": 741,
    },
    {
        "id": 6,
        "name": "Southwest Florida",
        "feature": "Calusa Marine Shell Estuary Nexus",
        "r": 0.35,
        "theta": 278.20,
        "color": "#00b0ff",
        "freq": 417,
    },
    {
        "id": 7,
        "name": "Detroit / Canton",
        "feature": "Laurentian Freshwater Confluence",
        "r": 0.26,
        "theta": 276.52,
        "color": "#4caf50",
        "freq": 396,
    },
    {
        "id": 8,
        "name": "Roanoke, Virginia",
        "feature": "Blue Ridge Rift & Valley Threshold",
        "r": 0.29,
        "theta": 280.06,
        "color": "#e040fb",
        "freq": 528,
    },
    {
        "id": 9,
        "name": "Sedona",
        "feature": "Ferrous Sandstone Vortex Core",
        "r": 0.31,
        "theta": 248.24,
        "color": "#ff5252",
        "freq": 432,
    },
    {
        "id": 10,
        "name": "Angkor Wat",
        "feature": "Microcosmic Lotus Reflection",
        "r": 0.43,
        "theta": 103.87,
        "color": "#ffab00",
        "freq": 639,
    },
    {
        "id": 11,
        "name": "Machu Picchu",
        "feature": "Andean Intihuatana Sun Tether",
        "r": 0.57,
        "theta": 287.46,
        "color": "#69f0ae",
        "freq": 741,
    },
    {
        "id": 12,
        "name": "Cryoin (Antarctica)",
        "feature": "Outer Perimeter Baseline & Ice Rim",
        "r": 1.00,
        "theta": 180.0,
        "color": "#80d8ff",
        "freq": 174,
    },
]

# ---------------------------------------------------------
# Sidebar Controls & Cartographic Overlay Options
# ---------------------------------------------------------
st.sidebar.title("🧭 Apex Earth Deck")
st.sidebar.caption("Planar 1500s Azimuthal Array")

selected_id = st.sidebar.selectbox(
    "Target Node Focus",
    options=[n["id"] for n in NODES],
    format_func=lambda x: f"[{x}] {NODES[x]['name']}",
)
selected_node = NODES[selected_id]

st.sidebar.markdown("---")
st.sidebar.subheader("Array Overlays")
show_rays = st.sidebar.checkbox("Emit Sophia Radial Vectors", value=True)
show_resonance = st.sidebar.checkbox("Calculate Harmonic Triads", value=True)
show_field_wave = st.sidebar.checkbox("Simulate Magnetic Radial Spiral", value=True)
transit_speed = st.sidebar.slider("Array Cycle Cadence (hours)", 1, 24, 6)

# ---------------------------------------------------------
# Calculations & Real-time Metrics
# ---------------------------------------------------------
now_utc = datetime.utcnow()
sim_pulse_phase = (now_utc.minute * 60 + now_utc.second) / 3600.0 * 2 * np.pi

m1, m2, m3, m4 = st.columns(4)
m1.metric("Station Focus", f"[{selected_node['id']}] {selected_node['name'].split()[0]}")
m2.metric("Radius / Polar Distance", f"{selected_node['r']:.2f} R")
m3.metric("Azimuth Vector", f"{selected_node['theta']:.1f}°")
m4.metric("Harmonic Resonance", f"{selected_node['freq']} Hz")

# ---------------------------------------------------------
# Two-Column Layout: Visual Cartography vs Telemetry & Intel
# ---------------------------------------------------------
col_deck, col_intel = st.columns([1.35, 1.0], gap="medium")

with col_deck:
    st.subheader("1500s Polar Planar Projection")

    fig, ax = plt.subplots(figsize=(7.5, 7.5), subplot_kw={"projection": "polar"})
    fig.patch.set_facecolor("#0b0e14")
    ax.set_facecolor("#111622")

    for r_ring in [0.25, 0.50, 0.75, 1.00]:
        ax.plot(
            np.linspace(0, 2 * np.pi, 300),
            [r_ring] * 300,
            color="#21283b",
            linestyle="--",
            linewidth=0.8,
            zorder=1,
        )

    ax.plot(
        np.linspace(0, 2 * np.pi, 500),
        [1.0] * 500,
        color="#80d8ff",
        linewidth=2.2,
        alpha=0.6,
        label="Cryoin Outer Rim",
        zorder=2,
    )

    if show_field_wave:
        spiral_theta = np.linspace(0, 4 * np.pi, 400)
        spiral_r = np.linspace(0.02, 0.98, 400)
        spiral_theta_rot = spiral_theta + sim_pulse_phase
        ax.plot(
            spiral_theta_rot,
            spiral_r,
            color="#388bfd",
            alpha=0.18,
            linewidth=1.5,
            linestyle=":",
            zorder=2,
        )

    if show_rays:
        for n in NODES[1:]:
            th = np.radians(n["theta"])
            ax.plot([0, th], [0, n["r"]], color="#58a6ff", alpha=0.18, linewidth=1.0, zorder=2)

    if selected_node["id"] != 0:
        sel_th = np.radians(selected_node["theta"])
        ax.plot(
            [0, sel_th],
            [0, selected_node["r"]],
            color=selected_node["color"],
            alpha=0.85,
            linewidth=2.0,
            zorder=3,
        )

    if show_resonance and selected_node["id"] != 0:
        triad_1 = NODES[(selected_node["id"] + 4) % 12 or 12]
        triad_2 = NODES[(selected_node["id"] + 8) % 12 or 12]
        tri_theta = [
            np.radians(selected_node["theta"]),
            np.radians(triad_1["theta"]),
            np.radians(triad_2["theta"]),
            np.radians(selected_node["theta"]),
        ]
        tri_r = [selected_node["r"], triad_1["r"], triad_2["r"], selected_node["r"]]
        ax.plot(
            tri_theta,
            tri_r,
            color="#ffd700",
            alpha=0.35,
            linestyle="-.",
            linewidth=1.2,
            zorder=3,
        )

    for n in NODES:
        th = np.radians(n["theta"])
        is_sel = n["id"] == selected_id
        size = 200 if is_sel else (120 if n["id"] == 0 else 65)
        edge = "#ffffff" if is_sel else ("#388bfd" if n["id"] == 0 else "#161b22")
        ax.scatter(
            th,
            n["r"],
            color=n["color"],
            s=size,
            edgecolors=edge,
            linewidths=1.8,
            zorder=5,
        )
        ax.text(
            th,
            n["r"] + 0.045,
            f"{n['id']}",
            color="#c9d1d9",
            fontsize=8.5,
            ha="center",
            weight="bold",
            zorder=6,
        )

    ax.set_yticklabels([])
    ax.set_xticks(np.linspace(0, 2 * np.pi, 12, endpoint=False))
    ax.set_xticklabels(
        ["0°", "30°", "60°", "90°", "120°", "150°", "180°", "210°", "240°", "270°", "300°", "330°"],
        color="#8b949e",
        fontsize=7.5,
    )
    ax.spines["polar"].set_color("#30363d")
    ax.grid(color="#1f2430", linewidth=0.7)

    st.pyplot(fig)
    st.caption(
        f"**Locked Node Matrix:** [{selected_node['id']}] {selected_node['name']} — "
        f"*{selected_node['feature']}*"
    )

with col_intel:
    st.subheader("Harmonic Transit Windows")

    transits = []
    for idx, n in enumerate(NODES):
        offset = idx * (transit_speed / 12.0)
        p_time = now_utc + timedelta(hours=offset)
        transits.append(
            {
                "ID": f"#{n['id']}",
                "Station": n["name"],
                "Transit Window": p_time.strftime("%H:%M:%S UTC"),
                "Harmonic": f"{n['freq']} Hz",
                "Status": "Direct Lock" if n["id"] == selected_id else "Harmonized",
            }
        )

    st.dataframe(pd.DataFrame(transits), hide_index=True, use_container_width=True)

    st.markdown("---")
    st.subheader("Mission Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": f"Eyerin-Cryoin array synchronized. Sophia core anchoring {selected_node['name']}.",
            }
        ]

    chat_box = st.container(height=260)
    with chat_box:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    query = st.chat_input("Inquire about harmonic intersections, alignments, or node transits...")
    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with chat_box:
            with st.chat_message("user"):
                st.markdown(query)
            with st.chat_message("assistant"):
                prompt = (
                    f"You are the cartographic and orbital intelligence officer for the Eyerin-Cryoin array, "
                    f"modeled on a 1500s azimuthal equidistant polar disc. "
                    f"Central Hub: Sophia (Node 0). Outer Perimeter: Cryoin Antarctica (Node 12). "
                    f"Currently focused target: [{selected_node['id']}] {selected_node['name']} "
                    f"({selected_node['feature']}) at {selected_node['r']} radius, {selected_node['theta']}° azimuth, "
                    f"vibrating at {selected_node['freq']} Hz. "
                    f"Deliver concise, intriguing, and precise observations."
                )
                try:
                    res = client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=[prompt, query],
                    )
                    reply_text = res.text
                except Exception as e:
                    reply_text = f"⚠️ **API Error Details:**\n```\n{e}\n```"

                st.markdown(reply_text)
                st.session_state.messages.append({"role": "assistant", "content": reply_text})
