from calculadora_horas import calcular_horas_trabalhadas_com_intervalo

if __name__ == "__main__":
  horario_inicio = input("Digite o horário de início (HHMM): ")
  horario_termino = input("Digite o horário de término (HHMM): ")
  duracao_intervalo = input("Digite a duração do intervalo (em minutos): ")

  horas_trabalhadas = calcular_horas_trabalhadas_com_intervalo(
      horario_inicio, horario_termino, duracao_intervalo)

  if isinstance(horas_trabalhadas, str):
    print(horas_trabalhadas)
  else:
    print(
        f"Horas trabalhadas no dia (com desconto do intervalo): {horas_trabalhadas:.2f} horas"
    )
