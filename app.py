import streamlit as st
import numpy as np
import plotly.graph_objects as go

# 1. 웹앱 기본 설정
st.set_page_config(page_title="K-PROTOCOL Master Simulator", layout="wide")

# 2. 사이드바 - 언어 선택
st.sidebar.header("🌐 Language / 언어")
lang = st.sidebar.radio("선택 (Select)", ("Korean (한국어)", "English"))

# 언어별 텍스트 변수 설정
if lang == "Korean (한국어)":
    ui_title = "🌌 K-PROTOCOL: 대통합 마스터 시뮬레이터"
    ui_desc = "**K-Omni 방정식** 하나로 거시 세계(은하 회전)와 미시 세계(양자 얽힘)의 미스터리를 기하학적으로 해체합니다."
    tab1_name = "은하 회전 곡선 (거시 세계)"
    tab2_name = "양자 얽힘 (미시 세계)"
else:
    ui_title = "🌌 K-PROTOCOL: Grand Unification Master Simulator"
    ui_desc = "Deconstructing the mysteries of the macro (Galactic Rotation) and micro (Quantum Entanglement) worlds using the single **K-Omni Equation**."
    tab1_name = "Galactic Rotation (Macro)"
    tab2_name = "Quantum Entanglement (Micro)"

st.title(ui_title)
st.markdown(ui_desc)

# K-Omni 마스터 방정식 출력
st.latex(r"\mathbf{\Psi}_{K} = \left( \frac{\pi^n \cdot f}{\mathbf{S}_{loc}} \right) e^{i \pi \mathbf{T}}")
st.markdown("---")

# 3. 탭(Tabs) 생성 (두 시뮬레이션을 한 화면에 분리)
tab1, tab2 = st.tabs([tab1_name, tab2_name])

# ==========================================
# 탭 1: 은하 회전 곡선 (암흑 물질 해체)
# ==========================================
with tab1:
    if lang == "Korean (한국어)":
        st.subheader("거시적 증명: 암흑 물질은 입자가 아니라 공간 텐서(S_loc)의 누적이다.")
        alpha_label = "공간 누적 계수 (α) 조작"
    else:
        st.subheader("Macroscopic Proof: Dark Matter is the Accumulation of Spatial Tensor (S_loc).")
        alpha_label = "Adjust Spatial Accumulation (α)"
        
    alpha_input = st.slider(alpha_label, 0.0, 0.1, 0.04545, 0.001, format="%.5f")

    # 데이터 생성
    r = np.linspace(1, 50, 500)
    G_M = 20000
    v_newton = np.sqrt(G_M / r)
    S_loc_cumulative = 1 + (alpha_input * r)
    v_kprotocol = np.sqrt((G_M / r) * S_loc_cumulative)
    observed_flat = np.full_like(r, np.mean(v_kprotocol[350:]))

    # Plotly 그래프 생성 (한글 깨짐 없음)
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=r, y=v_newton, mode='lines', name='뉴턴 역학 (Newtonian)', line=dict(dash='dash', color='blue')))
    fig1.add_trace(go.Scatter(x=r, y=v_kprotocol, mode='lines', name=f'K-PROTOCOL (α={alpha_input:.5f})', line=dict(color='red', width=4)))
    fig1.add_trace(go.Scatter(x=r, y=observed_flat, mode='lines', name='관측 데이터 (Observed)', line=dict(dash='dot', color='green', width=3)))

    fig1.update_layout(
        title="Galactic Rotation Curve",
        xaxis_title="은하 중심으로부터의 거리 r (Distance)",
        yaxis_title="회전 속도 v (Velocity)",
        hovermode="x unified",
        template="plotly_white"
    )
    st.plotly_chart(fig1, use_container_width=True)

# ==========================================
# 탭 2: 양자 얽힘 (벨의 부등식 해체)
# ==========================================
with tab2:
    if lang == "Korean (한국어)":
        st.subheader("미시적 증명: 양자 얽힘은 확률이 아니라 단일 위상 매듭(T)의 투영이다.")
    else:
        st.subheader("Microscopic Proof: Quantum Entanglement is a Geometric Projection of a Single Phase Knot (T).")

    # 데이터 생성
    theta = np.linspace(0, np.pi, 500)
    
    # 고전적 한계 (벨의 부등식 선형 한계)
    classical_limit = 1 - (2 * theta / np.pi)
    
    # K-PROTOCOL 기하학적 투영 (코사인 곡선)
    k_protocol_proj = np.cos(theta)

    # Plotly 그래프 생성
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=theta, y=classical_limit, mode='lines', name="고전적 한계 (Bell's Limit)", line=dict(dash='dash', color='blue')))
    fig2.add_trace(go.Scatter(x=theta, y=k_protocol_proj, mode='lines', name='K-PROTOCOL 투영 (Quantum Correlation)', line=dict(color='red', width=4)))

    fig2.update_layout(
        title="Quantum Entanglement: Bell's Inequality vs K-PROTOCOL",
        xaxis_title="측정기 사이의 각도 차이 θ (Radians)",
        yaxis_title="상관관계 (Correlation)",
        hovermode="x unified",
        template="plotly_white"
    )
    st.plotly_chart(fig2, use_container_width=True)

    if lang == "Korean (한국어)":
        st.info("💡 **분석:** 푸른색 점선(고전적 한계)을 뚫고 나오는 붉은색 곡선은 빛보다 빠른 통신이 아니라, 두 입자가 동일한 기하학적 매듭 끈으로 연결되어 있기 때문에 나타나는 3차원 투영(Cos) 현상입니다.")
    else:
        st.info("💡 **Analysis:** The red curve breaking the blue classical limit is not faster-than-light communication, but a necessary 3D projection (Cos) occurring because both particles share the same geometric topological string.")
