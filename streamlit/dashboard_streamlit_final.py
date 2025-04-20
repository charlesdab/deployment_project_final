
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="📊 Retards Getaround", layout="wide")
st.title("📊 Analyse des retards sur Getaround")

@st.cache_data
def load_data():
    df = pd.read_excel("get_around_delay_analysis.xlsx")
    df = df[df["state"] == "ended"]
    df = df[df["delay_at_checkout_in_minutes"].between(-500, 1500)]
    df["delay_status"] = df["delay_at_checkout_in_minutes"].apply(
        lambda x: "early" if x < 0 else ("on_time" if x == 0 else "late")
    )
    return df

df = load_data()

st.markdown("### 🎯 Objectif du dashboard")
st.info(
    "Ce tableau de bord aide l'équipe produit à comprendre les retards, "
    "leur impact sur les locations suivantes et à simuler l'effet d'un seuil de sécurité entre deux locations."
)

# Statistiques globales
st.markdown("### 📈 Statistiques globales")
col1, col2, col3 = st.columns(3)
col1.metric("Locations analysées", len(df))
col2.metric("Retards observés", (df["delay_status"] == "late").sum())
col3.metric("Taux de retards", f"{(df['delay_status'] == 'late').mean():.1%}")

# Slider de seuil
st.markdown("### 🛡️ Simulation d'un seuil de sécurité")
seuil = st.slider("Définir un seuil minimum (en minutes) entre deux locations :", min_value=0, max_value=600, value=120, step=15)

df_valid = df.dropna(subset=["time_delta_with_previous_rental_in_minutes"])
df_problematic = df_valid[
    (df_valid["delay_at_checkout_in_minutes"] > 0) &
    (df_valid["time_delta_with_previous_rental_in_minutes"] < df_valid["delay_at_checkout_in_minutes"])
]

df_evitable = df_valid[
    (df_valid["delay_at_checkout_in_minutes"] > 0) &
    (df_valid["time_delta_with_previous_rental_in_minutes"] < seuil)
]

st.markdown(f"💥 Cas réellement problématiques observés : **{len(df_problematic)}**")
st.markdown(f"✅ Cas qui **auraient pu être évités** avec un seuil de **{seuil} min** : **{len(df_evitable)}**")

# Histogramme des retards
st.markdown("### ⏱️ Distribution des retards")
fig1, ax1 = plt.subplots()
sns.histplot(df["delay_at_checkout_in_minutes"], bins=80, kde=True, color="cornflowerblue", ax=ax1)
ax1.set_title("Distribution des retards à la restitution (minutes)")
ax1.set_xlim(-100, 500)
st.pyplot(fig1)

# Boxplot par type de check-in
st.markdown("### 📦 Retards par type de check-in")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x="checkin_type", y="delay_at_checkout_in_minutes", ax=ax2, palette="Set2")
ax2.set_ylim(-100, 500)
st.pyplot(fig2)

# Scatterplot temps libre vs retard
st.markdown("### 🔁 Temps libre vs retard")
fig3, ax3 = plt.subplots()
sns.scatterplot(
    data=df_valid,
    x="time_delta_with_previous_rental_in_minutes",
    y="delay_at_checkout_in_minutes",
    hue="checkin_type",
    alpha=0.4,
    ax=ax3
)
ax3.set_xlim(0, 600)
ax3.set_ylim(-100, 500)
ax3.axvline(x=seuil, color="red", linestyle="--", label=f"Seuil = {seuil} min")
ax3.legend()
st.pyplot(fig3)

st.success("Dashboard généré avec succès. Modifiez le seuil pour simuler les effets produit.")
