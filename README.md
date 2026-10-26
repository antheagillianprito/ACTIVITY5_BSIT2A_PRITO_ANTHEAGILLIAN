# ACTIVITY5_BSIT2A_PRITO_ANTHEAGILLIAN

# Module 5 Laboratory Activity: Stacks and Queues (Array vs. Linked List)

## Student Information
* **Name:** Prito, Anthea Gillian G.
* **Course & Section:** BSIT-2A
* **Institution:** University of Eastern Philippines

## Project Overview
This repository contains the complete implementation of fundamental linear data structures—**Stacks** and **Queues**—built from first principles in Python without relying on built-in collection shortcuts that violate complexity constraints (such as `insert(0, x)` or `pop(0)`). The project demonstrates both fixed-capacity array-based implementations (with explicit underflow/overflow exception handling) and dynamic linked-list implementations.

## File Structure & Descriptions

* **`array_stack.py`**: Contains the `ArrayStack` class. Implements a fixed-size array stack using a tracking `top` index. Includes robust error handling for **Stack Overflow** and **Stack Underflow**.
* **`linked_stack.py`**: Contains the `Node` and `LinkedStack` classes. Implements a dynamic stack operating entirely at the **head** to ensure $O(1)$ time complexity for insertions and deletions.
* **`array_queue.py`**: Contains the `ArrayQueue` class. Implements a **circular queue** utilizing modulo arithmetic (`%`) and a size counter to reuse empty leading spaces and prevent false overflows.
* **`linked_queue.py`**: Contains the `LinkedQueue` class. Implements a dynamic queue anchored by separate **head (`front`)** and **tail (`rear`)** references for optimal $O(1)$ performance.
* **`test_driver.py`**: An interactive, menu-driven testing program that allows users to choose any of the four data structures, perform operations (`push`, `pop`, `enqueue`, `dequeue`, `peek`, capacity checks), and view real-time state changes. It also includes the two required **application exercises**:
  1. *Balanced Parentheses Checker* using a stack.
  2. *Print Queue Simulation* demonstrating FIFO task scheduling.
* **`analysis.md`**: Written responses explaining the structural design decisions (why linked stacks push at the head and why array queues must be circular).

## How to Run the Program

1. Ensure you have **Python 3.x** installed on your system.
2. Clone or download all source files into the same local directory (unzipped).
3. Open your terminal or command prompt in that directory and execute the test driver:

```bash
python test_driver.py
