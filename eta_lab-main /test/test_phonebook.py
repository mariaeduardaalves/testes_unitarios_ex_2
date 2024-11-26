from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_nome_vazio(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.add(None, '100')
        assert resultado == resultado_esperado

    def test_add_nome_diferente_string(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.add(1452, '100')
        assert resultado == resultado_esperado

    def test_add_numero_vazio(self):
        phonebook = Phonebook()
        resultado_esperado = 'Numero invalido'
        resultado = phonebook.add('Maria', None)
        assert resultado == resultado_esperado

    def test_add_numero_diferente_string(self):
        phonebook = Phonebook()
        resultado_esperado = 'Numero invalido'
        resultado = phonebook.add('Maria', 100)
        assert resultado == resultado_esperado

    def test_add_entrada_nao_existente(self):
        phonebook = Phonebook()
        resultado_esperado = 'Numero adicionado'
        resultado = phonebook.add("matheus", '800')
        assert resultado == resultado_esperado

    def test_add_nome_com_caracteres_invalidos(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.add('Jo@o', '100')
        assert resultado == resultado_esperado

    def test_add_numero_vazio_com_string(self):
        phonebook = Phonebook()
        resultado_esperado = 'Numero invalido'
        resultado = phonebook.add('Maria', '')
        assert resultado == resultado_esperado

    def test_add_nome_com_espacos(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.add('   ', '100')
        assert resultado == resultado_esperado

    def test_add_numero_com_espacos(self):
        phonebook = Phonebook()
        resultado_esperado = 'Numero invalido'
        resultado = phonebook.add('Maria', '   ')
        assert resultado == resultado_esperado

    def test_add_nome_duplicado(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '200')  # Adiciona a entrada
        resultado_esperado = 'Numero adicionado'
        resultado = phonebook.add('Joao', '300')  # Tenta adicionar o mesmo nome
        assert resultado == resultado_esperado

    # Testes para o método lookup
    def test_lookup_nome_vazio(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.lookup(None)
        assert resultado == resultado_esperado

    def test_lookup_nome_existente(self):
        phonebook = Phonebook()
        resultado_esperado = '190'
        resultado = phonebook.lookup("POLICIA")
        assert resultado == resultado_esperado

    def test_lookup_nome_com_espacos(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.lookup("   ")
        assert resultado == resultado_esperado

    def test_lookup_nome_nao_existente(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.lookup("matheus")
        assert resultado == resultado_esperado

    def test_lookup_caractere_invalido_hashtag(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.lookup("matheus#")
        assert resultado == resultado_esperado

    def test_lookup_caractere_invalido_arroba(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.lookup("matheus@")
        assert resultado == resultado_esperado

    def test_lookup_caractere_invalido_exclamacao(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.lookup("matheus!")
        assert resultado == resultado_esperado

    def test_lookup_caractere_invalido_cifrao(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.lookup("matheus$")
        assert resultado == resultado_esperado

    def test_lookup_caractere_invalido_percentual(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.lookup("matheus%")
        assert resultado == resultado_esperado

    def test_get_names_vazio(self):
        phonebook = Phonebook()
        resultado_esperado = ['POLICIA']  # Apenas a entrada inicial
        resultado = phonebook.get_names()
        assert resultado == resultado_esperado

    def test_get_names_com_entradas(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')
        resultado_esperado = ['POLICIA', 'Joao', 'Maria']
        resultado = phonebook.get_names()
        assert resultado == resultado_esperado

    def test_get_names_duplicado(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Joao', '67890')  # Nome duplicado não deve ser adicionado
        resultado_esperado = ['POLICIA', 'Joao']
        resultado = phonebook.get_names()
        assert resultado == resultado_esperado

    def test_get_numbers_vazio(self):
        phonebook = Phonebook()
        resultado_esperado = ['190']  # Apenas o número inicial associado a "POLICIA"
        resultado = phonebook.get_numbers()
        assert resultado == resultado_esperado

    def test_get_numbers_com_entradas(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')
        resultado_esperado = ['190', '12345', '67890']
        resultado = phonebook.get_numbers()
        assert resultado == resultado_esperado

    def test_get_numbers_com_numero_duplicado(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '12345')  # Mesmo número para um nome diferente
        resultado_esperado = ['190', '12345', '12345']  # Duplicatas são permitidas
        resultado = phonebook.get_numbers()
        assert resultado == resultado_esperado

    def test_clear_phonebook_nao_vazio(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')

        resultado_esperado = 'phonebook limpado'
        resultado = phonebook.clear()
        assert resultado == resultado_esperado
        assert phonebook.entries == {}  # Verifica se o phonebook está vazio

    def test_clear_phonebook_vazio(self):
        phonebook = Phonebook()

        resultado_esperado = 'phonebook limpado'
        resultado = phonebook.clear()
        assert resultado == resultado_esperado
        assert phonebook.entries == {}  # Verifica se o phonebook está vazio

    def test_search_nome_invalido(self):
        phonebook = Phonebook()
        resultado_esperado = 'Nome invalido'
        resultado = phonebook.search(123)  # Busca com valor não-string
        assert resultado == resultado_esperado

    def test_search_substring_existente(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')
        phonebook.add('Mariana', '54321')

        resultado_esperado = [('Maria', '67890'), ('Mariana', '54321')]
        resultado = phonebook.search('Mari')
        assert resultado == resultado_esperado

    def test_search_substring_nao_existente(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')

        resultado_esperado = []  # Nenhuma correspondência
        resultado = phonebook.search('Pedro')
        assert resultado == resultado_esperado

    def test_search_case_insensitive(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')

        resultado_esperado = [('Maria', '67890')]
        resultado = phonebook.search('mari')  # Busca com diferença de caso
        assert resultado == resultado_esperado

    def test_search_nome_vazio(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')

        resultado_esperado = [('POLICIA', '190'), ('Joao', '12345'), ('Maria', '67890')]
        resultado = phonebook.search('')  # Busca com substring vazia (retorna tudo)
        assert resultado == resultado_esperado

    def test_get_phonebook_sorted_vazio(self):
        phonebook = Phonebook()
        resultado_esperado = [('POLICIA', '190')]  # Apenas a entrada inicial
        resultado = phonebook.get_phonebook_sorted()
        assert resultado == resultado_esperado

    def test_get_phonebook_sorted_com_entradas(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')
        phonebook.add('Ana', '54321')  # Adiciona nomes fora de ordem

        resultado_esperado = [
            ('Ana', '54321'),
            ('Joao', '12345'),
            ('Maria', '67890'),
            ('POLICIA', '190')
        ]
        resultado = phonebook.get_phonebook_sorted()
        assert resultado == resultado_esperado

    def test_get_phonebook_sorted_com_nomes_duplicados(self):
        phonebook = Phonebook()
        phonebook.add('Ana', '54321')
        phonebook.add('Ana', '12345')  # Nome duplicado substitui o número

        resultado_esperado = [
            ('Ana', '12345'),
            ('POLICIA', '190')
        ]
        resultado = phonebook.get_phonebook_sorted()
        assert resultado == resultado_esperado

    def test_get_phonebook_reverse_vazio(self):
        phonebook = Phonebook()
        resultado_esperado = [('POLICIA', '190')]  # Apenas a entrada inicial
        resultado = phonebook.get_phonebook_reverse()
        assert resultado == resultado_esperado

    def test_get_phonebook_reverse_com_entradas(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')
        phonebook.add('Maria', '67890')
        phonebook.add('Ana', '54321')  # Adiciona nomes fora de ordem

        resultado_esperado = [
            ('POLICIA', '190'),
            ('Maria', '67890'),
            ('Joao', '12345'),
            ('Ana', '54321')
        ]
        resultado = phonebook.get_phonebook_reverse()
        assert resultado == resultado_esperado

    def test_get_phonebook_reverse_ordem_invertida(self):
        phonebook = Phonebook()
        phonebook.add('Cecilia', '11111')
        phonebook.add('Bruno', '22222')
        phonebook.add('Ana', '33333')

        resultado_esperado = [
            ('POLICIA', '190'),
            ('Cecilia', '11111'),
            ('Bruno', '22222'),
            ('Ana', '33333')
        ]
        resultado = phonebook.get_phonebook_reverse()
        assert resultado == resultado_esperado

    def test_delete_nome_existente(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')

        resultado_esperado = 'Numero deletado'
        resultado = phonebook.delete('Joao')
        assert resultado == resultado_esperado
        assert 'Joao' not in phonebook.entries  # Verifica se a entrada foi removida

    def test_delete_nome_inexistente(self):
        phonebook = Phonebook()

        resultado_esperado = 'Nome invalido'
        resultado = phonebook.delete('Maria')  # Nome não existe no phonebook
        assert resultado == resultado_esperado

    def test_delete_nome_vazio(self):
        phonebook = Phonebook()

        resultado_esperado = 'Nome invalido'
        resultado = phonebook.delete('')  # Nome vazio
        assert resultado == resultado_esperado

    def test_delete_nome_com_espacos(self):
        phonebook = Phonebook()

        resultado_esperado = 'Nome invalido'
        resultado = phonebook.delete('   ')  # Nome com espaços
        assert resultado == resultado_esperado

    def test_delete_nome_invalido_tipo(self):
        phonebook = Phonebook()

        resultado_esperado = 'Nome invalido'
        resultado = phonebook.delete(123)  # Nome não é string
        assert resultado == resultado_esperado

    def test_change_number_nome_existente(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')  # Adiciona uma entrada inicial

        resultado_esperado = 'Numero atualizado'
        resultado = phonebook.change_number('Joao', '67890')  # Atualiza o número
        assert resultado == resultado_esperado
        assert phonebook.entries['Joao'] == '67890'  # Verifica se o número foi atualizado

    def test_change_number_nome_inexistente(self):
        phonebook = Phonebook()

        resultado_esperado = 'Nome invalido'
        resultado = phonebook.change_number('Maria', '67890')  # Nome não existe
        assert resultado == resultado_esperado

    def test_change_number_nome_invalido(self):
        phonebook = Phonebook()

        resultado_esperado = 'Nome invalido'
        resultado = phonebook.change_number(123, '67890')  # Nome não é string
        assert resultado == resultado_esperado

    def test_change_number_nome_vazio(self):
        phonebook = Phonebook()

        resultado_esperado = 'Nome invalido'
        resultado = phonebook.change_number('', '67890')  # Nome vazio
        assert resultado == resultado_esperado

    def test_change_number_numero_invalido(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')  # Adiciona uma entrada inicial

        resultado_esperado = 'Numero invalido'
        resultado = phonebook.change_number('Joao', '')  # Número vazio
        assert resultado == resultado_esperado

    def test_get_name_by_number_existente(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')  # Adiciona uma entrada inicial

        resultado_esperado = 'Joao'
        resultado = phonebook.get_name_by_number('12345')
        assert resultado == resultado_esperado

    def test_get_name_by_number_inexistente(self):
        phonebook = Phonebook()
        phonebook.add('Joao', '12345')  # Adiciona uma entrada inicial

        resultado_esperado = 'Numero invalido'
        resultado = phonebook.get_name_by_number('67890')  # Número não existe
        assert resultado == resultado_esperado

    def test_get_name_by_number_numero_vazio(self):
        phonebook = Phonebook()

        resultado_esperado = 'Numero invalido'
        resultado = phonebook.get_name_by_number('')  # Número vazio
        assert resultado == resultado_esperado

    def test_get_name_by_number_numero_invalido(self):
        phonebook = Phonebook()

        resultado_esperado = 'Numero invalido'
        resultado = phonebook.get_name_by_number(12345)  # Número não é string
        assert resultado == resultado_esperado