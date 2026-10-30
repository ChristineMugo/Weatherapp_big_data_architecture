
import matplotlib.pyplot as plt

# Data stored in arrays
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 210, 195]

# Choose the graph type
graph_type = input("Choose graph type (line/bar): ").strip().lower()

if graph_type == "line":
    plt.plot(months, sales, marker="o", linestyle="-")
    plt.title("Monthly Sales - Line Graph")

elif graph_type == "bar":
    plt.bar(months, sales)
    plt.title("Monthly Sales - Bar Graph")

else:
    print("Invalid choice. Please enter line or bar.")
    raise SystemExit

plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
