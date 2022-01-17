#terms[side of "="][term][modifer sign key, varible, coefficient, modifer 1, 2, 3...]
#Each modfier is formated as a term

equation = input("Equation")
equal = 0
co_add = False

terms = [[[[],"",0]], [[[],"",0]]]
par_sign = []
# Inital Formating
for x in range(2):
  co = ""
  co_add = False
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
    if equation[a] not in ".0123456789" and equation[a-1] not in "+-)":
      if co == "":
        if co == "-":
          co = "-1"
        else:
          co = "1"
        co_add = True
      if len(terms[y][-1][0])==0:
        if (terms[y][-1][1] != "" or not co_add) and terms[y][-1][2] == 0:
          terms[y][-1][2] = float(co)
      elif (terms[y][-1][-1][1] != "" or not co_add) and terms[y][-1][-1][2] == 0:
        terms[y][-1][-1][2] = float(co)
      co_add = False
      co = ""

    # +, -
    if equation[a] in "+-":
      if equation[a]+equation[a+1] != "-(":
        if terms[y][-1][0] == [] or terms[y][-1][-1][2] != 0:
          # 2 + -3
          if equation[a] + equation[a+1] == "+-":
            co += equation[a+1]
            a += 1
          # 2 - 3
          elif equation[a]=="-":
            co += equation[a]
          # New term
          if equation[a-1]+equation[a] != "(-":
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
      if equation[a-1] != "+":
        # Check if () change PEMDAS order
        for b in range(a+1, len(equation)+1):
          if equation[b]==")":
            break
          # If change: go down layer, and save sign before "("
          elif equation[b] not in ".-0123456789":
            terms.append([[[],"",0]])
            par_sign.append(equation[a-1])
            break

    # )
    elif equation[a] == ")":
      if len(par_sign)!=0 and len(par_sign)==len(terms)-2:
        # For double () and side control
        if len(terms)>3:
          z = -2
        else:
          if x == 0:
            z = 0
          else:
            z = 1
        # If + in ()
        if len(terms[y])==1:
          par_term = terms[y][0]
        else:
          par_term = terms[y]    
        # x-(1+1)
        if par_sign[len(terms)-3] == "-":
          terms[z].append([["*"], "", -1, par_term])
        else:
          # x*(1+1) | # x/(1+1)
          if par_sign[len(terms)-3] in "*/":
            del terms[z][-1][-1]
          # x(1+1)
          else:
            terms[z][-1][0].append("*")
          terms[z][-1].append(par_term)
        # Go up layer
        del par_sign[-1]
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
  if equation[a-1] in ".0123456789" and equation[a-1] not in "+-)" and (x+equal>1 or x+equal==0):
    if co == "":
      if co == "-":
        co = "-1"
      else:
        co = "1"
      co_add = True
    if len(terms[y][-1][0])==0:
      if (terms[y][-1][1] != "" or not co_add) and terms[y][-1][2] == 0:
        terms[y][-1][2] = float(co)
    elif (terms[y][-1][-1][1] != "" or not co_add) and terms[y][-1][-1][2] == 0:
      terms[y][-1][-1][2] = float(co)
print(terms)



def print_eq():
  eq = []
  # Number Check: See if number can be int
  def numc(num):
    if num%1==0:
      return str(int(num))

  # Prints modifing terms
  def nest(term):
    # If term is single term
    if isinstance(term[1], str):
      # If no modifers
      if term[0]==[]:
        if len(eq)!=0 and eq[-1] not in "+-*/(":
          eq.append("+")
        eq.append(numc(term[2])+term[1])
      # If modifers -> check modifing terms; par control
      else:
        eq.append(numc(term[2])+term[1])
        for c in range(len(term[0])):
          eq.append(term[0][c])
          if (term[c+3][0]!=[] and isinstance(term[c+3][1], str)) or isinstance(term[c+3][1], list):
            eq.append("(")
            nest(term[c+3])
            eq.append(")")
          else:
            nest(term[c+3])
    # If term is the sum of others terms check each term
    else:
      for d in range(len(term)):
        nest(term[d])
        if d+1 != len(terms) and eq[-1] not in "+-*/(":
          eq.append("+")

  # Main Loop
  for x in range(1):
    for a in range(len(terms[x])):
      nest(terms[x][a])

  # Print Loop
  for a in eq:
    print(a, end="")
  print()
print_eq()