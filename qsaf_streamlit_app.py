
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="QSAF Scoring App", layout="wide")
st.title("🔐 QSAF Scoring App – Full Framework")

# Load QSAF Controls
with open("qsaf_controls_all_domains.json", "r") as f:
    qsaf_domains = json.load(f)

# Domain Selector
domain = st.selectbox("Select QSAF Domain", list(qsaf_domains.keys()))

controls = qsaf_domains[domain]
results = []

st.markdown(f"## Controls in {domain}")

for cid, desc in controls:
    st.subheader(f"{cid}: {desc}")
    col1, col2, col3, col4 = st.columns(4)
    cia = col1.slider(f"CIA Impact – {cid}", 0, 10, 5)
    expl = col2.slider(f"Exploitability – {cid}", 0, 10, 5)
    reach = col3.slider(f"Reachability – {cid}", 0, 10, 5)
    gap = col4.slider(f"Gap Score – {cid}", 0, 5, 3)

    risk_score = round((cia + expl + reach) / 3, 2)

    results.append({
        "Control ID": cid,
        "Description": desc,
        "CIA Impact": cia,
        "Exploitability": expl,
        "Reachability": reach,
        "Risk Score": risk_score,
        "Gap Score": gap
    })

# Show results
st.markdown("## 📊 Scoring Summary")
df = pd.DataFrame(results)
st.dataframe(df)

# Export results as CSV
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download CSV", csv, "qsaf_scores.csv", "text/csv")
