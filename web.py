import streamlit as st

# Set the title of the web page
st.title("Biography")

# Editable Section for Name
name = st.text_input("Enter Your Name", "Anera Q. Gilles")

# Editable Section for Introduction Text
about_me = st.text_area("Tell us about yourself", """
   Hello! I am a first-year college student, 
   eager to explore the vast world of higher education 
   and all the opportunities it brings. 
   I am currently taking courses in various fields to broaden my knowledge and skills.
   My academic interests lie in understanding fundamental concepts
   across different disciplines, from social sciences to natural sciences, 
   and everything in between. I am passionate about learning and actively participating in my classes, 
   engaging with my peers, and contributing to campus life. As I navigate this exciting new chapter, 
   I am committed to making the most of my college experience, balancing academics with personal growth, 
   and building a strong foundation for my future career. 
   I am excited to absorb as much knowledge as possible and apply it to real-world situations.
""")

# Editable Section for Education
education = st.text_area("Education", """
    - Cantapoy Elementary School,(2012 - 2018)
    - Malimono National High School,(2022 - 2024)
    - Bachelor of Science in Computer Engineering, SNSU (2024 - 2027)
""")

# Editable Section for Work Experience
work_experience = st.text_area("Work Experience", """
    - NONE
""")

# Editable Section for Skills
skills = st.text_area("Skills", """
    - Public Speaking
    - Problem solving 
    - Communication Skills 
    - Data Analysis
""")

# Editable Section for Achievements (New Section)
achievements = st.text_area("Achievements", """
    - Leadership Award
    - Outstanding Student
    - Awarded Outstanding Student Leader, 2023
    - Completed a Data Science Certification from Coursera, 2023
""")

# Section for Uploading a Profile Picture
st.header("Upload Your Profile Picture")

# File uploader for profile image
image_file = st.file_uploader("Upload your profile image", type=["jpg", "jpeg", "png"])

# If an image is uploaded, display it
if image_file is not None:
    st.image(image_file, caption=f"{name}'s Profile Picture", use_column_width=True)

# Editable Section for LinkedIn and Portfolio Links
linkedin = st.text_input("Enter your LinkedIn Profile URL", "https://www.linkedin.com/in/johndoe")
portfolio = st.text_input("Enter your Portfolio URL", "https://johndoe.com")

# Display the editable biography
st.header(f"About {name}")
st.write(about_me)

# Education Section
st.header("Education")
st.write(education)

# Work Experience Section
st.header("Work Experience")
st.write(work_experience)

# Skills Section
st.header("Skills")
st.write(skills)

# Achievements Section (New Section)
st.header("Achievements")
st.write(achievements)

# Links Section
st.header("Connect with Me")
st.markdown(f"[LinkedIn]({linkedin})")
st.markdown(f"[My Portfolio]({portfolio})")

# Button to save changes (Optional)
if st.button("Save Changes"):
    st.success("Your biography has been updated!")
