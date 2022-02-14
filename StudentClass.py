from datetime import date


class StudentClass:
    

    def __init__(self,studentid,name,birthdate,classification):
        self.__StudentID = studentid
        self.__Name = name
        self.__DateOfBirth = birthdate
        self.__Classification = classification
        self.__age = 0
        self.__registration = 0



    def StudentAge(self):
        self.__age = date.today().year - self.__DateOfBirth.year - 1

    def Registration(self):
        if self.__Classification == "Sr" or "sr":
            self.__registration = "11/1 thru 11/3"
        elif self.__Classification == "Jr" or "jr":
            self.__registration = "11/4 thru 11/6"
        elif self.__Classification == "S" or "s":
            self.__registration = "11/7 thru 11/9"
        elif self.__Classification == "F" or "f":
            self.__registration = "11/10 thru 11/12"

    def get_age(self):
        return self.__age

    def get_registration(self):
        return self.__registration

    