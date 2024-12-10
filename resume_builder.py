# Resume Builder in Python
def create_resume():
    print("Welcome to the Resume Builder!")

    # Collecting user details
    name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    print("\n--- Education Details ---")
    education = input("Enter your highest qualification (e.g., BE in Computer Science): ")
    university = input("Enter your university or institution name: ")
    graduation_year = input("Enter your year of graduation: ")

    print("\n--- Work Experience ---")
    experience = input("Enter your previous job title or write 'Fresher': ")
    company = input("Enter your company name (or type 'N/A' if Fresher): ")
    work_duration = input("Enter your work duration (or type 'N/A'): ")
    responsibilities = input("List your key responsibilities (comma-separated or type 'N/A'): ")

    print("\n--- Skills ---")
    skills = input("List your skills (comma-separated): ")

    print("\n--- Projects ---")
    projects = input("List your key projects (comma-separated): ")

    print("\n--- Achievements (Optional) ---")
    achievements = input("List your achievements (comma-separated, or press Enter to skip): ")

    print("\nGenerating your resume...")

    # Formatting the resume
    resume_content = f"""
    ================================
               RESUME
    ================================

    Name: {name}
    Email: {email}
    Phone: {phone}
    Address: {address}

    -----------------------------
           Education
    -----------------------------
    Highest Qualification: {education}
    University: {university}
    Year of Graduation: {graduation_year}

    -----------------------------
         Work Experience
    -----------------------------
    Job Title: {experience}
    Company: {company}
    Duration: {work_duration}
    Responsibilities: {responsibilities}

    -----------------------------
             Skills
    -----------------------------
    {skills}

    -----------------------------
            Projects
    -----------------------------
    {projects}

    -----------------------------
          Achievements
    -----------------------------
    {achievements if achievements else 'No achievements mentioned.'}

    ================================
    """

    # Saving the resume to a file
    file_name = name.replace(" ", "_") + "_Resume.txt"
    with open(file_name, "w") as file:
        file.write(resume_content)

    print(f"\nResume successfully saved as '{file_name}' in the current directory!")

# Call the function
if __name__ == "__main__":
    create_resume()
    
 
