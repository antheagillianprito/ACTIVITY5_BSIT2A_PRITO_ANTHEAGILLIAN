from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

def stack_menu(stack):
    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty")
        print("5. Is Full")
        print("6. Display")
        print("7. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                value = input("Enter value to push: ")
                stack.push(value)
                print("Value pushed.")

            elif choice == "2":
                value = stack.pop()
                print("Popped:", value)

            elif choice == "3":
                print("Top:", stack.peek())

            elif choice == "4":
                print("Empty:", stack.is_empty())

            elif choice == "5":
                if hasattr(stack, "is_full"):
                    print("Full:", stack.is_full())
                else:
                    print("Linked stack has no fixed capacity.")

            elif choice == "6":
                # Fallback display if __str__ isn't defined in the classes
                if isinstance(stack, ArrayStack):
                    print("Stack (bottom to top):", stack.data[:stack.top + 1])
                elif isinstance(stack, LinkedStack):
                    elements = []
                    curr = stack.top
                    while curr:
                        elements.append(curr.value)
                        curr = curr.next
                    print("Stack (top to bottom):", elements)

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

        except (IndexError, OverflowError) as e:
            print("Error:", e)


def queue_menu(queue):
    while True:
        print("\n--- QUEUE MENU ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek Front")
        print("4. Is Empty")
        print("5. Is Full")
        print("6. Display")
        print("7. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                value = input("Enter value to enqueue: ")
                queue.enqueue(value)
                print("Value enqueued.")

            elif choice == "2":
                value = queue.dequeue()
                print("Dequeued:", value)

            elif choice == "3":
                print("Front:", queue.peek_front())

            elif choice == "4":
                print("Empty:", queue.is_empty())

            elif choice == "5":
                if hasattr(queue, "is_full"):
                    print("Full:", queue.is_full())
                else:
                    print("Linked queue has no fixed capacity.")

            elif choice == "6":
                if isinstance(queue, ArrayQueue):
                    # Display circular queue elements in correct order
                    elements = [queue.data[(queue.front + i) % len(queue.data)] for i in range(queue.size)]
                    print("Queue (front to rear):", elements)
                elif isinstance(queue, LinkedQueue):
                    elements = []
                    curr = queue.front
                    while curr:
                        elements.append(curr.value)
                        curr = curr.next
                    print("Queue (front to rear):", elements)

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

        except (IndexError, OverflowError) as e:
            print("Error:", e)


def main():
    while True:
        print("\n==============================")
        print(" STACKS AND QUEUES PROGRAM")
        print("==============================")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("5. Exit")

        choice = input("Choose implementation: ")

        if choice == "1":
            capacity = int(input("Enter stack capacity: "))
            stack = ArrayStack(capacity)
            stack_menu(stack)

        elif choice == "2":
            stack = LinkedStack()
            stack_menu(stack)

        elif choice == "3":
            capacity = int(input("Enter queue capacity: "))
            queue = ArrayQueue(capacity)
            queue_menu(queue)

        elif choice == "4":
            queue = LinkedQueue()
            queue_menu(queue)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()