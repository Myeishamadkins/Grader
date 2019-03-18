def main():

    grades = []
    print("Enter your grades. Enter 'grade' when you are finished.")
    while True:
        response = input('Grade:"{0}" Number: '.format(len(grades) + 1))
        if response == 'grade':
            break
        else:
            grades.append(int(response))

    average_nums = sum(grades) / len(grades)
    if average_nums >= 90:
        print("Your final grade was a A and averaged as: ", average_nums)
    elif average_nums >= 80:
        print("Your final grade was a B and average as: ", average_nums)
    elif average_nums >= 70:
        print("Your final grade was a C and average as: ", average_nums)
    elif average_nums >= 65:
        print("Your final grade was a D and average as: ", average_nums)
    else:
        print("Your final grade was a F and average as: ", average_nums)


if __name__ == '__main__':
    main()
