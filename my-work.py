# Stack for undoing patient check-ins
undo_checkins_stack = []

# Queue for managing patient checkups
checkup_queue = []

# List for keeping track of patient details
patient_details_list = []

# Function to check-in a patient (add to patient details and checkup queue)
def check_in_patient(patient_name, patient_detail):
    patient_details_list.append(patient_detail)  # Add patient details to the list
    checkup_queue.append(patient_name)  # Enqueue patient for checkup
    undo_checkins_stack.append(patient_name)  # Add to stack for undo option
    print(f"{patient_name} checked in.")

# Function to undo the last check-in
def undo_last_checkin():
    if undo_checkins_stack:
        last_patient = undo_checkins_stack.pop()  # Remove the last check-in from the stack
        if last_patient in checkup_queue:
            checkup_queue.remove(last_patient)  # Remove the patient from the checkup queue
        print(f"Check-in for {last_patient} has been undone.")
    else:
        print("No check-ins to undo.")

# Function to process the next patient for checkup
def process_next_checkup():
    if checkup_queue:
        next_patient = checkup_queue.pop(0)  # Dequeue the next patient for checkup
        print(f"Processing checkup for {next_patient}.")
    else:
        print("No patients waiting for checkup.")

# Function to view all patient details
def view_patient_details():
    print("Patient Details List:", patient_details_list)

# Example usage
check_in_patient("Alice", {"name": "Alice", "age": 30, "condition": "flu"})
check_in_patient("Bob", {"name": "Bob", "age": 45, "condition": "fever"})

# Undo last check-in
undo_last_checkin()  # Undo Bob's check-in

# Process the next patient for checkup
process_next_checkup()  # Process Alice

# View patient details
view_patient_details()
