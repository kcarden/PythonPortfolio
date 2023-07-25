# Importing necessary modules
import time

# Resume details
name = "Kevin Troy Carden"
email = "cardenkevin@gmail.com"
phone = "(706)410-8955"

objective = """
Results-driven and customer-focused professional seeking a Junior Python Developer position. 
Leveraging a strong foundation in Python programming and a passion for problem-solving, I am eager 
to contribute my skills to a dynamic development team and build innovative solutions that 
positively impact the success of the organization.
"""

experience = [
    {
        "title": "Customer Service Representative",
        "company": "Central BDC (Remote)",
        "date": "January 2023 - Present",
        "description": """- Provided technical support and troubleshooting assistance to customers, 
    ensuring timely resolutions.
- Demonstrated strong customer advocacy by addressing inquiries and concerns with professionalism.
- Effectively communicated complex technical concepts to customers in a clear and concise manner."""
    },
    {
        "title": "Inside Sales",
        "company": "Turbo Diesel and Electric Systems",
        "date": "October 2021 - January 2023",
        "description": """- Cultivated and maintained strong customer relationships, understanding 
    their needs and providing personalized solutions.
- Collaborated with the sales team to identify upselling opportunities and achieve sales targets.
- Assisted customers with technical inquiries regarding product specifications and compatibility."""
    },
    {
        "title": "Service Advisor",
        "company": "Multiple Dealerships",
        "date": "September 2016 - October 2021",
        "description": """- Managed and prioritized customer requests, ensuring timely resolution and 
    customer satisfaction.
- Effectively communicate technical information to customers, addressing concerns and recommending 
    appropriate solutions.
- Collaborated with technicians to streamline processes and optimize service delivery."""
    },
]

skills = {
    "Python Programming": "Proficient in Python, including core concepts, data structures, and algorithms.",
    "Web Development": "Familiarity with HTML, CSS, and basic front-end frameworks.",
    "Problem-Solving": "Strong analytical skills and ability to tackle complex programming challenges.",
    "Communication": "Effective verbal and written communication for collaborating with team members.",
    "Teamwork": "Collaborative team player, adept at working with colleagues to achieve project goals.",
}

education = [
    {
        "school": "Fleming Island Highschool",
        "location": "Fleming Island, FL",
        "degree": "High School Diploma",
        "date": "May 2010",
        "achievements": "- Lacrosse Team Captain",
    },
]

certificates_training = [
    "CompTIA A+ Certification",
    "ITIL Foundation Certification",
]

additional_skills = [
    "Proficient in Microsoft Office Suite (Word, Excel, PowerPoint)",
    "Familiarity with ticketing systems and remote support tools.",
    "Strong understanding of network protocols and troubleshooting.",
]

# Creating an interactive resume
def print_with_delay(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

print_with_delay(f"Name: {name}")
print_with_delay(f"Email: {email}")
print_with_delay(f"Phone: {phone}\n")
print_with_delay("Objective:")
print_with_delay(objective.strip(), delay=0.02)

print_with_delay("\nWork Experience:")
for exp in experience:
    print_with_delay(f"\nTitle: {exp['title']}")
    print_with_delay(f"Company: {exp['company']}")
    print_with_delay(f"Date: {exp['date']}")
    print_with_delay(exp['description'], delay=0.02)

print_with_delay("\nSkills:")
for skill, description in skills.items():
    print_with_delay(f"\n- {skill}: {description}")

print_with_delay("\nEducation:")
for edu in education:
    print_with_delay(f"\nSchool: {edu['school']}")
    print_with_delay(f"Location: {edu['location']}")
    print_with_delay(f"Degree: {edu['degree']}")
    print_with_delay(f"Date: {edu['date']}")
    print_with_delay(edu['achievements'], delay=0.02)

print_with_delay("\nCertificates / Training:")
for cert in certificates_training:
    print_with_delay(f"\n- {cert}")

print_with_delay("\nAdditional Skills:")
for skill in additional_skills:
    print_with_delay(f"\n- {skill}")
