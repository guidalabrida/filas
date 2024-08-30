# Aluno: Guilherme Dalabrida
# Modelagem e Simulação de Sistemas

import pandas as pd

class Cliente:
    def __init__(self, id_cliente, tempo_chegada, duracao_atendimento):
        self.id_cliente = id_cliente
        self.tempo_chegada = tempo_chegada
        self.duracao_atendimento = duracao_atendimento
        self.inicio_atendimento = 0
        self.termino_atendimento = 0
        self.tempo_espera = 0

def sistema_de_filas():
    try:
        # Entrada de dados pelo usuário
        num_clientes = int(input("Digite o número de clientes: "))
        
        intervalos_chegada = []
        print("\nDigite os intervalos de chegada (em minutos):")
        for i in range(num_clientes):
            intervalo = float(input(f"Intervalo entre a chegada do cliente {i+1} e {i+2}: ")) if i < num_clientes - 1 else 0
            intervalos_chegada.append(intervalo)
        
        duracoes_atendimento = []
        print("\nDigite as durações de atendimento (em minutos):")
        for i in range(num_clientes):
            duracao = float(input(f"Duração do atendimento do cliente {i+1}: "))
            duracoes_atendimento.append(duracao)
        
        # Criação e processamento da lista de clientes
        clientes = []
        tempo_chegada_acumulado = 0
        
        for i in range(num_clientes):
            tempo_chegada_acumulado += intervalos_chegada[i-1] if i > 0 else 0
            cliente = Cliente(
                id_cliente = i + 1,
                tempo_chegada = tempo_chegada_acumulado,
                duracao_atendimento = duracoes_atendimento[i]
            )
            
            if i == 0:
                cliente.inicio_atendimento = cliente.tempo_chegada
            else:
                cliente.inicio_atendimento = max(cliente.tempo_chegada, clientes[i-1].termino_atendimento)
            
            cliente.termino_atendimento = cliente.inicio_atendimento + cliente.duracao_atendimento
            cliente.tempo_espera = cliente.inicio_atendimento - cliente.tempo_chegada
            
            clientes.append(cliente)
        
        # Cálculos das métricas
        intervalo_medio_chegada = sum(intervalos_chegada[:-1]) / (num_clientes - 1) if num_clientes > 1 else 0
        duracao_media_atendimento = sum(duracoes_atendimento) / num_clientes
        tempo_total_simulacao = clientes[-1].termino_atendimento
        tempo_total_espera = sum(cliente.tempo_espera for cliente in clientes)
        tamanho_medio_fila = tempo_total_espera / tempo_total_simulacao if tempo_total_simulacao > 0 else 0
        tempo_medio_espera = tempo_total_espera / num_clientes
        
        # Criação da tabela de funcionamento
        dados_tabela = {
            'Cliente': [cliente.id_cliente for cliente in clientes],
            'Tempo de Chegada': [cliente.tempo_chegada for cliente in clientes],
            'Início do Atendimento': [cliente.inicio_atendimento for cliente in clientes],
            'Término do Atendimento': [cliente.termino_atendimento for cliente in clientes],
            'Tempo de Espera na Fila': [cliente.tempo_espera for cliente in clientes]
        }
        
        tabela_funcionamento = pd.DataFrame(dados_tabela)
        
        # Apresentação dos resultados
        print("\n--- Resultados ---")
        print(f"Intervalo Médio entre Chegadas: {intervalo_medio_chegada:.2f} minutos")
        print(f"Duração Média do Atendimento: {duracao_media_atendimento:.2f} minutos")
        print(f"Tamanho Médio da Fila: {tamanho_medio_fila:.2f} clientes")
        print(f"Tempo Médio de Espera na Fila: {tempo_medio_espera:.2f} minutos")
        
        print("\n--- Tabela de Funcionamento do Sistema ---")
        print(tabela_funcionamento.to_string(index=False))
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    sistema_de_filas()
