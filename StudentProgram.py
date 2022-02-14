import StudentClass as s
from datetime import date

DateofBirth = date(1996,8,11)

brad = s.StudentClass(892110407,"Brad Roedema",DateofBirth,"Sr")

def main():

    brad.StudentAge()
    brad.Registration()
    print("Brad Roedema is",brad.get_age(),"years old")
    print("Brad Roedema registers",brad.get_registration())

main()