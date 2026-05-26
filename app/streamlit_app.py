import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import sys
import os

from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Path setup

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from preprocessing import clean_text
from theme_analysis import (
    detect_themes,
    analyze_aspects
)

# Page config

st.set_page_config(
    page_title="AI Sentiment Dashboard",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS

st.markdown("""
<style>

.main {
    background-color: #0b1020;
    color: white;
}

.stTextArea textarea {
    background-color: #1c1c3a;
    color: white;
    border-radius: 15px;
    font-size: 22px;
}

.stButton button {
    background-color: #1f2937;
    color: white;
    border-radius: 15px;
    padding: 12px 25px;
    font-size: 20px;
    border: 1px solid #4b5563;
}

.stButton button:hover {
    border: 1px solid #60a5fa;
    color: #60a5fa;
}

</style>
""", unsafe_allow_html=True)

# Sidebar

st.sidebar.title(
    "🧠 AI Dashboard"
)

st.sidebar.markdown("---")

st.sidebar.subheader(
    "Features"
)

st.sidebar.markdown(
    """
    ✔ Hinglish Sentiment Analysis
    
    ✔ Theme Detection
    
    ✔ Aspect Sentiment Analysis
    
    ✔ Batch CSV Analytics
    
    ✔ Word Cloud Visualization
    
    ✔ KPI Dashboard
    
    ✔ Downloadable Reports
    """
)

st.sidebar.markdown("---")

st.sidebar.subheader(
    "Tech Stack"
)

st.sidebar.markdown(
    """
    - Python
    
    - Streamlit
    
    - NLP
    
    - VADER
    
    - Pandas
    
    - Plotly
    
    - WordCloud
    """
)

st.sidebar.markdown("---")

st.sidebar.info(
    "AI-Powered Social Media Intelligence Dashboard"
)

# Title

st.title(
    "🧠 AI-Powered Hinglish Sentiment Intelligence Dashboard"
)

st.write(
    "Analyze sentiment using NLP, VADER, theme detection, aspect analysis, and batch analytics."
)

# Session state

if "user_text" not in st.session_state:

    st.session_state.user_text = ""

# Sample buttons

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("This movie was amazing"):

        st.session_state.user_text = (
            "This movie was amazing"
        )

with col2:

    if st.button("Service was terrible and slow"):

        st.session_state.user_text = (
            "Service was terrible and slow"
        )

with col3:

    if st.button("The event was okay"):

        st.session_state.user_text = (
            "The event was okay"
        )

# User input

user_input = st.text_area(

    "Enter Text",

    value=st.session_state.user_text,

    height=220
)

# CSV upload

uploaded_file = st.file_uploader(

    "Upload CSV File",

    type=["csv"]
)

# Sentiment analyzer

analyzer = SentimentIntensityAnalyzer()

# Dashboard tabs

tab1, tab2, tab3 = st.tabs([

    "📊 Single Analysis",

    "📁 Batch Analysis",

    "ℹ About Project"
])


# Single Analysis Tab


with tab1:

    if st.button("Analyze Sentiment"):

        if user_input.strip() != "":

            # Clean text

            cleaned_text = clean_text(
                user_input
            )

            # Theme detection

            detected_themes = detect_themes(
                cleaned_text
            )

            # Aspect analysis

            aspect_results = analyze_aspects(

                cleaned_text,

                detected_themes
            )

            # Sentiment scores

            scores = analyzer.polarity_scores(
                cleaned_text
            )

            compound = scores['compound']

            # Sentiment logic

            if compound >= 0.20:

                sentiment = "Positive"

                emoji = "😊"

                card_color = "#064e3b"

            elif compound <= -0.20:

                sentiment = "Negative"

                emoji = "😠"

                card_color = "#4c1d1d"

            else:

                sentiment = "Neutral"

                emoji = "😐"

                card_color = "#3f3f0f"

            # Prediction card

            st.subheader("Prediction")

            st.markdown(

                f"""
                <div style="
                    background:{card_color};
                    padding:40px;
                    border-radius:25px;
                    text-align:center;
                    font-size:60px;
                    font-weight:bold;
                    color:white;
                    border-left:10px solid #ffdd00;
                ">
                    {sentiment} {emoji}
                </div>
                """,

                unsafe_allow_html=True
            )

            # Sentiment strength

            st.subheader(
                "Sentiment Strength"
            )

            compound_percentage = round(

                abs(compound) * 100,

                2
            )

            if sentiment == "Positive":

                st.write(

                    f"Positive Confidence — {compound_percentage}%"
                )

                st.progress(
                    min(abs(compound), 1.0)
                )

            elif sentiment == "Negative":

                st.write(

                    f"Negative Confidence — {compound_percentage}%"
                )

                st.progress(
                    min(abs(compound), 1.0)
                )

            else:

                st.write(

                    f"Neutral Confidence — {scores['neu'] * 100:.2f}%"
                )

                st.progress(
                    min(scores['neu'], 1.0)
                )

            # Detected themes

            st.subheader(
                "Detected Themes"
            )

            if detected_themes:

                for theme, keywords in (

                    detected_themes.items()
                ):

                    st.success(theme)

                    st.write(
                        "Keywords Detected:"
                    )

                    for keyword in keywords:

                        st.markdown(
                            f"- {keyword}"
                        )

            else:

                st.info(
                    "No specific themes detected."
                )

            # Aspect sentiment analysis

            st.subheader(
                "Aspect Sentiment Analysis"
            )

            if aspect_results:

                for aspect, sentiment_value in (

                    aspect_results.items()
                ):

                    if sentiment_value == "Positive":

                        st.success(
                            f"{aspect} → Positive 😊"
                        )

                    elif sentiment_value == "Negative":

                        st.error(
                            f"{aspect} → Negative 😠"
                        )

                    else:

                        st.warning(
                            f"{aspect} → Neutral 😐"
                        )

            else:

                st.info(
                    "No aspect sentiment detected."
                )

            # Sentiment analytics

            st.subheader(
                "Sentiment Analytics"
            )

            chart_data = pd.DataFrame({

                "Sentiment": [

                    "Positive",

                    "Neutral",

                    "Negative"
                ],

                "Score": [

                    scores['pos'] * 100,

                    scores['neu'] * 100,

                    scores['neg'] * 100
                ]
            })

            # Bar chart

            bar_fig = px.bar(

                chart_data,

                x="Sentiment",

                y="Score",

                color="Sentiment",

                title="Sentiment Distribution",

                text_auto=".2f"
            )

            st.plotly_chart(

                bar_fig,

                use_container_width=True
            )

            # Pie chart

            pie_fig = px.pie(

                chart_data,

                names="Sentiment",

                values="Score",

                title="Sentiment Breakdown"
            )

            st.plotly_chart(

                pie_fig,

                use_container_width=True
            )

            # Word cloud

            st.subheader(
                "Word Cloud"
            )

            wordcloud = WordCloud(

                width=1000,

                height=500,

                background_color="black",

                colormap="viridis"

            ).generate(cleaned_text)

            fig, ax = plt.subplots(
                figsize=(12, 6)
            )

            ax.imshow(

                wordcloud,

                interpolation="bilinear"
            )

            ax.axis("off")

            st.pyplot(fig)

            # NLP preprocessing preview

            st.subheader(
                "NLP Preprocessing Preview"
            )

            st.code(cleaned_text)

            # Text analytics

            st.subheader(
                "Text Analytics"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(

                    label="Original Words",

                    value=len(
                        user_input.split()
                    )
                )

            with col2:

                st.metric(

                    label="Cleaned Words",

                    value=len(
                        cleaned_text.split()
                    )
                )

        else:

            st.warning(
                "Please enter some text."
            )


# Batch Analysis Tab


with tab2:

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Dataset")

        st.dataframe(df.head())

        # Validate column

        if "text" not in df.columns:

            st.error(
                "CSV must contain a column named 'text'"
            )

        else:

            # Storage lists

            sentiments = []

            compound_scores = []

            positive_scores = []

            neutral_scores = []

            negative_scores = []

            theme_results = []

            # Process dataset

            for text in df["text"]:

                cleaned = clean_text(
                    str(text)
                )

                # Sentiment scores

                scores = analyzer.polarity_scores(
                    cleaned
                )

                compound = scores['compound']

                # Sentiment prediction

                if compound >= 0.20:

                    sentiment = "Positive"

                elif compound <= -0.20:

                    sentiment = "Negative"

                else:

                    sentiment = "Neutral"

                sentiments.append(sentiment)

                # Store analytics

                compound_scores.append(
                    round(compound, 3)
                )

                positive_scores.append(
                    round(scores['pos'] * 100, 2)
                )

                neutral_scores.append(
                    round(scores['neu'] * 100, 2)
                )

                negative_scores.append(
                    round(scores['neg'] * 100, 2)
                )

                # Theme detection

                detected = detect_themes(
                    cleaned
                )

                if detected:

                    theme_names = ", ".join(
                        detected.keys()
                    )

                else:

                    theme_names = "None"

                theme_results.append(
                    theme_names
                )

            # Add dataframe columns

            df["Predicted Sentiment"] = sentiments

            df["Compound Score"] = compound_scores

            df["Positive %"] = positive_scores

            df["Neutral %"] = neutral_scores

            df["Negative %"] = negative_scores

            df["Themes"] = theme_results

            # Show results

            st.subheader(
                "Batch Analysis Results"
            )

            st.dataframe(df)

            # Download CSV

            csv = df.to_csv(
                index=False
            ).encode('utf-8')

            st.download_button(

                label="Download Processed CSV",

                data=csv,

                file_name=(
                    "processed_sentiment_analysis.csv"
                ),

                mime="text/csv"
            )

            # KPI cards

            total_reviews = len(df)

            positive_count = (
                df["Predicted Sentiment"]
                .value_counts()
                .get("Positive", 0)
            )

            negative_count = (
                df["Predicted Sentiment"]
                .value_counts()
                .get("Negative", 0)
            )

            neutral_count = (
                df["Predicted Sentiment"]
                .value_counts()
                .get("Neutral", 0)
            )

            st.subheader(
                "Dataset Overview"
            )

            kpi1, kpi2, kpi3, kpi4 = st.columns(4)

            with kpi1:

                st.metric(

                    label="Total Reviews",

                    value=total_reviews
                )

            with kpi2:

                st.metric(

                    label="Positive",

                    value=positive_count
                )

            with kpi3:

                st.metric(

                    label="Negative",

                    value=negative_count
                )

            with kpi4:

                st.metric(

                    label="Neutral",

                    value=neutral_count
                )

            # Batch sentiment analytics

            sentiment_counts = (

                df["Predicted Sentiment"]

                .value_counts()

                .reset_index()
            )

            sentiment_counts.columns = [

                "Sentiment",

                "Count"
            ]

            st.subheader(
                "Batch Sentiment Analytics"
            )

            batch_fig = px.bar(

                sentiment_counts,

                x="Sentiment",

                y="Count",

                color="Sentiment",

                title=(
                    "Batch Sentiment Distribution"
                ),

                text_auto=True
            )

            st.plotly_chart(

                batch_fig,

                use_container_width=True
            )

            # Theme analytics

            all_themes = []

            for themes in theme_results:

                if themes != "None":

                    split_themes = themes.split(", ")

                    all_themes.extend(
                        split_themes
                    )

            if all_themes:

                theme_df = pd.DataFrame({

                    "Theme": all_themes
                })

                theme_counts = (

                    theme_df["Theme"]

                    .value_counts()

                    .reset_index()
                )

                theme_counts.columns = [

                    "Theme",

                    "Count"
                ]

                st.subheader(
                    "Theme Analytics"
                )

                st.dataframe(theme_counts)

                theme_fig = px.bar(

                    theme_counts,

                    x="Theme",

                    y="Count",

                    color="Theme",

                    title="Theme Distribution",

                    text_auto=True
                )

                st.plotly_chart(

                    theme_fig,

                    use_container_width=True
                )


# About Project Tab


with tab3:

    st.title(
        "ℹ About This Project"
    )

    st.markdown(
        """
        # AI-Powered Hinglish Sentiment Intelligence Dashboard

        This project is an advanced NLP-based analytics dashboard
        designed for sentiment analysis, theme detection,
        aspect-based analysis, and batch analytics.

        ## Key Features

        - Hinglish Sentiment Analysis
        
        - Theme Detection
        
        - Aspect-Based Sentiment Analysis
        
        - Batch CSV Processing
        
        - Word Cloud Visualization
        
        - KPI Dashboard
        
        - Downloadable Analytics Reports
        
        - Interactive Charts

        ### Technologies Used

        - Python
        
        - Streamlit
        
        - NLP
        
        - VADER
        
        - Pandas
        
        - Plotly
        
        - WordCloud

        ### Use Cases

        - Social Media Monitoring
        
        - Review Analysis
        
        - Public Opinion Mining
        
        - Customer Feedback Analytics
        
        - Brand Sentiment Tracking
        """
    )