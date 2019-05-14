import variable as var

class Compile():
  def __init__(self):
    self.space=0
    self.err = []
  def setSrc(self, srcCode=None):
    self.src = self.cutSrc(srcCode)
    self.current_index = 0

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
        if i == 1:
          tokens.append({'type': 'number', 'value': int(command[0])})
        else :
          tokens.append({'type': 'number', 'value': int(command[0:i-1])})
      else:
        i = 0
        while(i<len(command) and (command[i].isalpha() or command[i].isdigit())):
          i+=1
        status = i
        token = command[0:i]
        if token in var.keyword:
          tokens.append({'type': 'keyword_'+ token, 'value': var.keyword[token] })
        else:
          tokens.append({'type': 'indent', 'value': command[0:i]})
      non_cut = command
      command = non_cut[status:len(non_cut)]
    return tokens

  def check_syntax(self):
    content = []
    while self.src[self.current_index] != []:
      command_lines.append(self.check_command())
  def check_command(self):
    content = []
    if self.current_syntax[0]['type'] == 'keyword_if':
  def check_expression(self):
    content = []
    content.append(self.check_math_ex())
    while self.current_index < len(self.src) and (self.src[self.current_index]['type'] == 'keyword_and' or self.src[self.current_index]['type'] == 'keyword_or'):
      content.append(self.src[self.current_index])
      self.current_index += 1
      content.append(self.check_math_ex())
    return {'type': 'expression', 'value': content}
  def check_math_ex(self):
    content = []
    content.append(self.check_term())
    while self.current_index < len(self.src) and (self.src[self.current_index]['type'] == 'sb_plus' or self.src[self.current_index]['type'] == 'sb_minus') :
      content.append(self.src[self.current_index])
      self.current_index += 1
      content.append(self.check_term())
    for x in content:
      print(x)
    return {'type': 'math_expression', 'value': content}
  def check_term(self):
    content = []
    content.append(self.check_operand())
    while self.current_index < len(self.src) and (self.src[self.current_index]['type'] == 'sb_time' or self.src[self.current_index]['type'] == 'sb_slash'):
      print(self.src[self.current_index])
      content.append(self.src[self.current_index])
      self.current_index += 1
      content.append(self.check_operand())
    return {'type': 'term', 'value': content}
  def check_operand(self):
    type = ['indent', 'number', 'expression']
    if self.src[self.current_index]['type'] in type :
      self.current_index += 1
      return self.src[self.current_index-1]
    elif self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_exopen':
      self.current_index += 1
      self.check_expression()
      if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_exclose':
        self.current_index += 1
      else :
        self.err.append('Not close )')
    else:
      self.err.append('There must operand')
compile = Compile()
src = " a+b*c/d and 6"
compile.setSrc(src)
compile.check_expression()
