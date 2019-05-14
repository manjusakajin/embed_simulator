import variable as var

class Compile():
  def __init__(self):
    self.space=0
    self.err = []
  def setSrc(self, srcCode=None):
    self.src = self.cutSrc(srcCode)
    print(self.src)

  def cutSrc(self, srcCode=None):
    if srcCode != None:
      splited = self.getTokens(srcCode)
      # for x in range(len(splited)):
      #   if splited[x] != "":
      #     cur = splited[x]
      #     splited[x] = self.getTokens(previous, cur)
      #     previous = splited[x]
      return splited

  def getTokens(self, command=None):
    tokens = []
    while(command != None and command != ''):
      status = 0
      if command[0] == '#':
        i=1
        while command[i] != '\n':
          i+=1
        status = i
      elif command[0] == '\n':
        status = 1
      elif command[0] == '{':
        tokens.append({'type': 'sb_blockopen', 'value': '{'})
        status = 1
      elif command[0] == '}':
        tokens.append({'type': 'sb_blockclose', 'value': '}'})
        status = 1
      elif command[0] == ' ':
        status = 1
      elif command[0] == '+':
        tokens.append({'type': 'sb_plus', 'value': command[0]})
        status = 1
      elif command[0] == '-':
        tokens.append({'type': 'sb_minus', 'value': command[0]})
        status = 1
      elif command[0] == '*':
        tokens.append({'type': 'sb_time', 'value': command[0]})
        status = 1
      elif command[0] == '/':
        tokens.append({'type': 'sb_slash', 'value': command[0]})
        status = 1
      elif command[0] == '>':
        if command[1] == '=':
          tokens.append({'type': 'sb_gte', 'value': '>='})
          status = 2
        else :
          tokens.append({'type': 'sb_gt', 'value': command[0]})
          status = 1
      elif command[0] == '<':
        if command[1] == '=':
          tokens.append({'type': 'sb_lte', 'value': '<='})
          status = 2
        else:
          tokens.append({'type': 'sb_lt', 'value': command[0]})
          status = 1
      elif command[0] == '=':
        if command[1] == '=':
          tokens.append({'type': 'sb_eq', 'value': '=='})
          status = 2
        else:
          tokens.append({'type': 'sb_assign', 'value': command[0]})
          status = 1
      elif command[0] == '!':
        if command[1] == '=':
          tokens.append({'type': 'sb_noteq', 'value': '!='})
          status = 2
        else:
          self.err.append('syntax error : not use !')
          status = 1
          break
      elif command[0] == '(':
        tokens.append({'type': 'sb_exopen', 'value': '('})
        status = 1
      elif command[0] == ')':
        tokens.append({'type': 'sb_exclose', 'value': ')'})
        status = 1
      elif command[0] == '[':
        tokens.append({'type': 'sb_listopen', 'value': '['})
        status = 1
      elif command[0] == ']':
        tokens.append({'type': 'sb_listclose', 'value': ']'})
        status = 1
      elif command[0].isdigit():
        i = 0
        while(i<len(command) and command[i].isdigit()):
          i+=1
        status = i
        tokens.append({'type': 'number', 'value': float(command[0:i-1])})
      else:
        i = 0
        while(i<len(command) and (command[i].isalpha() or command[i].isdigit())):
          i+=1
        status = i
        token = command[0:i]
        if token in var.keyword:
          tokens.append({'type': 'keyword', 'value': var.keyword[token] })
        else:
          tokens.append({'type': 'indent', 'value': command[0:i]})
      non_cut = command
      command = non_cut[status:len(non_cut)]
      print(command)
    return tokens

  def check_syntax(self, tokens):
    stack = []
    x=0
    while x < len(tokens):
      stack.append(tokens[x])
      combine = -1
      while combine != 0 :
        combine = 0
        for y in range(stack):
          if check_case(stack[y:]) != None:
            stack = stack[0:y-1] + check_case(stack[y:])
            combine +=1
            break
      x+=1
    return stack

  def check(self, case):
    if case[0]['type'] == 'ident':
      if case[1]['type'] == 'sb_eq':
        x = check_expression(case[2:])
      if case[1]['type'] == 'sb_listopen':
        x = 
    return x
