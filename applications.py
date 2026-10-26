# APPPLICATION EXERCISES

# ---------------------------------------------
# A. Balanced Parentheses Checker Using a Stack
# ---------------------------------------------

def is_balanced(expression):
    stack = LinkedStack()
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in mapping.values():
            stack.push(char)
        elif char in mapping.keys():
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False
    return stack.is_empty()

# Example usage:
print(is_balanced("{[()]}"))  # Output: True
print(is_balanced("([)]"))    # Output: False

class PrintJob:
    def __init__(self, job_id, pages):
        self.job_id = job_id
        self.pages = pages
        
    def __str__(self):
        return f"Job ID: {self.job_id} ({self.pages} pages)"


# -------------------------
# B. Print Queue Simulation
# -------------------------

def simulate_print_queue():
    queue = LinkedQueue()
    
    # Enqueue sample print jobs
    queue.enqueue(PrintJob("J101", 5))
    queue.enqueue(PrintJob("J102", 2))
    queue.enqueue(PrintJob("J103", 8))
    
    print("--- Starting Print Queue Simulation (FIFO) ---")
    position = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Printing position {position}: [ {job} ]")
        position += 1

simulate_print_queue()