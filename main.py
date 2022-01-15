equation = input("Equation")
equal = 0

terms = [[[]]]
for x in range(2):
  for a in range(equal, len(equation)):
    if x==1:
      if equal==0:
        break
      elif len(terms)==1:
        terms.append([[]])
    elif equation[a] == "=":
      equal = a
      break
    if equation[a] in "+*/":
      terms[x].append([])
    elif equation[a]!="=":
      terms[x][len(terms[x])-1].append(equation[a])

for x in range(len(terms)):
  for a in range(len(terms[x])):
    co, num_spot, var = 0, 1, ""
    for b in range(len(terms[x][a])-1,-1,-1):
      if terms[x][a][b] in "123456789":
        if num_spot==1:
          co += int(terms[x][a][b])
        else:
          co += int(terms[x][a][b])*num_spot
        terms[x][a].remove(terms[x][a][b])
        num_spot *= 10
      elif terms[x][a][b] == "0":
        terms[x][a].remove(terms[x][a][b])
        num_spot *= 10
      elif terms[x][a][b] == "-":
        terms[x][a].remove(terms[x][a][b])
        co *= -1
      else:
        var += terms[x][a][b]
        terms[x][a].remove(terms[x][a][b])
    if co!=0:
      terms[x][a].insert(0, co)
    if var != "":
      terms[x][a].insert(1, var)

def combine():
  for x in range(len(terms)):
    a = 0
    while a<len(terms[x]):
      b = 0
      while b<len(terms[x]):
        if a != b:
          if len(terms[x][a])==1 and len(terms[x][b])==1:
            if terms[x][a][0]+terms[x][b][0] != 0:
              terms[x].append([terms[x][a][0]+terms[x][b][0]])
            terms[x].pop(a)
            b -= 1
            terms[x].pop(b)
          elif len(terms[x][a])>1 and len(terms[x][b])>1 and terms[x][a][1]==terms[x][b][1]:
            if terms[x][a][0]+terms[x][b][0] != 0:
              terms[x].append([terms[x][a][0]+terms[x][b][0], terms[x][a][1]])
            terms[x].pop(a)
            b -= 1
            terms[x].pop(b)
        b += 1
      a += 1

def add_sub(term):
  for x in range(len(terms)):
    terms[x].append([term])

def multiply(term):
  pass

def divide(term):
  pass

combine()
while True:
  task = input("Run: ")
  term = int(input("Term: "))
  if task == "add_sub":
    add_sub(term)
  print(terms)