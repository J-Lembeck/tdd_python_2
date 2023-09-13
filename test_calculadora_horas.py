from calculadora_horas import calcular_horas_trabalhadas_com_intervalo


def test_calculo_horas_trabalhadas_sem_intervalo():
  resultado = calcular_horas_trabalhadas_com_intervalo("0800", "1730", 0)
  assert resultado == 9.5


def test_calculo_horas_trabalhadas_com_intervalo():
  resultado = calcular_horas_trabalhadas_com_intervalo("0800", "1730", 30)
  assert resultado == 9


def test_inverter_horarios_inicio_e_termino():
  resultado = calcular_horas_trabalhadas_com_intervalo("1700", "0800", 30)
  assert resultado == 8.5


def test_inserir_horarios_sem_dois_pontos():
  resultado = calcular_horas_trabalhadas_com_intervalo("0800", "1730", 30)
  assert resultado == 9


def test_formato_de_hora_invalido():
  resultado = calcular_horas_trabalhadas_com_intervalo("0800", "2560", 30)
  assert resultado == "Formato de hora inválido. Use o formato HHMM (24 horas) para horários."
