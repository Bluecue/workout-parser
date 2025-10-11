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
    "midback": "Midback", "mid back": "Midback",
}
valid_muscles = set(normalize.values())

raw_text = st.text_area("Paste your workout log here:")

if st.button("Process"):
    muscle_totals = defaultdict(float)

    # Regex matches both "3 x biceps" and "biceps x 3"
    pattern = re.compile(
        r"(?:(\d+(?:\.\d+)?)\s*[xX:]\s*([a-zA-Z ]+)$|^([a-zA-Z ]+)\s*[xX:]\s*(\d+(?:\.\d+)?)$)"
    )

    for line in raw_text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = pattern.match(line)
        if match:
            if match.group(1):  # number first
                sets = float(match.group(1))
                muscle_key = match.group(2).strip().lower()
            else:  # muscle first
                muscle_key = match.group(3).strip().lower()
                sets = float(match.group(4))
            muscle = normalize.get(muscle_key)
            if muscle and muscle in valid_muscles:
                muscle_totals[muscle] += sets

    st.subheader("Muscle Summary")
    if muscle_totals:
        for muscle, total in sorted(muscle_totals.items()):
            st.write(f"**{muscle}** x {total}")
    else:
        st.info("No muscle data found. Make sure your lines look like `3 x biceps` or `front delts x 3`.")
