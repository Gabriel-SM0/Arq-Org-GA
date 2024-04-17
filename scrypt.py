from FileReader import FileReader
from OneFetchStep import OneFetchStep
from TwoDecodeStep import TwoDecodeStep
from TreExecutionStep import TreExecutionStep
from FourMemoryStep import FourMemoryStep
from FiveWriteStep import FiveWriteStep


print("Hello, World!");


#######################################
def main(): 
    content = FileReader()
    content.readFile("teste.txt")

    print(content.returnContent())

    oneFetchStep = OneFetchStep("add","add","add","add","add")
    twoDecodeStep = TwoDecodeStep("add","add","add","add","add")
    treExecutionStep = OneFetchStep("add","add","add","add","add")
    OneFetchStep = OneFetchStep("add","add","add","add","add")
    OneFetchStep = OneFetchStep("add","add","add","add","add")

########################################




if __name__ == "__main__":
    main()
