# ============================================================
# Hospital Patient Queue Management System
# ============================================================

class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status  # 0 = normal, 1 = urgent, 2 = super-urgent

    def __str__(self):
        status_map = {
            0: "Normal",
            1: "Urgent",
            2: "Super-Urgent"
        }
        return f"{self.name} ({status_map.get(self.status, 'Unknown')})"


class Specialization:
    def __init__(self, name, capacity=5):
        self.name = name
        self.capacity = capacity
        self.queue = []

    def add_patient(self, patient):
        if len(self.queue) >= self.capacity:
            print(f"{self.name} is full. Cannot add patient {patient.name}.")
            return

        if patient.status == 2:
            self.queue.insert(0, patient)
        elif patient.status == 1:
            inserted = False
            for i in range(len(self.queue)):
                if self.queue[i].status < 1:
                    self.queue.insert(i, patient)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(patient)
        else:
            self.queue.append(patient)

        print(f"Patient {patient.name} added to {self.name}.")

    def get_next_patient(self):
        if not self.queue:
            print(f"No patients in {self.name}.")
            return None
        patient = self.queue.pop(0)
        print(f"Next patient in {self.name}: {patient}")
        return patient

    def remove_patient(self, name):
        for patient in self.queue:
            if patient.name.lower() == name.lower():
                self.queue.remove(patient)
                print(f"Patient {name} removed from {self.name}.")
                return
        print(f"Patient {name} not found in {self.name}.")

    def list_patients(self):
        print(f"\n{self.name} Queue:")
        if not self.queue:
            print("No patients.")
        else:
            for patient in self.queue:
                print(patient)


class OperationsManager:
    def __init__(self):
        self.specializations = {
            1: Specialization("General"),
            2: Specialization("Cardiology"),
            3: Specialization("Orthopedics")
        }

    def add_patient(self, spec_id, name, status):
        if spec_id in self.specializations:
            patient = Patient(name, status)
            self.specializations[spec_id].add_patient(patient)

    def list_patients(self):
        for spec in self.specializations.values():
            spec.list_patients()

    def get_next(self, spec_id):
        if spec_id in self.specializations:
            self.specializations[spec_id].get_next_patient()

    def remove_patient(self, spec_id, name):
        if spec_id in self.specializations:
            self.specializations[spec_id].remove_patient(name)




if __name__ == "__main__":
    manager = OperationsManager()

    manager.add_patient(1, "Swaraj", 0)
    manager.add_patient(1, "Rahul", 2)
    manager.add_patient(1, "Amit", 1)

    manager.add_patient(2, "Priya", 1)
    manager.add_patient(2, "Neha", 0)

    manager.add_patient(3, "Rohit", 2)

    manager.list_patients()

    manager.get_next(1)
    manager.get_next(2)

    manager.remove_patient(1, "Amit")

    manager.list_patients()

