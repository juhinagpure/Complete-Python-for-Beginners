from random import randint  # Correct import for randint

class Train:
    
    # Method to book a ticket
    def book(self, trainNo, fro, to):
        # Use f-string to format values
        print(f"Ticket is booked in trainNo: {trainNo} from {fro} to {to}")
    
    # Placeholder for status method
    def getStatus(self, trainNo):
        print(f"Checking status for trainNo: {trainNo}")
        # You can later add logic to show status
    
    # Method to get random fare
    def getFare(self, trainNo, fro, to):
        fare = randint(222, 5555)  # Generate random fare
        print(f"The fare is ₹{fare} for trainNo: {trainNo} from {fro} to {to}")

# Example usage
t = Train()
t.book(12345, "pune", "Delhi")
t.getStatus(12345)
t.getFare(12345, "pune", "Delhi")
