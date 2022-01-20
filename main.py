#terms[side of "="][term][modifer sign key, varible, coefficient, modifer 1, 2, 3...]
#Each modfier is formated as a term

equation = input("Equation: ")
equal = 0
co_add = False

terms = [[[[],"",0]], [[[],"",0]]]
# Inital Formating
for x in range(2):
  def coefficient(co, terms, co_add):
    if terms[y][-1][0]==[]:
      if (terms[y][-1][1] != "" or co != "") and terms[y][-1][2] == 0:
        if co == "" or co == "-":
          co += "1"
        terms[y][-1][2] = float(co)
    elif (terms[y][-1][-1][0][1] != "" or not co_add) and terms[y][-1][-1][0][2] == 0:
      if co == "" or co == "-":
        co += "1"
      terms[y][-1][-1][0][2] = float(co)

  a, co, co_add = equal+x, "", False
  while a < len(equation):
    # Layering for ()
    if len(terms)==2:
      y = x
    else:
      y = -1

    # Check for "="
    if x==1 and equal==0:
      break
    elif equation[a] == "=":
      equal = a
      break

    # Setting coefficient
    if equation[a] not in ".0123456789" and equation[a-1] not in "+-)":
      coefficient(co, terms, co_add)
      co_add = False
      co = ""

    # +, -
    if equation[a] in "+-":
      if  equation[a+1] != "(":
        # 2 * -3
        if equation[a-1] in "*/" and equation[a]=="-":
          co += equation[a]
        # 2 + -3
        if equation[a] + equation[a+1] == "+-":
          co += equation[a+1]
          a += 1
        # 2 - 3
        elif equation[a]=="-":
          co += equation[a]
        # New term
        if a>0 and equation[a-1]+equation[a] != "(-":
          terms[y].append([[],"",0])
      

    # *, /
    elif equation[a] in "*/":
      # Add sign to key, and term to back of existing
      terms[y][-1][0].append(equation[a])
      terms[y][-1].append([[[], "",0]])

    # (
    elif equation[a] == "(":
      # 2*(3+3) | 2/(3+3)
      if equation[a-1] in "*/":
        del terms[y][-1][-1]
      # 2-(3+3)
      elif equation[a-1] == "-":
        terms[y].append([["*"], "", -1])
      # 2(3+3)
      elif equation[a-1] != "+":
        terms[y][-1][0].append("*")
      # Go down layer
      terms.append([[[],"",0]])

    # )
    elif equation[a] == ")":
      # For double () and side control
      if len(terms)>3:
        z = -2
      else:
        z = x
      # 2*(3+3) | 2/(3+3) | 2(3+3)
      if len(terms[z][-1][0])>len(terms[z][-1])-3:
        terms[z][-1].append(terms[y])
      # 2+(3+3) | 2-(3+3)
      else:
        terms[z].append(terms[y])
      # Go up layer
      del terms[y]

    # If coefficient or varible
    elif equation[a] != "=":
      # If coefficient
      if equation[a] in ".0123456789":
        co += equation[a]
      # If varible
      else:
        # For term
        if terms[y][-1][0]==[]:
          terms[y][-1][1] = terms[y][-1][1]+equation[a]
        # For modifing term
        else:
          terms[y][-1][-1][-1][1] = terms[y][-1][-1][-1][1]+equation[a]
    a += 1

  # Setting coefficient
  if (equation[a-1] in ".0123456789" or terms[y][-1][1]!="") and equation[a-1] not in "+-)" and (x+equal>1 or x+equal==0):
    coefficient(co, terms, co_add)
print(terms)

def print_eq():
  eq = []
  # Number Check: See if number can be int
  def numc(num):
    if num%1==0:
      return str(int(num))
    return str(num)
  # Prints modifing terms
  def inner(term):
    if len(term)==1:
      inner(term[0])
    # If term is single term
    elif isinstance(term[1], str):
      # If no modifers
      if term[0]==[]:
        if len(eq)!=0 and eq[-1] not in "+-*/(=":
          eq.append("+")
        eq.append(numc(term[2])+term[1])
      # If modifers -> check modifing terms; par control
      else:
        eq.append(numc(term[2])+term[1])
        for c in range(len(term[0])):
          eq.append(term[0][c])
          if len(term[c+3])>1:
            eq.append("(")
            inner(term[c+3])
            eq.append(")")
          else:
            inner(term[c+3])
    # If term is the sum of others terms check each term
    else:
      for d in range(len(term)):
        inner(term[d])
        if d+1 != len(terms) and eq[-1] not in "+-*/(=":
          eq.append("+")

  # Main Loop
  for x in range(2):
    inner(terms[x])
    if x==0:
      eq.append("=")

  # Print Loop
  for a in eq:
    print(a, end="")
  print()

def simplify():
  def inner(term):
    # For side start and modifer nesting
    if len(term)==1:
      term = inner(term[0])
    # If selected is term and not sum of terms
    elif len(term)>=3 and isinstance(term[1], str):
      if term[0] != []:
        c = 0
        while c < len(term[0]):
          # Single term * /
          if len(term[c+3])==1 and term[c+3][0][0]==[]:
            if term[1]=="" or term[c+3][0][1]=="":
              if term[0][c]=="*":
                term[2] = term[2]*term[c+3][0][2]
              elif term[0][c]=="/":
                term[2] = term[2]/term[c+3][0][2]
              if term[1]=="":
                term[1] = term[c+3][0][1]
              del term[c+3]
              del term[0][c]
            else:
              c += 1
          else:
            # Distributive / extended fracton
            if len(term[c+3])>1 and len(term[0])==1:
              dist_check = True
              for f in range(len(term[c+3])):
                if term[1]=="" or term[c+3][f][1] == "":
                  dist_check = dist_check
                else:
                  dist_check = False
              if dist_check:
                for g in range(len(term[c+3])):
                  if term[0][0]=="*":
                    term[c+3][g][2] = term[2]*term[c+3][g][2]
                  elif term[0][0]=="/":
                    term[c+3][g][2] = term[2]/term[c+3][g][2]
                  term[c+3][g][1] = term[1]+term[c+3][g][1]
                term = inner(term[c+3])
                break
                
            # If modifing term is also modified
            else:
              term = inner(term[c+3])
    # If sum of terms -> Add terms
    else:
      d = 0
      while d < len(term):
        print(term, d)
        e = 0
        if len(term[d]) == 3 and isinstance(term[d][1], str):
          while e < len(term):
            if d != e:
              if  len(term[e]) == 3 and isinstance(term[e][1], str):
                if term[d][1]==term[e][1]:
                  term[d][2] = term[d][2]+term[e][2]
                  del term[e]
              elif isinstance(term[d][1], list) or (isinstance(term[d][1], str) and term[d][0] != []):
                term = inner(term[e])
            e += 1
        elif isinstance(term[d][1], list) or (isinstance(term[d][1], str) and term[d][0] != []):
            term = inner(term[d])
        d += 1
    return(term)
  # Main Loop
  for x in range(2):
    terms[x] = inner(terms[x])

simplify()
print_eq()