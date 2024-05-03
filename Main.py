from FileReader import FileReader
from OneFetchStep import OneFetchStep
from PipeLineMananger import PipeLineMananger
from RegisterFile import RegisterFile



print("Hello, World!");


#######################################
def main(): 
    content = FileReader()
    content.readFile("contador10.txt")
    num_registers = 10
    register_file = RegisterFile(num_registers)  # Instancie o banco de registradores
    pipeline_manager = PipeLineMananger(register_file)  # Passe o banco de registradores como argumento
    pipeline_manager.importPipeLine(content.returnContent())



    # Exibir o conteúdo do pipeline (para fins de verificação)
    print("Instructions:")
    for instr in pipeline_manager.instructions:
        print(instr)

    print("Memory:")
    print(pipeline_manager.memory)

    print("Escolha o modo de predição de desvio, 1 para allways false, 2 para predição por histórico (levando em consideração o último desvio):")
    prompt = input("Waiting for value")
    pipeline_manager.setConditionalPreview(prompt);



########################################

    while pipeline_manager.endOfInstructions == False:
        # Aguarda o pressionamento da tecla "Enter"
        input("Pressione Enter para avançar a pipeline...")

        # Avança a pipeline
        pipeline_manager.advance_pipeline()

        # Exibe o estado atual da pipeline
        pipeline_manager.print_pipeline_state()


    print("No more Instructions")
    print("Descarted Instructions: " + str(pipeline_manager.descartedInstruction))
    print("Total runs: " + str(pipeline_manager.totalRuns))

if __name__ == "__main__":
    main()
