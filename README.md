Especificação do Trabalho  GA 2
Organização e Arquitetura de Computadores
Objetivos:  Comprovar a melhora do desempenho do processador com a utilização de um mecanismo de predição e reforçar os conceitos de funcionamento do pipeline.

Resultado Esperado:  Um índice em porcentagem da melhora do desempenho (compara a execução do mesmo código com e sem mecanismo de predição).

O que é necessário implementar:

Primeira Entrega - Um simulador com os 5 estágios do pipeline, que tenha as seguintes funcionalidades.
- Leitura da memória de programa (arquivo texto com instruções para um vetor de instruções).
- Simulador de pipeline com 5 estágios (busca, decodificação, execução, memória e escrita do resultado).
- Banco de registradores com R0 a R31 (R0 fixo em zero).
- Utiliza uma política fixa para instruções de desvio condicional
- Mecanismo de invalidação da instrução se a execução do desvio for incorreta

Instruções Suportadas:
ADD, ADDI, SUB, SUBI, BEQ, J

Sugestão da struct de instrução:
Struct {
	Opcode
	Op1
	Op2
Op3
Valida
}

Banco de registradores:
Unsigned int R[32];


Segunda Entrega - Acrescentar no simulador desenvolvido o algoritmo de predição escolhido.
- Mecanismo de predição que indica qual a próxima instrução a ser buscada (se ativado manipula PC)
- Mecanismo de verificação do acerto da predição e  atualização da tabela de predição ( estágio de execução, quando já  se tem o resultado da instrução condicional)
- Mecanismo de invalidação da instrução se a predição foi incorreta
- Possibilidade de desabilitar a predição
- Estatísticas de  instruções executadas e   instruções inválidas buscadas


Tabela de predição:
Unsigned char  predicao[32];
