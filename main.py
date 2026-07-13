import subprocess


# v_f = v_i + a*t
# v_i = v_f-a*t
# a = (v_f-v_i)/t
# t = (v_f-v_i)/a
def linearmotion(v_f=None, v_i=None, a=None, t=None):
    subprocess.run("clear")
    variables = [v_f, v_i, a, t]
    if sum(v is not None for v in variables) < 3:
        subprocess.run("clear")
        input(
            "You need to provide at least three of the four variables (v_f, v_i, a, t). Press enter to continue.\n"
        )
        main()
    for i in variables:
        if i is not None:
            if type(i) is not float:
                subprocess.run("clear")
                input(
                    "Variables should either be type None or Float. Press enter to continue.\n"
                )
                main()

    finalresult = None

    if v_f is None:
        if v_i is not None and a is not None and t is not None:
            try:
                finalresult = v_i + (a * t)
            except ZeroDivisionError:
                print(f"{v_i} + ({a}*{t})")
                input("Divide by zero error. Press enter to continue.\n")
                main()
            except Exception as err:
                subprocess.run("clear")
                input(f"Error: {err}\n\nPress enter to continue.\n")
                main()
            print(f"Velocity final (v_f): {finalresult} m/s")
            input("\n\nPress enter to continue\n")
            main()
    elif v_i is None:
        if v_f is not None and a is not None and t is not None:
            try:
                finalresult = v_f - (a * t)
            except ZeroDivisionError:
                print(f"{v_f} - ({a}*{t})")
                input("Divide by zero error. Press enter to continue.\n")
                main()
            except Exception as err:
                subprocess.run("clear")
                input(f"Error: {err}\n\nPress enter to continue.\n")
                main()
            print(f"Velocity initial (v_i): {finalresult} m/s")
            input("\n\nPress enter to continue\n")
            main()
    elif a is None:
        if v_f is not None and v_i is not None and t is not None:
            try:
                finalresult = (v_f - v_i) / t
            except ZeroDivisionError:
                print(f"({v_f}-{v_i})/{t}")
                input("Divide by zero error. Press enter to continue.\n")
                main()
            except Exception as err:
                subprocess.run("clear")
                input(f"Error: {err}\n\nPress enter to continue.\n")
                main()
            print(f"Acceleration (a): {finalresult} m/s²")
            input("\n\nPress enter to continue\n")
            main()
    elif t is None:
        if v_f is not None and v_i is not None and a is not None:
            try:
                finalresult = (v_f - v_i) / a
            except ZeroDivisionError:
                print(f"({v_f}-{v_i})/{a}")
                input("Divide by zero error. Press enter to continue.\n")
                main()
            except Exception as err:
                subprocess.run("clear")
                input(f"Error: {err}\n\nPress enter to continue.\n")
                main()
            print(f"Time (t): {finalresult} s")
            input("\n\nPress enter to continue\n")
            main()


# main loop


def main():
    subprocess.run("clear")
    print("Python Physics\n\nChoose an operation\n\n1. Linear Motion\n2. Quit\n")
    choice = input()
    if choice == "1":
        subprocess.run("clear")
        print("Linear motion (Horizontal. Gravity doesn't apply.)\n")
        v_f = input("v_f=")
        v_i = input("v_i=")
        a = input("a=")
        t = input("t=")

        if v_f == "":
            v_f = None
        else:
            try:
                v_f = float(v_f)
            except Exception:
                subprocess.run("clear")
                input("You must provide a number or leave the variable blank.")
                main()
        if v_i == "":
            v_i = None
        else:
            try:
                v_i = float(v_i)
            except Exception:
                subprocess.run("clear")
                input("You must provide a number or leave the variable blank.")
                main()
        if a == "":
            a = None
        else:
            try:
                a = float(a)
            except Exception:
                subprocess.run("clear")
                input("You must provide a number or leave the variable blank.")
                main()
        if t == "":
            t = None
        else:
            try:
                t = float(t)
            except Exception:
                subprocess.run("clear")
                input("You must provide a number or leave the variable blank.")
                main()

        linearmotion(v_f=v_f, v_i=v_i, a=a, t=t)
    elif choice == "2":
        subprocess.run("clear")
        quit()
    else:
        subprocess.run("clear")
        input("Invalid choice. Press enter to continue.")
        main()


main()
