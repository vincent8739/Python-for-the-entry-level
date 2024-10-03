import learning

def main():

    p2=learning.Person.getPerson("name=帥哥")
    print(p2.bmi_print())

if __name__=="__main__":
    main()
