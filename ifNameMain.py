def calculate_area(base, height):
    print("__name__:", __name__)
    return 1 / 2 * (base * height)


if __name__ == '__main__':
    print("This is from ifNameMain.py")
    Area = calculate_area(10, 30)
    print(Area)
