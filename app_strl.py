from myfunction_65130701726 import get_movie_recommendations
import streamlit as st
import pandas as pd
import pickle

# Load your data
with open('recommendation_data_65130701726.pkl', 'rb') as file:
    user_similarity_df, user_movie_ratings = pickle.load(file)


# Streamlit app
def main():
    st.title("Movie Recommendation")

    # User input
    user_id = st.number_input("Enter User ID:", min_value=0, max_value=user_similarity_df.shape[0]-1, value=0)
    n_recommendations = st.slider("Number of Recommendations:", min_value=1, max_value=10, value=5)

    # Generate recommendations on button click
    if st.button("Get Recommendations"):
        if user_id in user_similarity_df.index: 
            recommendations = get_movie_recommendations(user_id, user_similarity_df, user_movie_ratings, n_recommendations)
            st.write(f"Top {n_recommendations} Movie Recommendations for User {user_id}:", recommendations)
        else: 
            st.write(f" Movie Recommendations for User {user_id}: is not available.")

if __name__ == '__main__':
    main()
