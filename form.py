fn=input("First Name:")
ln=input("Last Name:")
ip=input("Issue and Problems :")
pbl=input("Project based problem:")
e=input("Email:")

c=input("contact:")
s=input("semester:")
cn=input("course name")
cc=input("course code:")
cln=input("Course lead name:")

i=input("Would you like to have any another course with same course lead")
h=input("Overall rating of the course")
g=input("We would like to hear if you have any comments/suggestions about the course and class.")
response = input("Does the instructor come punctually on time? (always/mostly/rarely/never): ")
punctuality_level = response.lower()
pace=int(input("The pace at which material was covered was:\n '5' if too fast\n '4' if slightly fast\n '3' if about right\n '2' if lightly slow\n '1' if too slow\n Your choice : "))
material=int(input("The course materials helped me understand the subject matter:\n '5' if you strongly agree\n '4' if you agree\n '3' if neutral\n '2' if disagree\n '1' if strongly disagree\n Your choice : "))
skills=int(input("In this course, I learned skills or content that I consider valuable:\n '5' if strongly agree\n '4' if agree\n '3' if neutral\n '2' if disagree\n '1' if strongly disagree\n Your choice : "))
knowledge=int(input("What would you say about the knowledge of the course lead:\n '5' if excellent\n '4' if good\n '3' if average\n '2' if bad\n '1' if very bad\n Your choice : "))
overall=pace+material+skills+knowledge               
which year did you take admission?
print("2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023 , 2024 ")

