class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
    :param name: name of person in string
    :param number: number of person in string
    :return:
        'Nome invalido' - If the name is not a string, contains invalid characters, is empty,
                          or is already in the phonebook.
        'Numero invalido' - If the number is not a string or is empty.
        'Numero adicionado' - If the name and number are valid and successfully added.
    """
        # Valida se o nome e o número são strings
        if not isinstance(name, str):
            return 'Nome invalido'
        if not isinstance(number, str):
            return 'Numero invalido'

        # Verifica se o nome contém caracteres inválidos
        invalid_chars = ['#', '@', '!', '$', '%']
        # Verifica se o nome contém caracteres inválidos
        if any(char in name for char in invalid_chars):
            return 'Nome invalido'

        # Verifica se o name e número é válido (não vazio)
        if len(name.strip()) == 0:
            return 'Nome invalido'
        if len(number.strip()) == 0:
            return 'Numero invalido'

        # Adiciona o nome e o número no dicionário se forem válidos
        self.entries[name] = number
        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        # Verifica se o nome é uma string
        if not isinstance(name, str):
            return 'Nome invalido'

        # Lista de caracteres inválidos
        invalid_chars = ['#', '@', '!', '$', '%']
        # Verifica se o nome contém caracteres inválidos
        if any(char in name for char in invalid_chars):
                return 'Nome invalido'

        # Verifica se o nome é vazio ou contém apenas espaços
        if len(name.strip()) == 0:
            return 'Nome invalido'

        # Verifica se o nome existe no dicionário
        if name in self.entries:
            return self.entries[name]

        # Caso o nome não exista na agenda
        return 'Nome invalido'

    # Busca a lista de nomes
    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())

    # Busca a lista de números
    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())

    # Limpa toda a lista existente
    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    # Procura todos nomes pela chave primária name
    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        if not isinstance(search_name, str):
            return 'Nome invalido'
        # Lista para armazenar resultados
        results = []
        # Itera sobre as entradas no dicionário
        for name, number in self.entries.items():
            if search_name.lower() in name.lower():  # Busca case-insensitive
                results.append((name, number))
        return results

    # Retorna corretamente as entradas em ordem
    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        return sorted(self.entries.items())

    # Retorna corretamente as entradas em ordem reversa
    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        return sorted(self.entries.items(), reverse=True)


    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        # Verifica se o nome é uma string válida
        if not isinstance(name, str) or len(name.strip()) == 0:
            return 'Nome invalido'

        # Verifica se o nome existe no dicionário
        if name not in self.entries:
            return 'Nome invalido'

        # Remove a entrada correspondente
        self.entries.pop(name)
        return 'Numero deletado'

    def change_number(self, name, number):
        """
        Change the number of an existing name in the phonebook.
        :param name: String with name
        :param number: String with new number
        :return: 'Numero atualizado', 'Nome invalido', or 'Numero invalido'
        """
        # Valida se o nome é uma string válida
        if not isinstance(name, str) or len(name.strip()) == 0:
            return 'Nome invalido'

        # Verifica se o número é válido (não vazio e é string)
        if not isinstance(number, str) or len(number.strip()) == 0:
            return 'Numero invalido'

        # Verifica se o nome existe no dicionário
        if name not in self.entries:
            return 'Nome invalido'

        # Atualiza o número associado ao nome
        self.entries[name] = number
        return 'Numero atualizado'

    def get_name_by_number(self, number):
        """
        Retrieve the name associated with a given number in the phonebook.
        :param number: String with the number
        :return: The name associated with the number, or 'Numero invalido'
        """
        # Verifica se o número é válido (não vazio e é string)
        if not isinstance(number, str) or len(number.strip()) == 0:
            return 'Numero invalido'

        # Busca pelo número no dicionário e retorna o nome associado
        for name, num in self.entries.items():
            if num == number:
                return name

        # Se o número não for encontrado
        return 'Numero invalido'


