from collections import deque

def managePackageQueue(query):
    queue = deque()  # Initialize a deque to act as the queue
    results = []     # List to store the results for SHIP queries

    for q in query:
        operation = q[0]
        if operation == "INSERT":
            # Add the package ID to the queue
            package_id = q[1]
            queue.append(package_id)
        elif operation == "SHIP":
            # Check if there are at least 3 items in the queue
            if len(queue) >= 3:
                # Ship the first 3 items (FIFO order)
                group = [queue.popleft() for _ in range(3)]
                results.append(group)
            else:
                # Not enough items to ship, append "N/A"
                results.append(["N/A"])

    return results


# Example usage:
query = [
    ["INSERT", "GT23513413"],
    ["INSERT", "TQC2451340"],
    ["SHIP"],
    ["INSERT", "VYP8561991"],
    ["SHIP"]
]

output = managePackageQueue(query)
print(output)
