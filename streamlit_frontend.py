import streamlit as st
from streamlit_option_menu import option_menu
from image_gen import image_generator
from image_to_text import img2txt
from io import BytesIO
from metaphor_api import shop_link_metaphor_api
import pandas as pd
from marketplace_filter import user_desired_marketplaces

#Header
st.header("Shopping Assistant Using Metaphor API")
# Initialize session state
if 'shopping_prompt' not in st.session_state:
    st.session_state.shopping_prompt = None

if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = 2
    manual_select = 2
else:
    manual_select = None

def make_clickable(link):
    text = link.split('/')[-1]  # Extract the last part of the URL as text
    return f'<a target="_blank" href="{link}">{text}</a>'

selected = option_menu(
            menu_title=None,  
            options=["Upload Image", "Generate Image", "Shopping Links"], 
            icons=["upload", "hammer", "shop"], 
            menu_icon="cast", 
            default_index=0,  
            orientation="horizontal",
            manual_select=manual_select, key='menu_4'
        )

if selected == "Upload Image":
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        shopping_prompt = img2txt(uploaded_image)
        if shopping_prompt:
            st.button(f"Get Shopping Links", key='switch_button')
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            # Store shopping_prompt in session state
            st.session_state.shopping_prompt = shopping_prompt

if selected == "Generate Image":
    user_input = st.text_input("Enter Prompt:")
    generate_button = st.button("Generate")
    if generate_button and user_input != "":
        generated_image = image_generator(user_input)
        generated_image = BytesIO(generated_image)
        shopping_prompt = img2txt(generated_image)
        if shopping_prompt:
            st.button(f"Get Shopping Links", key='switch_button')
            st.image(generated_image, caption="Generated Image", use_column_width=True)
            # Store shopping_prompt in session state
            st.session_state.shopping_prompt = shopping_prompt

if selected == "Shopping Links":
    if st.session_state.shopping_prompt:
        st.subheader(f"Here Are your Products related to {st.session_state.shopping_prompt}")
        user_input = st.text_input("Filter by Marketplace")
        if  user_input:
            domains = user_desired_marketplaces(user_input)
            shopping_links = shop_link_metaphor_api(st.session_state.shopping_prompt,domains)
        else:
            shopping_links = shop_link_metaphor_api(st.session_state.shopping_prompt,["www.amazon.com"])
        df = pd.DataFrame(shopping_links, columns=["Product Name", "Link"])
        df['Link'] = df['Link'].apply(make_clickable)

        # Convert the DataFrame to an HTML table with CSS styling
        html_table = df.to_html(escape=False, index=False, classes=["styled-table"])

        # Apply custom CSS to style the table
        custom_css = """
            <style>
                .styled-table {
                    width: 100%;
                    border-collapse: collapse;
                    overflow: hidden;
                }
                .styled-table th,
                .styled-table td {
                    padding: 12px 15px;
                    text-align: left;
                }
                /* Add more CSS styling as needed */
            </style>
        """

        # Display the HTML table with custom CSS
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown(html_table, unsafe_allow_html=True)

