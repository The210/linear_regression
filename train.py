import csv

def read_csv_as_tuples(file_path):
    tuples_list = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if len(row) >= 2:  # Ensure there are at least 2 columns
                tuples_list.append((int(row[0]), int(row[1])))
    return tuples_list

# Example usage

def train(data, iterations, learningRate):
    theta0 = 0
    theta1 = 0
    m = len(data)

    for _ in range(iterations):
        tmp_theta0 = 0
        tmp_theta1 = 0
        for d in data:
            estimated_price = theta0 + (theta1 * d[0])
            tmp_theta0 += estimated_price - d[1]
            tmp_theta1 += (estimated_price - d[1]) * d[0]
        tmp_theta0 = tmp_theta0 / m * learningRate
        tmp_theta1 = tmp_theta1 / m * learningRate
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1

def main():
    file_path = 'data.csv'
    data = read_csv_as_tuples(file_path)


    # Sample array of tuples
    array_of_tuples = data

    # Step 1: Extract the first and second elements
    first_elements = [t[0] for t in array_of_tuples]
    second_elements = [t[1] for t in array_of_tuples]

    # Step 2: Find the maximum values
    max_first = max(first_elements)
    max_second = max(second_elements)
    #print(max_first, max_second)

    # Step 3 & 4: Normalize the elements
    normalized_tuples = [(t[0] / max_first, t[1] / max_second) for t in array_of_tuples]

    theta0, theta1 = train(normalized_tuples, 50000, 0.01)
    with open('thetas', 'w') as file:
        file.write(f"{theta0} {theta1}")

if __name__ == "__main__":
    main()

