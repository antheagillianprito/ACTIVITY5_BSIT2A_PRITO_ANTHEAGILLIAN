# ACTIVITY5_BSIT2A_PRITO_ANTHEAGILLIAN

# Module 5 Laboratory Activity: Stacks and Queues (Array vs. Linked List)

## Student Information
* **Name:** Prito, Anthea Gillian G.
* **Course & Section:** BSIT-2A
* **Institution:** University of Eastern Philippines

---

## Project Overview
This repository contains the complete implementation of fundamental linear data structures—**Stacks** and **Queues**—built from first principles in Python without relying on built-in collection shortcuts that violate complexity constraints (such as `insert(0, x)` or `pop(0)`). The project demonstrates both fixed-capacity array-based implementations (with explicit underflow/overflow exception handling) and dynamic linked-list implementations.

---

## File Structure & Descriptions

* **`array_stack.py`**: Contains the `ArrayStack` class. Implements a fixed-size array stack using a tracking `top` index with explicit **Stack Overflow** and **Stack Underflow** error handling.
* **`linked_stack.py`**: Contains the `LinkedStack` class. Implements a dynamic stack operating at the **head** to ensure $O(1)$ time complexity for insertions and deletions.
* **`array_queue.py`**: Contains the `ArrayQueue` class. Implements a **circular queue** utilizing modulo arithmetic (`%`) and a size counter to reuse empty leading space.
* **`linked_queue.py`**: Contains the `LinkedQueue` class. Implements a dynamic queue with separate **head (`front`)** and **tail (`rear`)** references for $O(1)$ operations.
* **`node.py`**: Contains the shared `Node` class used by both `LinkedStack` and `LinkedQueue` to avoid code duplication.
* **`main.py`**: The main menu-driven program that allows users to select any implementation, execute operations (`push`, `pop`, `enqueue`, `dequeue`, `peek`, capacity checks), and inspect the current state of the structure.
* **`applications.py`**: Contains the two real-world application exercises:
  1. **Balanced Parentheses Checker**: Uses a stack to check if expression symbols `()[] {}` are properly balanced.
  2. **Print Queue Simulation**: Simulates a FIFO printer queue handling print jobs sequentially.
* **`analysis.md`**: Written responses explaining the structural design choices (why linked stacks push at the head and why array queues must be circular).

---

## How to Run the Program

1. Ensure you have **Python 3.x** installed on your system.
2. Clone or download all source files into the same local directory (unzipped).
3. To run the main interactive menu:
   ```bash
   python main.py
4. To run the application exercises:
   ```bash
   python applications.py
