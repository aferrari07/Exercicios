def conta_vogais(string):
    string = string.lower() 
    result = {}
    vogais = ['a','e','i','o','u']
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result
print(conta_vogais('olaaa'))
def test_econta_vogaisx01():
  print ('First_last6')
  assert conta_vogais('') == {'i':1,'o':1}
  assert conta_vogais('') =={'u':1,'a':1}
  assert conta_vogais('') =={'a':1,'e':1,'u':1}
  assert conta_vogais('') =={'u':1,'o':1}
