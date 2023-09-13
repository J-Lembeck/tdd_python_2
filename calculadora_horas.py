from datetime import datetime


def calcular_horas_trabalhadas_com_intervalo(inicio, termino,
                                             duracao_intervalo):
  try:
    if len(inicio) != 4 or len(termino) != 4:
      raise ValueError(
          "Formato de hora inválido. Use o formato HHMM (24 horas) para horários."
      )

    hora_inicio, min_inicio = int(inicio[:2]), int(inicio[2:])
    hora_termino, min_termino = int(termino[:2]), int(termino[2:])

    if hora_inicio < 0 or hora_inicio > 23 or min_inicio < 0 or min_inicio > 59:
      raise ValueError(
          "Formato de hora inválido. Use o formato HHMM (24 horas) para horários."
      )
    if hora_termino < 0 or hora_termino > 23 or min_termino < 0 or min_termino > 59:
      raise ValueError(
          "Formato de hora inválido. Use o formato HHMM (24 horas) para horários."
      )

    minutos_inicio = hora_inicio * 60 + min_inicio
    minutos_termino = hora_termino * 60 + min_termino
    diferenca_em_minutos = abs(minutos_termino - minutos_inicio)

    duracao_intervalo = int(duracao_intervalo)

    if duracao_intervalo >= diferenca_em_minutos:
      return 0.00
    horas_trabalhadas = (diferenca_em_minutos - duracao_intervalo) / 60.0

    return horas_trabalhadas

  except ValueError as e:
    return str(e)
