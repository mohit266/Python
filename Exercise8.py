import re

str = '''Toggle navigation
INTERNSHIPS 
ONLINE WINTER TRAININGS OFFER 
LOGIN / REGISTER 

Contact us


Student - Internships
For internship related queries,
visit Student Help Center
VISIT HELP CENTER 
Student - Trainings
For trainings related queries,
visit Trainings Help Center
VISIT HELP CENTER 
Employers
For employer queries,
visit Employer Help Center
VISIT HELP CENTER 
For others
University/college associations
Email us: university.relations@internshala.com
Media queries
Email us: kavya@internshala.com
Fest sponsorships
Email us: sponsorship@internshala.com
For everything else
Email us: sarvesh@internshala.com
Address

Scholiverse Educare Pvt. Ltd. B-610, Unitech Business Zone,
Nirvana Country, South City 2, Gurgaon, India - 122018

Working Hours: Monday to Friday, 10:00 AM – 6:00 PM

Internships by places
Internship in India
Internship in Delhi
Internship in Bangalore
Internship in Hyderabad
Internship in Mumbai
Internship in Chennai
Internship in Gurgaon
Internship in Kolkata
Virtual internship
Internship by Stream
Computer Science Internship
Electronics Internship
Mechanical Internship
Civil Internship
Marketing Internship
Chemical Internship
Finance Internship
Summer Research Fellowship
Campus Ambassador Program
Online Winter Trainings OFFER
Web Development
Android App Development
Programming with Python
Data Science
Ethical Hacking
Core Java
Digital Marketing
Advance Excel
Programming with C & C++
About Internshala
About us
We're hiring
Hire interns for your company
Team Diary
Blog
Our Services
Terms & Conditions
Privacy
Contact us

© Copyright 2019 Internshala

'''
mail = re.findall(r'\w+@\S+\w', str)
# print(mail)
f = open('Email_file.txt', 'a')
i = 1
for email in mail:
    f.write(f"email_address{i}:{email}\n")
    i += 1
f.close()
