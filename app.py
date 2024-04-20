import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("video_subtitles.csv")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #1e3d59; /* Custom color for heading */
        margin-bottom: 20px;
    }
    .search-box {
        width: 90%; /* Adjust width of text input */
        margin-bottom: 20px;
    }
    .search-btn {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-left: auto; /* Center align search button */
        margin-right: auto;
        display: block;
    }
    .search-btn:hover {
        background-color: #45a049;
    }
    .results {
        margin-top: 20px;
    }
    .result-item {
        font-size: 18px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.markdown("<h1 class='title'>Search Engine based on Movie Subtitle</h1>", unsafe_allow_html=True)

# User input for search query
user_input = st.text_input("Enter Query", key="search-box")  # Adjusted text input size

# Button to trigger search
button_clicked = st.button("Search", key="search-btn")  # Center aligned search button
if button_clicked:
    with st.spinner('Loading Movies...'):
        # Filter results based on user input
        results = df[df['content_clean'].str.contains(user_input, case=False)]['name'].tolist()
    
        # Display search results
        if len(results) == 0:
            st.warning("No results found.")
        else:
            st.success("Top Results of your Query:")
            # Display each result as a list item
            for result in results[:10]:
                st.markdown(f"<p class='result-item'>{result}</p>", unsafe_allow_html=True)
