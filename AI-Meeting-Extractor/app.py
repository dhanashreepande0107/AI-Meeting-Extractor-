import streamlit as st
import pandas as pd
from extractor import extract_action_items

st.title("🤖 AI Meeting Action-Item Extractor")

# Step 8 - Upload Transcript File
uploaded_file = st.file_uploader(
    "Upload Meeting Transcript (.txt)",
    type=["txt"]
)

if uploaded_file:
    transcript = uploaded_file.read().decode("utf-8")
else:
    transcript = ""

# Text Area
transcript = st.text_area(
    "Paste Meeting Transcript",
    transcript,
    height=250
)

# Extract Button
if st.button("Extract Action Items"):

    results = extract_action_items(transcript)

    if results:
        df = pd.DataFrame(results)

        # Display Results
        st.dataframe(df, use_container_width=True)

        # Step 9 - Download CSV
        csv = df.to_csv(index=False)

        st.download_button(
            label="📥 Download Results",
            data=csv,
            file_name="action_items.csv",
            mime="text/csv"
        )

    else:
        st.warning("No action items found.")