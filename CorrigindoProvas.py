respostas = []
alunos = []
pontos = [0, 0, 0]
print('RESPOSTAS CERTAS:')
for rc in range(0, 5):
	respostas.append(str(input(f'Questão {rc+1}: ')))
for ra in range(0, 3):
	alunos.append(str(input('Qual o seu nome: ')))
	print(f'Aluno {alunos[ra]}')
	for q in range(0, 5):
		r_aluno = str(input(f'Resposta da questão {q+1}: '))
		if r_aluno == respostas[q]:
			pontos[ra] += 2

for infor in range(0, 3):
	print(f'{alunos[infor]}, com {pontos[infor]} pontos')
