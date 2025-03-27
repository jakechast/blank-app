import streamlit as st

# Page setup
st.set_page_config(page_title="Agentic System Cost Savings Estimator", layout="centered")

st.title("🤖 Agentic System Cost Savings Estimator")
st.caption("Estimate how much your organization can save by automating service desk operations.")

# Sidebar inputs
st.sidebar.header("Adjust Parameters")

total_tickets = st.sidebar.number_input("Total L1 service desk tickets annually", min_value=0, value=2_100_000, step=100_000)
automation_pct = st.sidebar.slider("Percentage of tickets that can be automated (%)", 0, 100, 80)
accuracy_pct = st.sidebar.slider("Agentic System Accuracy (%)", 0, 100, 90)
manual_cost = st.sidebar.slider("Cost per manual ticket (USD)", 0.0, 50.0, 25.0)
automated_cost = st.sidebar.slider("Cost per automated ticket (USD)", 0.0, 5.0, 2.5)
rollout_cost = st.sidebar.slider("Annual rollout & infra cost (USD)", 0.0, 10_000_000.0, 5_000_000.0)

# Calculations
automatable_tickets = total_tickets * (automation_pct / 100)
successful_automated = automatable_tickets * (accuracy_pct / 100)
failed_automated = automatable_tickets - successful_automated

# Cost calculations
manual_total = automatable_tickets * manual_cost
successful_cost = successful_automated * automated_cost
fallback_cost = failed_automated * manual_cost
new_automated_total = successful_cost + fallback_cost

# Savings
gross_savings = manual_total - new_automated_total
net_savings = gross_savings - rollout_cost

# Results
st.subheader("Results 💰")
st.metric("Automatable Tickets", f"{automatable_tickets:,.0f}")
st.metric("Manual Handling Cost (Before Automation)", f"${manual_total:,.2f}")
st.metric("Adjusted Automation Cost (with Accuracy)", f"${new_automated_total:,.2f}")
st.metric("Gross Savings (Before Rollout Cost)", f"${gross_savings:,.2f}")
st.metric("Estimated Net Annual Savings", f"${net_savings:,.2f}")

# Optional: Add a note
st.caption("Note: Inaccurately resolved tickets are assumed to fall back to manual resolution at full cost.")
