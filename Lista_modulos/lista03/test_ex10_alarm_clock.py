# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# J. alarm_clock
# day: 0=domingo, 1=segunda, 2=terça, ..., 6=sábado
# vacation = True caso você esteja de férias
# o retorno é uma string que diz quando o despertador tocará
# dias da semana '07:00'
# finais de semana '10:00'
# a menos que você esteja de férias, neste caso:
# dias da semana '10:00'
# finais de semana 'off'
# alarm_clock(1, False) -> '7:00'
# alarm_clock(5, False) -> '7:00'
# alarm_clock(0, False) -> '10:00'
def alarm_clock(day, vacation):
  week_preset = "7:00" if not vacation else "10:00"
  weekend_preset = "10:00" if not vacation else "off"
  return week_preset if day not in [6,0] else weekend_preset

def test_ex10():
  print ('Alarm Clock')
  assert alarm_clock(1, False) == '7:00'
  assert alarm_clock(5, False) == '7:00'
  assert alarm_clock(0, False) == '10:00'
  assert alarm_clock(6, False) == '10:00'
  assert alarm_clock(0, True) == 'off'
  assert alarm_clock(6, True) == 'off'
  assert alarm_clock(1, True) == '10:00'
  assert alarm_clock(3, True) == '10:00'
  assert alarm_clock(5, True) == '10:00'


