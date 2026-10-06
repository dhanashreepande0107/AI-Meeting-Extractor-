import re

def extract_action_items(transcript):
    action_items = []

    patterns = [
        r"(\w+) will (.+?) by (\d{1,2}/\d{1,2}/\d{4})",
        r"(\w+) should (.+?) by (\d{1,2}/\d{1,2}/\d{4})"
    ]

    for pattern in patterns:
        matches = re.findall(pattern, transcript)

        for match in matches:
            owner = match[0]
            task = match[1]
            deadline = match[2]

            action_items.append({
                "Task": task,
                "Owner": owner,
                "Deadline": deadline,
                "Status": "Pending",
                "Confidence": "90%"
            })

    return action_items