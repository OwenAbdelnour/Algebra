equation = input("Equation")
equal = 0

terms = [[[[],"","+"]], [[[],"","+"]]]
for x in range(2):
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
    
    # +, -
    if equation[a] in "+-":
      # Check if making new term
      if (len(terms[y][-1][0]) == 0 or terms[y][-1][-1][1] != "+") and equation[a+1] != "(":
        # Two signs
        if equation[a+1] in "+-":
           # 2 + +3 | 2 + -3
          if equation[a] == "+":
            terms[y].append([[],"",equation[a+1]])
          # 2 + +3 | 2 - +3
          elif equation[a+1] == "+":
            terms[y].append([[],"",equation[a]])
          # 2 - -3
          else:
            terms[y].append([[],"","+"])
          a += 1
        # One sign
        else:
          # 2 + 3 | 2 - 3
          terms[y].append([[],"",equation[a]])
      # Modifing existing term
      else:
        if terms[y][-1][-1][1]+equation[a] == "+-":
          terms[y][-1][-1][1] = "-"
        elif terms[y][-1][-1][1]+equation[a] == "--":
          terms[y][-1][-1][1] = "+"

    # *, /
    elif equation[a] in "*/":
      # Add sign to key, and term to back of existing
      terms[y][-1][0].append(equation[a])
      terms[y][-1].append([[], "","+"])

    # (
    elif equation[a] == "(":
      # Save sign before "(", and go down layer
      par_enter = equation[a-1]
      terms.append([[[],"","+"]])
    
    # )
    elif equation[a] == ")":
      # x+(1+1)
      if par_enter == "+":
        terms[x].append(terms[y][0])
      # x-(1+1)
      elif par_enter == "-":
        terms[x].append([["*"], "", "-1", terms[y][0]])
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

    # Add number or varible to term
    elif equation[a] != "=":
      # For coefficient or varible
      if len(terms[y][-1][0])==0:
        # Coefficient
        if equation[a] in "0123456789":
          terms[y][-1][2] = terms[y][-1][2]+equation[a]
        # Varible
        else:
          terms[y][-1][1] = terms[y][-1][1]+equation[a]
      # For modifer(*, /) coefficient or varible
      else:
        # Coefficient
        if equation[a] in "0123456789":
          terms[y][-1][-1][2] = terms[y][-1][-1][1]+equation[a]
        # Varible
        else:
          terms[y][-1][-1][1] = terms[y][-1][-1][0]+equation[a]
    a += 1
print(terms)

for x in range(2):
  for a in range(len(terms[x])):
    if len(terms[x][a][0]) == 0:
      if terms[x][a][2] == "+":
        terms[x][a][2] = 1
      elif terms[x][a][2] == "-":
        terms[x][a][2] = -1
    else:
      pass

def print_eq():
  pass