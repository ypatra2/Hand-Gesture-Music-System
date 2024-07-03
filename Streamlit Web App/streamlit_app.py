import streamlit as st
import openai
import subprocess
import sys
import signal
import os

# Define the list of instruments to choose from
instruments = ['Guitar', 'Piano', 'Violin', 'Saxophone', 'Trumpet', 'Saxophone', 'Horn', 'Cello']

# Define the function to get the description of the instrument
def get_instrument_description(instrument):

    openai.api_key = "<ENTER OPENAI KEY>" ##new API Key from verja72

    response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=f"Can you give me a 100 word summarry on the instrument {instrument},"
                f"as if you were explaining it to a 10-year old to spike their interest in music.",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    # response = OpenAI.completions(json={"model": "text-davinci-003",
    #                                     "prompt": f"Can you give me a 100 word summary on the instrument {instrument}?"})

    return response["choices"][0]["text"].strip()

# Define the Streamlit app
def main():
    # Set the title of the app
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    st.title('Music Instruments Learning App')
    col1, col2, col3 = st.columns(3)

    with col1:
        # Add a dropdown to select the instrument
        selected_option = st.session_state.selected_option = st.selectbox('Select an instrument', instruments)
        instrument = st.session_state.selected_option

        # Get the description of the instrument using the OpenAI API
        description = get_instrument_description(instrument)

    with col2:

        # Display the picture and description of the instrument
        st.image(f'Instrument Images/{instrument}.jpg', use_column_width=True)

    with col3:
        ## Sample testing for Violin Instrument - Use Synthesia API Subscription to enter ChatGPT response to be converted into Synthesia AI Avatar Video
        st.markdown("""
        <style>
        .big-font {
            font-size:25px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown("""<div style="position: relative; overflow: hidden; padding-top: 56.25%;"><iframe src="https://share.synthesia.io/embeds/videos/720df568-8cf2-4612-beae-fcfdffe8e2b8" loading="lazy" title="Synthesia video player - Your AI video" allow="encrypted-media; fullscreen;" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0; margin: 0; overflow:hidden;"></iframe></div>
        """, unsafe_allow_html=True)
        st.markdown(f'<p cmelass="big-font"> {description} !!</p>', unsafe_allow_html=True)

    with col2:
        # Add a button to run the project_run.py file to initiate hand tracking to play the instrument
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)
        if st.button("LET'S HAVE SOME FUN!"):
            # Start the process
            p = subprocess.Popen("exec " + f"python project_run.py {st.session_state.selected_option}", stdout=subprocess.PIPE, shell=True)
            p.kill()
            subprocess.run(['python', 'project_run.py', instrument])


if __name__ == '__main__':
    main()
