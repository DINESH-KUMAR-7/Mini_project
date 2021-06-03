"""
  Mini Project : Command Line Appointment Booking System
"""

#Doctor class
class Doctor:
    def __init__(self,doctor_name,specialisations,availability_days,appointment_seat,hospital):
        self.doctor_name = doctor_name
        self.specialisations = specialisations
        self.availability_days = availability_days
        self.appointment_seat = appointment_seat
        self.hospital = hospital

    def is_available(self,day):
        #day in list and appointment is available it returns TRUE
        if day in self.availability_days and self.appointment_seat[day] > 0:
            return True
        else:
            return False

    def is_specialist(self,disease):
        for _ in self.specialisations:
            if  _ ==disease :
                return True
            else:
                return False

    def book_appointment(self,day, disease):
        #call the functions to get details
        if self.is_specialist(disease) == False:
            return -1
        elif self.is_available(day) == False:
            return 0
        else:
            return 1

    def do_booking(self,day, disease):
        if self.book_appointment(day,disease) == -1:
            return "Requested Doctor is not a specialist for your request"

        elif self.book_appointment(day,disease) == 0:
            return "Doctor not available on your requested date"

        else:
            #decrements the appointment in Dictionary
            self.appointment_seat[day] -= 1
            print("-------------------------------------------------------------")
            print("Doctor:",self.doctor_name,"Hospital:",self.hospital.hospital_name,"\nAddress:",self.hospital.address_of_the_hospital,"\nPatient:",patient.name_of_patient)
            print("Booking Day:",day)
            print("Booked for:",disease)
            print("---------------------------------------------------------------")
            return "Appointment Successful"

#Patient class 4r appointment booking
class Patient:
    def __init__(self,name_of_patient,disease,doctor):
        self.name_of_patient = name_of_patient
        self.disease = disease
        self.doctor = doctor#Doctor class object

    #calls the do_booking in doctor class
    def book(self,requested_day):
        print(patient.doctor.do_booking(requested_day,self.disease))

#Hospital class just for initialization
class Hospital:
    def __init__(self,hospital_name, address_of_the_hospital):
        self.hospital_name = hospital_name
        self.address_of_the_hospital = address_of_the_hospital

hospital = Hospital("ABC Multi-speciality Hospital", "71, South Street, Ambattur, Chennai")
doctor = Doctor("Dr. John", ["Diabetics", "ENT"], ["Monday", "Friday"], {"Monday": 5, "Friday":1}, hospital)
patient = Patient("talentpY", "Diabetics", doctor)


patient.book("Friday")
patient.book("Friday")
patient.book("Tuesday")
patient = Patient("Roy", "Dengue", doctor)
patient.book("Monday")

"""
Output:
/GitHub/Mini_project/Doctor.py
-------------------------------------------------------------
Doctor: Dr. John Hospital: ABC Multi-speciality Hospital
Address: 71, South Street, Ambattur, Chennai
Patient: talentpY
Booking Day: Friday
Booked for: Diabetics
---------------------------------------------------------------
Appointment Successful
Doctor not available on your requested date
Doctor not available on your requested date
Requested Doctor is not a specialist for your request
"""