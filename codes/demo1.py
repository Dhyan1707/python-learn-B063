def main():

    a = 2
    b = 3.4
    c = True
    d = "Apple"
    e = [2, 'app', False]
    f = {1: "sunday", 2: "monday"}

    print(type(a))

    num_int=123
    num_flo=1.23
    num_new=num_int+num_flo
    print("Value of num_new:",num_new)
    print("Data types of num_new:",type(num_new))

def segregateMarks(lst):
    a = []
    b = []
    c = []

    for val in lst:
        if val > 80:
            a.append(val)
        elif val < 80 and val > 50:
            b.append(val)
        else:
            c.append(val)

    return a, b, c



def main():
    marks = [23, 65, 85, 29, 78, 93, 46, 62, 39]

    A_grade, B_grade, C_grade = segregateMarks(marks)

    print(f"A grade students are {A_grade}")
    print(f"B grade students are {B_grade}")
    print(f"C grade students are {C_grade}")


    
if __name__ == "__main__":
    main()
