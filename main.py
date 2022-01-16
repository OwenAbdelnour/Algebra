equation = input("Equation")
equal = 0

terms = [[[[],"","+"]], [[[],"","+"]]]
for x in range(2):
  a = equal+x
  while a < len(equation):
    if len(terms)==2:
      y = x
    else:
      y = -1
    if x==1 and equal == 0:
        break
    elif equation[a] == "=":
      equal = a
      break
    if equation[a] in "+-":
      if (len(terms[y][-1][0]) == 0 or terms[y][-1][-1][1] != "+") and equation[a+1] != "(":
        if terms[y][-1][2] == "+":
          if equation[a] == "-":
            terms[y][-1][2] = "-"
        elif equation[a-1] not in "+-":
          terms[y].append([[],"",equation[a]])
        elif equation[a-1]+equation[a] == "+-":
          terms[y][-1] = [],"","-"
        elif equation[a-1]+equation[a] == "--":
          terms[y][-1] = [],"","+"
      else:
        if terms[y][-1][-1][1]+equation[a] == "+-":
          terms[y][-1][-1][1] = "-"
        elif terms[y][-1][-1][1]+equation[a] == "--":
          terms[y][-1][-1][1] = "+"
    elif equation[a] in "*/":
      terms[y][-1][0].append(equation[a])
      terms[y][-1].append(["","+"])
    elif equation[a] == "(":
      par_enter = equation[a-1]
      terms.append([[[],"","+"]])
    elif equation[a] == ")":
      if par_enter == "+":
        terms[x].append(terms[y][0])
      elif par_enter == "-":
        terms[x].append([["*"], "", "-1", terms[y][0]])
      elif par_enter in "*/":
        del terms[x][-1][-1]
        terms[x][-1].append(terms[y][0])
      else:
        terms[x][-1][0].append("*")
        terms[x][-1].append(terms[y][0])
      del terms[y]
    elif equation[a] != "=":
      if len(terms[y][-1][0])==0:
        if equation[a] in "0123456789":
          terms[y][-1][2] = terms[y][-1][2]+equation[a]
        else:
          terms[y][-1][1] = terms[y][-1][1]+equation[a]
      else:
        if equation[a] in "0123456789":
          terms[y][-1][-1][1] = terms[y][-1][-1][1]+equation[a]
        else:
          terms[y][-1][-1][0] = terms[y][-1][-1][0]+equation[a]
    a += 1
print(terms)