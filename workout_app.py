import streamlit as st
import re
from collections import defaultdict

# Normalization dictionary
normalize = {
    "hams": "Hamstrings", "hamstrings": "Hamstrings", "hamstring": "Hamstrings",
    "glutes": "Glutes", "glute": "Glutes",
    "quads": "Quadriceps", "quad": "Quadriceps",
    "rear delt": "Rear Delts", "rear delts": "Rear Delts",
    "side delt": "Side Delts", "side delts": "Side Delts",
    "front delt": "Front Delts", "front delts": "Front Delts",
    "biceps": "Biceps", "triceps": "Triceps",
    "calves": "Calves", "calf": "Calves",
    "chest": "Chest", "pecs": "Chest", "pec": "Chest",
    "lats": "Lats", "lat": "Lats",
    "traps": "Trapezius", "trap": "Trapezius",
    "forearm": "Forearms", "forearms": "Forearms",
    "abs": "Abdominals", "core": "Abdominals",
    "midback": "Midback", "midback": "Mid back",
}

st.title("🏋️ Workout Log Parser")

raw_text = st.text_area("Paste your workout log here:")

if st.button("Process"):
    muscle_totals = defaultdict(float)
    pattern = re.compile(r"([\d\.]+)\s*x\s*(.+)", re.I)

    for line in raw_text.splitlines():
        match = pattern.match(line.strip())
        if match:
            sets = float(match.group(1))
            muscle = match.group(2).lower().strip()
            muscle = normalize.get(muscle, muscle.title())
            muscle_totals[muscle] += sets

    st.subheader("Muscle Summary")
    if muscle_totals:
        for muscle, total in sorted(muscle_totals.items()):
            st.write(f"**{muscle}**: {total}")
    else:
        st.info("No muscle data found. Make sure your lines look like `3 x biceps` or `1.5 x glutes`.")

