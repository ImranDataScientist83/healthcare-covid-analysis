
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import random

# Page configuration
st.set_page_config(
    page_title="Wildlife Agentic AI Platform",
    page_icon=":panda:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .main-header {
        background: linear-gradient(135deg, #2ECC71, #27AE60);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .alert-card {
        background-color: #FFF3CD;
        border-left: 4px solid #FFC107;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header"><h1>Wildlife Agentic AI Platform</h1><p>Conservation | Guest Experience | Commercial Optimization</p></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/panda.png", width=80)
    st.markdown("## Control Panel")

    selected_agent = st.selectbox(
        "Select Agent",
        ["Overview", "Conservation Agent", "Guest Experience Agent", "Commercial Agent", "Agent Orchestrator"]
    )

    st.markdown("---")
    st.markdown("### System Status")
    st.markdown("All Systems Operational")
    st.markdown(f"Last Updated: {datetime.now().strftime('%H:%M:%S')}")

    st.markdown("---")
    st.markdown("### Responsible AI")
    st.markdown("Fairness Check: Passed")
    st.markdown("Privacy Check: Passed")
    st.markdown("Safety Check: Passed")

# Generate sample data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
conservation_data = pd.DataFrame({
    'date': dates,
    'animals_monitored': np.random.randint(450, 550, 30),
    'alerts_generated': np.random.randint(2, 15, 30),
    'response_time_min': np.random.uniform(5, 30, 30)
})

visitor_data = pd.DataFrame({
    'date': dates,
    'visitors': np.random.randint(800, 1200, 30),
    'satisfaction': np.random.uniform(3.5, 4.8, 30),
    'spend_avg': np.random.uniform(45, 85, 30)
})

# Overview Dashboard
if selected_agent == "Overview":
    st.markdown("## Platform Overview")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Animals Protected", "10,000+", "+2.3%")
    with col2:
        st.metric("Visitors Served", "50,000+", "+5.2%")
    with col3:
        st.metric("Revenue Generated", "$2.5M", "+8.1%")
    with col4:
        st.metric("Alerts Resolved", "98.5%", "+1.2%")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Conservation Activity")
        fig = px.line(conservation_data, x='date', y='alerts_generated', 
                      title='Daily Alerts Generated',
                      labels={'date': 'Date', 'alerts_generated': 'Number of Alerts'})
        fig.update_traces(line_color='#E74C3C', line_width=2)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Guest Experience")
        fig = px.line(visitor_data, x='date', y='satisfaction',
                      title='Visitor Satisfaction Trend',
                      labels={'date': 'Date', 'satisfaction': 'Satisfaction Score'})
        fig.update_traces(line_color='#2ECC71', line_width=2)
        fig.add_hline(y=4.0, line_dash="dash", line_color="orange", 
                      annotation_text="Target (4.0)")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("Agent Activity Summary")

    agent_activity = pd.DataFrame({
        'Agent': ['Conservation', 'Guest Experience', 'Commercial'],
        'Tasks Completed': [1250, 3420, 890],
        'Success Rate': [98.2, 96.5, 94.8]
    })

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(agent_activity, x='Agent', y='Tasks Completed', 
                     title='Tasks by Agent', color='Agent',
                     color_discrete_sequence=['#3498DB', '#2ECC71', '#E74C3C'])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(agent_activity, x='Agent', y='Success Rate', 
                     title='Success Rate by Agent', color='Agent',
                     color_discrete_sequence=['#3498DB', '#2ECC71', '#E74C3C'])
        fig.add_hline(y=95, line_dash="dash", line_color="green")
        st.plotly_chart(fig, use_container_width=True)

# Conservation Agent Dashboard
elif selected_agent == "Conservation Agent":
    st.markdown("## Conservation Agent Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Animals Monitored", "523", "+12")
    with col2:
        st.metric("Active Alerts", "3", "-2")
    with col3:
        st.metric("Avg Response Time", "8.5 min", "-1.2 min")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Recent Alerts")
        alerts = [
            {"animal": "Tiger #205", "condition": "Elevated Heart Rate", "severity": "High", "time": "5 min ago"},
            {"animal": "Elephant #089", "condition": "Low Activity", "severity": "Medium", "time": "12 min ago"},
            {"animal": "Orangutan #167", "condition": "Temperature Anomaly", "severity": "High", "time": "25 min ago"},
            {"animal": "Panda #423", "condition": "Routine Check", "severity": "Resolved", "time": "1 hour ago"},
        ]
        for alert in alerts:
            severity_color = "red" if alert["severity"] == "High" else "orange" if alert["severity"] == "Medium" else "green"
            st.markdown(f'<div class="alert-card"><b>{alert["animal"]}</b><br>{alert["condition"]}<br><span style="color: {severity_color}">{alert["severity"]}</span> • {alert["time"]}</div>', unsafe_allow_html=True)

    with col2:
        st.subheader("Health Metrics")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=conservation_data['date'], y=conservation_data['alerts_generated'],
            mode='lines+markers', name='Alerts',
            line=dict(color='red', width=2), marker=dict(size=6)
        ))
        fig.update_layout(title='Alert Trend (Last 30 Days)', xaxis_title='Date', yaxis_title='Number of Alerts')
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Species Health Status")
    species_health = pd.DataFrame({
        'Species': ['Tiger', 'Elephant', 'Orangutan', 'Panda', 'Dolphin'],
        'Health Score': [94, 97, 91, 88, 96],
        'Risk Level': ['Low', 'Low', 'Medium', 'Medium', 'Low']
    })
    fig = px.bar(species_health, x='Species', y='Health Score', color='Risk Level',
                 color_discrete_map={'Low': '#2ECC71', 'Medium': '#F39C12', 'High': '#E74C3C'})
    fig.add_hline(y=90, line_dash="dash", line_color="green", annotation_text="Target (90%)")
    st.plotly_chart(fig, use_container_width=True)

# Guest Experience Agent Dashboard
elif selected_agent == "Guest Experience Agent":
    st.markdown("## Guest Experience Agent Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Visitors", "15,234", "+892")
    with col2:
        st.metric("Avg Satisfaction", "4.2/5", "+0.3")
    with col3:
        st.metric("Recommendation Rate", "87%", "+5%")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Satisfaction Distribution")
        satisfaction_data = pd.DataFrame({
            'Rating': ['1 Star', '2 Star', '3 Star', '4 Star', '5 Star'],
            'Count': [234, 567, 2341, 5678, 3412]
        })
        fig = px.bar(satisfaction_data, x='Rating', y='Count', title='Visitor Ratings',
                     color_discrete_sequence=['#3498DB'])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Real-time Recommendations")
        recommendations = [
            "VIP Upgrade - 30% discount",
            "Dining Package - $25 value",
            "Photo Pass - Capture memories",
            "Souvenir Bundle - 15% off"
        ]
        for rec in recommendations:
            st.success(rec)

    st.subheader("Visitor Trends")
    fig = px.line(visitor_data, x='date', y='visitors', title='Daily Visitors',
                  labels={'date': 'Date', 'visitors': 'Number of Visitors'})
    fig.update_traces(line_color='#2ECC71', line_width=2, fill='tozeroy', fillcolor='rgba(46,204,113,0.2)')
    st.plotly_chart(fig, use_container_width=True)

# Commercial Agent Dashboard
elif selected_agent == "Commercial Agent":
    st.markdown("## Commercial Agent Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Revenue (MTD)", "$342K", "+12%")
    with col2:
        st.metric("Avg Transaction", "$78.50", "+$5.20")
    with col3:
        st.metric("Conversion Rate", "34%", "+4%")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue by Ticket Type")
        revenue_data = pd.DataFrame({
            'Ticket Type': ['Standard', 'Premium', 'VIP', 'Annual Pass'],
            'Revenue': [125000, 89000, 72000, 56000],
            'Share': [36, 26, 21, 17]
        })
        fig = px.pie(revenue_data, values='Revenue', names='Ticket Type', title='Revenue Distribution',
                     color_discrete_sequence=['#3498DB', '#2ECC71', '#F39C12', '#E74C3C'])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Upsell Opportunities")
        offers = [
            "High Value: VIP Upgrade - Expected uplift: $45",
            "Medium Value: Premium Dining - Expected uplift: $25",
            "Low Value: Snack Combo - Expected uplift: $10"
        ]
        for offer in offers:
            st.info(offer)

    st.subheader("Revenue Trend")
    revenue_trend = pd.DataFrame({
        'date': dates,
        'revenue': np.random.uniform(8000, 15000, 30)
    })
    fig = px.line(revenue_trend, x='date', y='revenue', title='Daily Revenue',
                  labels={'date': 'Date', 'revenue': 'Revenue ($)'})
    fig.update_traces(line_color='#E74C3C', line_width=2)
    st.plotly_chart(fig, use_container_width=True)

# Agent Orchestrator Dashboard
else:
    st.markdown("## Agent Orchestrator")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Agents", "3", "✅")
    with col2:
        st.metric("Tasks Processed", "5,560", "+234")
    with col3:
        st.metric("Workflows Executed", "1,234", "+56")
    with col4:
        st.metric("Avg Response", "1.2s", "-0.3s")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Agent Status")
        agent_status = pd.DataFrame({
            'Agent': ['Conservation', 'Guest Experience', 'Commercial'],
            'Status': ['Active', 'Active', 'Active'],
            'Tasks': [1250, 3420, 890],
            'Last Active': ['Just now', '2 min ago', '5 min ago']
        })
        st.dataframe(agent_status, use_container_width=True)

    with col2:
        st.subheader("Recent Workflows")
        workflows = [
            "Visitor Arrival - Guest + Commercial agents",
            "Health Alert - Conservation agent",
            "Full Sync - All agents",
            "Visitor Arrival - Guest + Commercial agents"
        ]
        for wf in workflows:
            st.code(wf)

    st.subheader("Agent Activity Heatmap")
    activity_data = np.random.rand(3, 7)
    fig = px.imshow(activity_data, 
                    x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                    y=['Conservation', 'Guest Exp', 'Commercial'],
                    title='Agent Activity Heatmap',
                    color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Wildlife Agentic AI Platform | Powered by Snowflake | Responsible AI Framework")
