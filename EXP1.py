
import matplotlib.pyplot as plt

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

h = ['0'] * 6
history = []

for row in data:
    if row[-1] == 'Yes':
        for i in range(6):
            if h[i] == '0':
                h[i] = row[i]
            elif h[i] != row[i]:
                h[i] = '?'
        history.append(h.copy())

print("Final Hypothesis:", h)

# Graph
plt.figure(figsize=(8, 4))

for i, hyp in enumerate(history):
    plt.plot(range(1, 7), hyp, marker='o',
             label=f"Positive Example {i+1}")

plt.xlabel("Attributes")
plt.ylabel("Hypothesis Values")
plt.title("FIND-S Algorithm")
plt.xticks(range(1, 7),
           ['Sky', 'AirTemp', 'Humidity',
            'Wind', 'Water', 'Forecast'])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
