def main():
    with open("thetas", "r") as file:
        file_contents = file.read()
    
    try:
        mileage = float(input("Please enter a mileage: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()
    mileage = mileage / 240000

    theta0 = float(file_contents.split()[0])
    theta1 = float(file_contents.split()[1])
    print((theta0 + (theta1 * mileage)) * 8290)


if __name__ == "__main__":
    main()