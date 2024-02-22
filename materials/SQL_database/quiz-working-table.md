1. Em uma tabela chamada Cliente de um banco de dados padrão SQL aberto e em condições ideais há o campo idCliente do tipo inteiro e chave primária. Há também o campo nomeCliente que é do tipo varchar. Nessa tabela, um gerente deseja alterar o nome do cliente de id 1 para 'Barbara Paz’'. Para isso, terá que utilizar o comando:

*Escolha somente UMA resposta*


A) ALTER TABLE Cliente SET nomeCliente=’Barbara Paz' WHERE idCliente=1;

B) UPDATE Cliente SET nomeCliente='Barbara Paz' WHERE idCliente=1;

C) UPDATE nomeCliente TO 'Barbara Paz' FROM Cliente WHERE idCliente=1;

D) ALTER TABLE Cliente FIELD nomeCliente='Barbara Paz' WHERE idCliente=1;

E) UPDATE TABLE Cliente FIELD nomeCliente='Barbara Paz' WHERE idCliente=1;


2. Assinale a alternativa com o uso correto do comando Insert do SQL:

*Escolha somente UMA resposta*

A) INSERT (CODIGO, NOME, SALARIO, SECAO) VALUES(1, "LUCKY LUCIANO", 120, 1) INTO EMPREGADOS

B) INSERT INTO EMPREGADOS VALUES(1, "LUCKY LUCIANO", 120, 1) (CODIGO, NOME, SALARIO, SECAO)

C) INSERT INTO EMPREGADOS(CODIGO, NOME, SALARIO, SECAO)

D) INSERT INTO EMPREGADOS (CODIGO, NOME, SALARIO, SECAO) VALUES (1, "LUCKY LUCIANO", 120, 1)

3. O gerente pediu a exclusão de alguns clientes com id: 1, 10, 20 , qual a estrutura de comando será necessário realizar, levando em consideração que pode ser executado mais de uma vez:

*Escolha somente UMA resposta*

A) DELETE FROM clientes FROM id(1, 10, 20);

B) DELETE FROM clientes WHERE id = 1;

C) DROP FROM clientes WHERE id = 1;

D) DROP FROM usuários WHERE id = 1;
