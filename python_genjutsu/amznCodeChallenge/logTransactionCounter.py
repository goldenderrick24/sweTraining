def countGroups(related):
    def dfs(node, visited):
        # Mark the current node as visited
        visited[node] = True
        
        # Visit all the connected nodes
        for neighbor in range(len(related)):
            if related[node][neighbor] == '1' and not visited[neighbor]:
                dfs(neighbor, visited)
    
    n = len(related)
    visited = [False] * n
    groups = 0
    
    for i in range(n):
        if not visited[i]:
            # Start a new group and perform DFS
            dfs(i, visited)
            groups += 1  # Increment group count
    
    return groups

# Example Input
related = [
    "1100",
    "1110",
    "0110",
    "0001"
]

# Call the function
print(countGroups(related))  # Output: 2


def processLogs(logs, threshold):
    from collections import defaultdict

    # Dictionary to count transactions for each user
    transaction_counts = defaultdict(int)

    # Parse each log entry
    for log in logs:
        sender, recipient, _ = log.split()
        
        # Increment transaction count for sender and recipient
        transaction_counts[sender] += 1
        if sender != recipient:  # Avoid double counting for the same user
            transaction_counts[recipient] += 1

    # Filter users who meet or exceed the threshold
    result = [user for user, count in transaction_counts.items() if count >= threshold]

    # Return sorted list of user IDs
    return sorted(result, key=int)


# Example Input
logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = 2

# Example Output
print(processLogs(logs, threshold))
