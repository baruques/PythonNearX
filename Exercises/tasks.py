def readfile(file_path: str) -> list:
    """
    Lê um arquivo de texto e retorna uma lista de tarefas (linhas).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as arquivo:
            tarefas = [linha.strip() for linha in arquivo]
        return tarefas
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

def writefile(file_path: str, tarefas: list):
    """
    Escreve uma lista de tarefas (strings) em um arquivo de texto.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as arquivo:
            for tarefa in tarefas:
                arquivo.write(str(tarefa) + "\n")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")
    