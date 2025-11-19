# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
    num = int(input("Enter a number: "))
    result = check_even_odd(num)
    print(result)

# Call main function
if __name__ == "__main__":
    main()
