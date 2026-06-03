import statistics

def process_sales(filename="sales.txt"):
    try:
        with open(filename, "r") as f:
            data = []
            for line in f:
                line = line.strip()
                if line:
                    data.append(float(line))
        if not data:
            print("No data found in file.")
            return
        mean_val = statistics.mean(data)
        median_val = statistics.median(data)
        print(f"Mean: {mean_val}")
        print(f"Median: {median_val}")
    except FileNotFoundError:
        print("Error: The file sales.txt was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")

with open("sales.txt", "w") as f:
    f.write("100\n150.5\n200\n250\n300\n")

process_sales()
