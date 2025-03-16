import streamlit as st
from function import check_password_strength, generate_strong_password, plot_strength_meter

st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="auto",
)
def main():
    """Streamlit UI for password strength meter"""
st.title("Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)
    st.image(plot_strength_meter(score), use_container_width=True)


    if score == 4:
        st.success("Strong password!")
    elif score == 3:
        st.warning("Good password, but could be stronger.")
    else:
        st.error("Weak password. Please consider the following suggestions:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")

    if st.button("Generate Strong Password"):
        generated_password = generate_strong_password()
        st.session_state["generated_password"] = generated_password
        # st.write(f"Generated Strong Password: {generated_password}")
        # st.image(plot_strength_meter(check_password_strength(generated_password)[0]), use_container_width=True)

        if "generated_password" in st.session_state:
            st.text_input("Your Strong password:",
                          st.session_state["generated_password"],
                          key="generated_password_input")

if __name__ == "__main__":
    main()
