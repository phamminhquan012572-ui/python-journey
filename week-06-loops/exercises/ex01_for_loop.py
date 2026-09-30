```
"""Exercise 01: for, range, enumerate and zip."""

topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# Print numbers 1 through 5.
for number in range(1, 6):
    print(number)

# Print each topic with a one-based position.
for position, topic in enumerate(topics, start=1):
    print(position, topic)

# Pair topics and scores.
for topic, score in zip(topics, scores, strict=True):
    print(topic, score)

print(topics, scores)
```