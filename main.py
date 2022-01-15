equation = input("Equation")
divide = 0
print("test")
terms = [[[]]]
for a in range(2):
  for b in range(divide, len(equation)):
    if a==1:
      if divide==0:
        break
      elif len(terms)==1:
        terms.append([[]])
    elif equation[b] == "=":
      divide = b
      break
    if equation[b] in "+*/":
      terms[a].append([])
    elif equation[b]!="=":
      terms[a][len(terms[a])-1].append(equation[b])
  

  

print(terms)

"""
def combine_coefficients(terms):
  for a in range(len(terms)):
    co, num_spot, var = 0, 1, ""
    for b in range(len(terms[a])-1,-1,-1):
      if terms[a][b] in "123456789":
        if num_spot==1:
          co += int(terms[a][b])
        else:
          co += int(terms[a][b])*num_spot
        terms[a].remove(terms[a][b])
        num_spot *= 10
      elif terms[a][b] == "0":
        terms[a].remove(terms[a][b])
        num_spot *= 10
      elif terms[a][b] == "-":
        terms[a].remove(terms[a][b])
        co *= -1
      else:
        var += terms[a][b]
        terms[a].remove(terms[a][b])
    if co!=0:
      terms[a].insert(0, co)
    if var != "":
      terms[a].insert(1, var)
combine_coefficients(lerms)
if divide != -1:
  combine_coefficients(rerms)

def like_terms():
  def combine(terms):
    a = 0
    while a<len(terms):
      b = 0
      while b<len(terms):
        if a != b:
          if len(terms[a])==1 and len(terms[b])==1:
            terms.append([terms[a][0]+terms[b][0]])
            terms.pop(a)
            b -= 1
            terms.pop(b)
          elif len(terms[a])>1 and len(terms[b])>1 and terms[a][1]==terms[b][1]:
            terms.append([terms[a][0]+terms[b][0], terms[a][1]])
            terms.pop(a)
            b -= 1
            terms.pop(b)
        b += 1
      a += 1
  combine(lerms)
  if divide != -1:
    combine(rerms)
like_terms()
print(lerms)
if divide != -1:
  print(rerms)

def add_sub(term1, term2):
  pass

def multiply(term1, term2):
  pass

def divide(term1, term2):
  pass
"""