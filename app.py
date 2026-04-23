import streamlit as st
from apis import note_generator, audio_transcription, quiz_generator
from PIL import Image


st.set_page_config(
    page_title="Image to text",
    page_icon="🚀",
    layout="wide"
)

#title
st.title("Image to text Tool By Ridoy Islam")
st.markdown("Upload upto 3 images to generate Note summary")
st.divider()


#sidebar

with st.sidebar:
    st.header("Controls")

    images = st.file_uploader("Upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True)
    
    pil_images =[]

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

        if images:
            if len(images)>3:
                st.error("Upload at max 3 images")
            else:
                st.subheader("Uploaded images")
            
            col = st.columns(len(images))

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    #difficulty 
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index = None
    )

    pressed= st.button("Click the button to initiate AI",type="primary")

if pressed: 
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty")
    if images and selected_option:
        #note 
        with st.container(border=True):
            st.subheader("Your note")
            #the portion below will be replaced by API Call

            with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pil_images)
                st.text(generated_notes)


        
         #Audio transcipt
        with st.container(border=True):
            st.subheader("Audio Transcription")
            with st.spinner("AI is generating audio for you"):
                generated_audio = audio_transcription(generated_notes)
                st.audio(generated_audio)

        #quiz

        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")

            with st.spinner("AI is generating Quiz for you"):
                generated_quiz = quiz_generator(pil_images, selected_option)
                st.markdown(generated_quiz)