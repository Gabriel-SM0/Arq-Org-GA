from FileReader import FileReader
from OneFetchStep import OneFetchStep
from PipeLineMananger import PipeLineMananger



print("Hello, World!");


#######################################
def main(): 
    content = FileReader()
    content.readFile("teste.txt")
    pipeline_manager = PipeLineMananger()
    pipeline_manager.importPipeLine(content.returnContent())



    # Exibir o conteúdo do pipeline (para fins de verificação)
    print("Instructions:")
    for instr in pipeline_manager.instructions:
        print(instr)

    print("Memory:")
    print(pipeline_manager.memory)



########################################


    while True:
        # Aguarda o pressionamento da tecla "Enter"
        input("Pressione Enter para avançar a pipeline...")

        # Avança a pipeline
        pipeline_manager.advance_pipeline()

        # Exibe o estado atual da pipeline
        pipeline_manager.print_pipeline_state()

if __name__ == "__main__":
    main()
