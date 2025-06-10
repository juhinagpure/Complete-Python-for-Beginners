def main():
    try:
        a=int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(f"An error occurred: {e}")
        return 

    finally:
        print("I am inside the finally block")
        print("Thank you")

main()