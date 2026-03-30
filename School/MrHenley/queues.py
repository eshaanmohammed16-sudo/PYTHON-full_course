# Create a queue with a fixed maximum size
def createqueue(size):
    queue = [None] * size      # allocate list with fixed capacity
    front = -1                 # -1 means queue is empty
    rear = -1                  # -1 means no elements inserted yet
    return queue, front, rear


# Add an item to the queue
def enqueue(queue, front, rear, item, size):
    # Check if queue is full
    if rear == size - 1:
        print("Queue is full, cannot enqueue.")
        return queue, front, rear

    # If queue was empty, set front to 0
    if front == -1:
        front = 0

    # Move rear forward and insert the item
    rear += 1
    queue[rear] = item
    print(f"{item} has been added to the queue.")
    return queue, front, rear


# -------------------------
# Example usage
# -------------------------

size = 5
queue, front, rear = createqueue(size)

queue, front, rear = enqueue(queue, front, rear, "Eshaan", size)
print(queue, front, rear)

queue, front, rear = enqueue(queue, front, rear, "Callum", size)
print(queue, front, rear)

print("shush")