import streamlit as st
import langchain_helper as lch
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="Please enter the YouTube video URL?",
            max_chars=50
            )
        query = st.sidebar.text_area(
            label="Do you have any questions about the video?",
            max_chars=100,
            key="query"
            )
        openai_api_key = st.sidebar.text_input(
            label="OpenAI API Key",
            key="langchain_search_api_key_openai",
            max_chars=50,
            type="password"
            )
        submit_button = st.form_submit_button(label='Submit')

# once we reeive the query and youtube_url do below
if query and youtube_url:
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    else:
    # call bothe fuxn first create the vector store and then perform similrity search and return the content
        db = lch.create_vector_db(youtube_url)
        response, docs = lch.get_response_from_query(db, query)
        st.subheader("Answer:")
        st.text(textwrap.fill(response, width=85)) # wrap text text so user doesnt scroll