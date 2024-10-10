# train_model.py
import random

# Simulate model training
def train_model():
    # For simplicity, generate random metrics
    accuracy = random.uniform(0.8, 0.95)
    loss = random.uniform(0.1, 0.3)
    return accuracy, loss

# Save metrics to a file
def save_metrics(accuracy, loss):
    with open("metrics.txt", "w") as f:
        f.write(f"Accuracy: {accuracy:.2f}\n")
        f.write(f"Loss: {loss:.2f}\n")


accuracy, loss = train_model()
save_metrics(accuracy, loss)
print(f"Model trained with Accuracy: {accuracy:.2f}, Loss: {loss:.2f}")
