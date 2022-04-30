# The Clinic.Inc 🏥
# by Maja & Janek

from Doctor import Doctor
from Patient import Patient
from Queue import Queue
from mainHelpers import Helpers
from LearningStuff.projekt import Classifier
import time

# TODO: Odpalić kilka razy dla nowo wygenrowanych pacjentów i zrobić mała statystykę i wykres jeden - zmiejszyć jedną liczbę pacjentów

# Algorytm zachłanny - List scheduling
# Lekarz jest na takim samym poziomie specjalizacji
# Kryterium Cmax - minimalizować najdłuzszy czas przyjęcia

# Documentation !

#      WSZYSTKO JEST SKROCONE 
# __ WSZYSTKO DZIEL PRZEZ 100 __
#       8h = 28 800 sekund
#       288 sek ~ 4.8 minuty

# Założenia odnośnie pacjentów
# Doktor, którego: Pacjent ze zdefiniowanym lekkim przebiegiem choroby będzie potrzebował 10 min przy odpowiadającym mu okienku. Czas dotarcia do okienka będzie wynosił 10sek.
# Doktor, którego: Pacjent ze zdefiniowanym średnim przebiegiem choroby będzie potrzebował 20 min przy odpowiadającym mu okienku. Czas dotarcia do okienka będzie wynosił 20sek.
# Doktor, którego: Pacjent ze zdefiniowanym ciężkim przebiegiem choroby będzie potrzebował 30 min przy odpowiadającym mu okienku. Czas dotarcia do okienka będzie wynosił 30sek.
# Doktor multi, którego: Pacjent będzie potrzebował 15 min przy odpowiadającym mu okienku. Czas dotarcia do okienka będzie wynosił 20sek.

if __name__ == "__main__":

    # Helpers
    helpers = Helpers()

    # Classifier
    print("🦠 The group of people is gathering. Beata is classifing now...")
    classifier = Classifier()
    model = classifier.create_model()
    classifiedPatientsAll = classifier.get_patient(model)
    print("Beata classified them, some of them are symulujący 🥸")
    print("Beata is kicking out symulujących 🦵🏻")
    time.sleep(5)
    classifiedPatientsFiltered = [x for x in classifiedPatientsAll if x != 0]
    patientsSimulants = len(classifiedPatientsAll) - len(classifiedPatientsFiltered)
    print("Patients are ready to be przebadani!")
    time.sleep(5)
    print("----[]-----[]-----[]----[]--<-<-\(+_+)/")

    #Define time counters for each queue
    firstTimer = 0
    secondTimer = 0
    thirdTimer = 0
    fourthTimer = 0

    # Doctors
    # Lekarze randomowo obsługuja rónych pacjentów
    firstDoctor = Doctor()
    secondDoctor = Doctor()
    thirdDoctor = Doctor()
    forthDoctor = Doctor()

    doctorsColletion = [
        firstDoctor,
        secondDoctor,
        thirdDoctor,
        forthDoctor
    ]

    #Queue
    firstQueue = Queue(queue=[])
    secondQueue = Queue(queue=[])
    thirdQueue = Queue(queue=[])
    forthQueue = Queue(queue=[])

    queueColection = [
        firstQueue,
        secondQueue,
        thirdQueue,
        forthQueue
    ]

    # Given all of the patients the right identity
    IdentifiedPatients = [helpers.convertPatient(x) for x in classifiedPatientsFiltered]

    def sortValue(p):
        return p.serviceTotalTime

    IdentifiedPatients.sort(key=sortValue)

    # Moving patients to right queue
    firstQueue.queue = IdentifiedPatients[0::4]
    del IdentifiedPatients[0::4]

    secondQueue.queue = IdentifiedPatients[0::3]
    del IdentifiedPatients[0::3]

    thirdQueue.queue = IdentifiedPatients[0::2]
    del IdentifiedPatients[0::2]

    forthQueue.queue = IdentifiedPatients

    # Starting work day
    end_time = helpers.defineWorkingHours()
    while(time.time() < end_time):

        if firstDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(firstQueue.queue):
            patient = firstQueue.takeFirstToDoctor(doctor=firstDoctor)
            firstTimer += patient.serviceTotalTime
            print(f"- (D1 👨🏻‍⚕️) Currently the patient {patient.name} is badany -")
        
        if secondDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(secondQueue.queue):
            patient = secondQueue.takeFirstToDoctor(doctor=secondDoctor)
            secondTimer += patient.serviceTotalTime
            print(f"- (D2 👨🏿‍⚕️) Currently the patient {patient.name} is badany -")
        
        if thirdDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(thirdQueue.queue):
            patient = thirdQueue.takeFirstToDoctor(doctor=thirdDoctor)
            thirdTimer += patient.serviceTotalTime
            print(f"- (D3 👩🏼‍⚕️) Currently the patient {patient.name} is badany -")
        
        if forthDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(forthQueue.queue):
            patient = forthQueue.takeFirstToDoctor(doctor=forthDoctor)
            fourthTimer += patient.serviceTotalTime
            print(f"- (D4 👩🏾‍⚕️) Currently the patient {patient.name} is badany -")

    # Define the ending 
    print("The badania has finished, tasks completed.")

    totalOfPatientPrzebadanych = 0
    for doctor in doctorsColletion:
        totalOfPatientPrzebadanych += doctor.patientCount
    
    patientUnserviced = (len(classifiedPatientsAll) - (totalOfPatientPrzebadanych + patientsSimulants))
    print("--------SUMARRY--------------------------------------------")
    print(f"Total of patient przebadanych: {totalOfPatientPrzebadanych}")
    print(f"Total of patient NIEprzebadanych: {patientUnserviced}")
    print(f"Total of patient symulantów: {patientsSimulants}")
    print(f"1 - First queue total time: {firstTimer}")
    print(f"2 - Second queue total time: {secondTimer}")
    print(f"3 - Third queue total time: {thirdTimer}")
    print(f"4 - Fourth queue total time: {fourthTimer}")


