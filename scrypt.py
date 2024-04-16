from FileReader import FileReader


print("Hello, World!");


#######################################
def main(): 
    content = FileReader()
    content.readFile("teste.txt")

    print(content.returnContent())


########################################
#test


if __name__ == "__main__":
    main()
