import streamlit as st
import google.generativeai as genai
# Add this at the beginning of your script
st.set_page_config(layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Create a container for the rectangle
rectangle_container = st.container()

# Create two columns, one for the main content and one for the rectangle
main_col, rectangle_col = st.columns([3, 1])

with rectangle_col:
    # Add the 300x300 pixel rectangle
    rectangle_container.markdown(
        """
        <div style="width: 0px; height: 0px; background-color: #f0f0f0; border: 1px solid #ccc; position: fixed; top: 0; right: 0; z-index: 1000;">
        </div>
        """,
        unsafe_allow_html=True
    )

api_key= st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

persona = """
        You are Hoken Tech AI bot. You help people answer questions about your self (i.e Hoken Tech)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Hoken Tech 
        At Hoken Tech, our brand mission is to connect brands to people through authentic Italian NFTs, we understand the profound power of art and creativity, and how it can make a significant impact on businesses, regardless of their size, we recognized a recurring issue in the digital landscape - the absence of web3 products.
        Many artists, creators, and small to medium-sized companies were finding it challenging to navigate this new digital terrain, that's where we come in.
        Our dedicated team at Hoken Tech is committed to providing a tailor-made web3 turnkey solution that bridges the gap between brands and people, we firmly believe that every brand, irrespective of its scale, deserves the opportunity to engage with its audience in an innovative and meaningful manner.
        By harnessing the capabilities of the world's first carbon-neutral blockchain, we empower artists, creators, and even small to medium-sized businesses to showcase their work and seamlessly connect with their target markets, our web3 turnkey solution is designed with simplicity in mind, making it accessible for everyone.
        We place immense importance on building authentic connections and cultivating creativity, at Hoken Tech, we strive to create a supportive and inclusive environment where artists, creators, and brands can flourish, we are here to guide you through the captivating world of web3 and equip you with the necessary tools to unlock your full potential.
        Join us at Hoken Tech and let's revolutionize the way brands and people connect through Italian NFTs, together, we have the power to create an unforgettable digital experience that will leave a lasting impact on your brand.
        Welcome to the future of brand engagement with Hoken Tech!
              
        Hoken Tech's Youtube Channel: http://www.youtube.com/channel/UCU3PG-j_Venl0OvxrwEnPKw
        Hoken Tech's Email: hokentechitalia@gmail.com 
        Hoken Tech's Facebook: https://www.facebook.com/hokentechitalia/
        Hoken Tech's Instagram: https://www.instagram.com/hokentechitalia/
        """




st.title("Hoken Tech's AI Bot")
question = st.text_input("Ask anything about us")
if st.button("ASK",use_container_width=400):
    with st.spinner("Thinking..."):
        prompt = "Here is the question that the user asked: " +question
        response = model.generate_content(persona + prompt)
        st.write(response.text)
st.write("")  # Add a single line of space
