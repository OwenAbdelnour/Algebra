#terms[side of "="][term][modifer sign key, varible, coefficient, modifer 1, 2, 3...]
#Each modfier is formated as a term

equation = input("Equation")
equal = 0


terms = [[[[],"",0]], [[[],"",0]]]
par_key = [[], []]
for x in range(2):
  co = ""
  a = equal+x
  while a < len(equation):

    # Layering for ()
    if len(terms)==2:
      y = x
    else:
      y = -1

    # Check for "="
    if x==1 and equal == 0:
        break
    elif equation[a] == "=":
      equal = a
      break

    # Setting coefficient
    if equation[a] not in "0123456789":
      if co == "":
        if co == "-":
          co = "-1"
        else:
          co = "1"
      if len(terms[y][-1][0])==0:
        if (terms[y][-1][1] != "" or "1" not in co) and terms[y][-1][2] == 0:
          terms[y][-1][2] = int(co)
      elif (terms[y][-1][-1][1] != "" or "1" not in co) and terms[y][-1][-1][2] == 0:
        terms[y][-1][-1][2] = int(co)
      co = ""

    # +, -
    if equation[a] in "+-":
      if (len(terms[y][-1][0]) == 0 or terms[y][-1][-1][2] != 0) and equation[a+1] != "(":
        if equation[a+1] in "+-":
          # 2 + +3 | 2 + -3
          if equation[a] == "+":
            co += equation[a+1]
          # 2 + +3 | 2 - +3
          elif equation[a+1] == "+":
            co += equation[a]
          a += 1
        # 2 - 3
        elif equation[a]=="-":
          co += equation[a]
        # New term
        print("run")
        terms[y].append([[],"",0])
      # 2 * -3
      elif equation[a] == "-":
          co += equation[a]

    # *, /
    elif equation[a] in "*/":
      # Add sign to key, and term to back of existing
      terms[y][-1][0].append(equation[a])
      terms[y][-1].append([[], "",0])

    # (
    elif equation[a] == "(":
      # Go down layer, and save sign before "("
      terms.append([[[],"",0]])
      par_enter = equation[a-1]
    
    # )
    elif equation[a] == ")":
      # x+(1+1)
      if par_enter == "+":
        terms[x].append(terms[y][0])
      # x-(1+1)
      elif par_enter == "-":
        terms[x].append([["*"], "", -1, terms[y][0]])
      # x*(1+1) | # x/(1+1)
      elif par_enter in "*/":
        del terms[x][-1][-1]
        terms[x][-1].append(terms[y][0])
      # x(1+1)
      else:
        terms[x][-1][0].append("*")
        terms[x][-1].append(terms[y][0])
      # Go up layer
      del terms[y]

    # If coefficient or varible
    elif equation[a] != "=":
      # If coefficient
      if equation[a] in "0123456789":
        co += equation[a]
      # If varible
      else:
        # For term
        if len(terms[y][-1][0])==0:
          terms[y][-1][1] = terms[y][-1][1]+equation[a]
        # For modifing term
        else:
          terms[y][-1][-1][1] = terms[y][-1][-1][1]+equation[a]
    a += 1

  # Setting coefficient
  if equation[a-1] in "0123456789":
    if co == "":
      if co == "-":
        co = "-1"
      else:
        co = "1"
    if len(terms[y][-1][0])==0:
      if (terms[y][-1][1] != "" or (co != "1" and co != "-1")) and terms[y][-1][2] == 0:
        terms[y][-1][2] = int(co)
    elif (terms[y][-1][-1][1] != "" or (co != "1" and co != "-1")) and terms[y][-1][-1][2] == 0:
      terms[y][-1][-1][2] = int(co)
print(terms)

def print_eq():
  for x in range(2):
    for a in range(len(terms[x])):
      