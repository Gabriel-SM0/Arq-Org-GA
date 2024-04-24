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



PLUSSS

Busca (Fetch):
Neste estágio, a próxima instrução a ser executada é buscada na memória de instruções.
O endereço da próxima instrução é geralmente mantido em um registrador especial chamado Contador de Programa (PC).
A instrução buscada é colocada no início do pipeline para ser processada nos estágios subsequentes.

Decodificação (Decode):
A instrução buscada é decodificada para determinar sua operação e operandos.
O opcode da instrução é extraído e usado para identificar o tipo de instrução e as operações necessárias.
Os operandos são identificados e, se necessário, lidos do banco de registradores.

Execução (Execute):
Neste estágio, a instrução é executada.
Isso pode envolver operações aritméticas, lógicas, de controle de fluxo, etc., dependendo do tipo de instrução.
Para operações aritméticas, os operandos podem ser processados aqui.
Para instruções de desvio condicional, a condição é avaliada e, se verdadeira, o desvio é tomado.

Acesso à Memória (Memory Access):
Se a instrução envolve acesso à memória (por exemplo, leitura ou escrita), isso acontece neste estágio.
Isso inclui acesso à memória de dados para instruções de carga e armazenamento.
Para algumas arquiteturas, como a arquitetura MIPS, instruções de carga e armazenamento podem ser divididas em estágios separados de acesso à memória e conclusão do acesso à memória.

Escrita do Resultado (Write-back):
O resultado da instrução é escrito de volta no banco de registradores.
Para instruções que produzem um resultado (por exemplo, operações aritméticas), esse estágio é onde o resultado é armazenado no registrador apropriado.
Para instruções que não produzem um resultado (por exemplo, instruções de desvio), esse estágio ainda pode ser usado para limpar ou preparar o pipeline para a próxima instrução.






Na primeira não faz nada.
Na segunda não faz nada.
Na terceira ele vai calcular qual a posição do dado que ele deve pegar
Na quarta ele vai pegar o dado na memoria
Na quinta ele pega o dado que ele pegou na quarta e joga pros registradores

