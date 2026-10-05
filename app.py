pessoas = [{'nome':'carlos', 'idade':'143', 'cidade':'goiania'}]
for pessoa in pessoas: 
    nome_pessoa = pessoa['nome']
    idade_pessoa = pessoa['idade']
    cidade_pessoa = pessoa['cidade']
    print(nome_pessoa, idade_pessoa, cidade_pessoa)

pessoas[0]['idade'] = '32'

print(f"Nome: {pessoas[0]['nome']}, Idade: {pessoas[0]['idade']}, Cidade: {pessoas[0]['cidade']}")