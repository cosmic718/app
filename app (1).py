import streamlit as st

# --- Core Data (from your notebook) ---
mama = 39
baba = 40
dadi = 80
saad = 11
Faris = 6
Asim = 4

# --- Streamlit App UI ---
st.set_page_config(layout="centered", page_title="Interactive Family Data App")

st.title("--- Interactive Storage App Menu ---")

st.markdown("--- --- --- --- --- --- --- --- --- --- ")

# Layout for buttons
col1, col2 = st.columns(2)

with col1:
    if st.button('Display Ages', help='Click to see ages'):

        st.subheader("Family Ages:")
        # Display ages in the requested format and order with HTML styling
        html_output = f'''
            <p style="font-size: 16px; color: #0056b3;"><b>Baba</b> = {baba}</p>
            <p style="font-size: 16px; color: #0056b3;"><b>Mama</b> = {mama}</p>
            <p style="font-size: 16px; color: #0056b3;"><b>Dadi</b> = {dadi}</p>
            <p style="font-size: 16px; color: #0056b3;"><b>Saad</b> = {saad}</p>
            <p style="font-size: 16px; color: #0056b3;"><b>Faris</b> = {Faris}</p>
            <p style="font-size: 16px; color: #0056b3;"><b>Asim</b> = {Asim}</p>
        '''
        st.markdown(html_output, unsafe_allow_html=True)

with col2:
    if st.button('Display family members', help='Click to see family members')
        st.subheader("Family Members:")
        html_output = '''
            <ol style="font-size: 16px; color: #5cb85c;">
                <li><b>Saad</b></li>
                <li><b>Faris</b></li>
                <li><b>Asim</b></li>
                <li><b>Baba</b></li>
                <li><b>Mama</b></li>
                <li><b>Dadi</b></li>
            </ol>
        '''
        st.markdown(html_output, unsafe_allow_html=True)
