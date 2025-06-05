import streamlit as st
import langchain_helper as langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Select a cuisine type:", ["Arabic", "Italian", "Chinese", "Mexican", "Indian", "American"])




if cuisine:
    result = langchain_helper.generate_restaurant_name_items(cuisine)
    if result and 'restaurant_name' in result and 'menu_items' in result:
        st.header(result['restaurant_name'])
        menu_items = result['menu_items'].split(",")
        st.write("**Menu Items:**")
        for item in menu_items:
            st.write(f"- {item}")
    else:
        st.error("No result returned. Please check langchain_helper.py.")
    # st.write(f"**Restaurant Name:** {result['restaurant_name']}")
    # st.write("**Menu Items:**")
    # for item in result['menu_items']:
    #     st.write(f"- {item}")
# if st.button("Generate"):
#     # Call the restaurant name generation logic here
#     pass
