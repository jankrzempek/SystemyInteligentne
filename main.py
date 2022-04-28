# The Clinic.Inc 🏥
# by Maja & Janek

from Doctor import Doctor
from Patient import Patient
from Queue import Queue
from mainHelpers import Helpers
import time

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

    #Helpers
    helpers = Helpers()

    # Doctors
    lightDoctor = Doctor(serviceTime = 10, walkingTime = 10)
    mediumDoctor = Doctor(serviceTime = 20, walkingTime = 20)
    hardDoctor = Doctor(serviceTime = 30, walkingTime = 30)
    multiDoctor = Doctor(serviceTime = 15, walkingTime = 20)

    doctorsColletion = [
        lightDoctor,
        mediumDoctor,
        hardDoctor,
        multiDoctor
    ]

    #Queue
    lightQueue = Queue(queue=[])
    mediumQueue = Queue(queue=[])
    hardQueue = Queue(queue=[])
    multiQueue = Queue(queue=[])

    queueColection = [
        lightQueue,
        mediumQueue,
        hardQueue,
        multiQueue
    ]

    # Adding patients to the queue
    lightQueue.addToQueue(patient=Patient(name="Wojtek"))
    lightQueue.addToQueue(patient=Patient(name="Marcin"))
    lightQueue.addToQueue(patient=Patient(name="Żaneta"))

    mediumQueue.addToQueue(patient=Patient(name="Anna"))
    mediumQueue.addToQueue(patient=Patient(name="Dawid"))

    hardQueue.addToQueue(patient=Patient(name="Franek"))
    hardQueue.addToQueue(patient=Patient(name="Darek"))
    hardQueue.addToQueue(patient=Patient(name="Marek"))
    hardQueue.addToQueue(patient=Patient(name="Alicja"))
    hardQueue.addToQueue(patient=Patient(name="Marysia"))

    # Starting work day
    end_time = helpers.defineWorkingHours()
    while(time.time() < end_time):

        if lightDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(lightQueue.queue):
            patient = lightQueue.takeFirstToDoctor(doctor=lightDoctor)
            print(f"- (💊 L) Currently the patient {patient.name} is badany -")
        
        if mediumDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(mediumQueue.queue):
            patient = mediumQueue.takeFirstToDoctor(doctor=mediumDoctor)
            print(f"- (💉 M) Currently the patient {patient.name} is badany -")
        
        if hardDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInQueue(hardQueue.queue):
            patient = hardQueue.takeFirstToDoctor(doctor=hardDoctor)
            print(f"- (🦠 H) Currently the patient {patient.name} is badany -")
        
        if multiDoctor.isFreeToTakeNewPatient() and helpers.isAnyoneInAnyQueue(queueColection=queueColection):
            queue = helpers.getQueueWithPeople(queueColection=queueColection)
            patient = queue.takeFirstToDoctor(doctor=multiDoctor)
            print(f"- (🧻 MT) Currently the patient {patient.name} is badany -")

    # Define the ending 
    print("The badania has finished, tasks completed.")

    totalOfPatientPrzebadanych = 0
    for doctor in doctorsColletion:
        totalOfPatientPrzebadanych += doctor.patientCount
    
    print(f"Total of patient przebadanych: {totalOfPatientPrzebadanych}")

