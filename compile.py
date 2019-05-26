import variable as var

class Compile():
  def __init__(self, agents):
    self.space=0
    self.err = []
    self.agents = agents ### danh sách tên các agent tồn tại
  def setSrc(self, srcCode=None):
    self.src = self.cutSrc(srcCode)
    self.current_index = 0
    self.syntax_tree = self.check_syntax()
    print(self.syntax_tree)
    self.check_meaning(self.syntax_tree['value'])

  def trans(self, src):
    self.setSrc(src)
    return self.transToPython(self.syntax_tree['value'], 0)
  def transToPython(self, tokens, space):
    space = space
    result = ''
    for token in tokens:
      for x in range(space):
        result = result + '  '
      if token['type'] == 'command':
        for y in token['value']:
          result = result + y['value']
          result = result + ' '
      if token['type'] == 'if_clause' or token['type'] == 'while_clause':
        result = result + token['value'][0]['value']
        result = result + ' '
        result+= self.transExpression(token['value'][1])
        result = result + ' '
        result = result + ':'
        result = result + '\n'
        result += str(self.transToPython(token['value'][2]['value'], space +1))
        if len(token['value']) > 3:
          i = 3
          while i < len(token['value']):
            if token['value'][i]['type'] == 'keyword_elif':
              result = result + token['value'][i]['value']
              result = result + ' '
              result+= self.transExpression(token['value'][i+1])
              result = result + ' '
              result = result + ':'
              result = result + '\n'
              result += str(self.transToPython(token['value'][i+2]['value'], space +1))
              i+=3
            elif token['value'][i]['type'] == 'keyword_else':
              result = result + token['value'][i]['value']
              result = result + ' '
              result = result + ':'
              result = result + '\n'
              result += str(self.transToPython(token['value'][i+1]['value'], space +1))
              i+=2
      if token['type'] == 'call_method':
        result+= token['value'][0]['value']
        result+= '.'
        for y in token['value'][1:]:
          if y['type'] == 'params':
            result+='('
            for x in y['value']:
              if x['type'] == 'expression':
                result += str(self.transExpression(x))
              else:
                result = result + x['value']
              if x != y['value'][-1]:
                result += ','
            result+=')'
          else :
            result = result + y['value']
      result = result + '\n'
    return result
  def transExpression(self, expression):
    result = ''
    if expression['type'] == 'expression':
      for i in expression['value']:
        if i['type'] == 'math_expression':
          result += str(self.transMathExpression(i))
          result += ' '
        else:
          result += str(i['value'])
          result += ' '
    return result
  def transMathExpression(self, math_expression):
    result = ''
    if math_expression['type'] == 'math_expression':
      for i in math_expression['value']:
        if i['type'] == 'term':
          result += str(self.transTerm(i))
          result += ' '
        else:
          result += str(i['value'])
          result += ' '
    return result
  def transTerm(self, term):
    result = ''
    if term['type'] == 'term':
      for i in term['value']:
        result += str(i['value'])
        result += ' '
    return result
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
        while command[i] != '/n':
          i+=1
        status = i
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
      elif command[0] == '.':
        tokens.append({'type': 'sb_point', 'value': command[0]})
        status = 1
      elif command[0] == ',':
        tokens.append({'type': 'sb_comma', 'value': command[0]})
        status = 1
      elif command[0] == '\"':
        i = 1
        while i< len(command) and command[i] != '\"':
          i+=1
        status = i + 2
        tokens.append({'type': 'string', 'value': '\"'+command[1:i]+'\"'})
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
      elif command[0] == "\n":
        tokens.append({'type': 'sb_newline', 'value': '\n'})
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
          tokens.append({'type': 'keyword_'+ var.keyword[token], 'value': token })
        else:
          tokens.append({'type': 'indent', 'value': command[0:i]})
      non_cut = command
      command = non_cut[status:len(non_cut)]
    return tokens

  def check_syntax(self):
    content = []
    while self.current_index < len(self.src):
      content.append(self.check_command())
    return {'type': 'syntax_tree', 'value': content}
  def check_block(self):
    content = []
    if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_blockopen':
      self.current_index += 1
      while self.current_index < len(self.src) and self.src[self.current_index]['type'] != 'sb_blockclose':
        content.append(self.check_command())
      if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_blockclose':
        self.current_index += 1
      else :
        self.err.append("No have close block")
    else :
      self.err.append("No have open block")
    if content == [] :
      self.err.append("Block must have content")
    return {'type': 'block', 'value': content}

  def check_command(self):
    content = []
    ##########if clause##################################################
    if self.src[self.current_index]['type'] == 'keyword_if':
      content.append(self.src[self.current_index])
      self.current_index += 1
      content.append(self.check_expression())
      content.append(self.check_block())
      while self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_newline':
        self.current_index += 1
      while self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'keyword_elif':
        content.append(self.src[self.current_index])
        self.current_index += 1
        content.append(self.check_expression())
        content.append(self.check_block())
      while self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_newline':
        self.current_index += 1
      if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'keyword_else':
        content.append(self.src[self.current_index])
        self.current_index += 1
        content.append(self.check_block())
      return {'type': 'if_clause', 'value': content}
    ################### while clause #######################################
    elif self.src[self.current_index]['type'] == 'keyword_while':
      content.append(self.src[self.current_index])
      self.current_index += 1
      content.append(self.check_expression())
      content.append(self.check_block())
      return {'type': 'while_clause', 'value': content}
    ###################### call method #################################
    elif self.src[self.current_index]['type'] == 'indent':
      if self.current_index+1 < len(self.src) and self.src[self.current_index+1]['type'] == 'sb_point':
        content.append(self.src[self.current_index])
        self.current_index += 2
        if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'keyword_method':
          content.append(self.src[self.current_index])
          self.current_index += 1
          content.append(self.check_params())
          return {'type': 'call_method', 'value': content}
        else:
          self.err.append("Not have method name")
      elif self.current_index+1 < len(self.src) and self.src[self.current_index+1]['type'] == 'keyword_method':
        content.append(self.src[self.current_index])
        content.append(self.src[self.current_index+1])
        self.current_index += 2
        content.append(self.check_params())
        return {'type': 'call_method', 'value': content}
      else :
        while self.current_index < len(self.src) and self.src[self.current_index]['type'] != 'sb_newline' and self.src[self.current_index]['type'] != 'sb_blockclose':
          content.append(self.src[self.current_index])
          self.current_index += 1
        if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_newline':
          self.current_index += 1
        return {'type': 'command', 'value': content}
    ############################### other ########################################
    else:
      while self.current_index < len(self.src) and self.src[self.current_index]['type'] != 'sb_newline' and self.src[self.current_index]['type'] != 'sb_blockclose':
        content.append(self.src[self.current_index])
        self.current_index += 1
      if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_newline':
        self.current_index += 1
      return {'type': 'command', 'value': content}
  def check_params(self):
    content = []
    if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_exopen':
      self.current_index += 1
      while self.current_index < len(self.src) and self.src[self.current_index]['type'] != 'sb_exclose':
        content.append(self.check_expression())
        if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_comma':
          self.current_index += 1
          continue
        else:
          break
      if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_exclose':
        self.current_index += 1
    else :
      while self.current_index < len(self.src) and self.src[self.current_index]['type'] != 'sb_newline':
        content.append(self.check_expression())
        if self.current_index < len(self.src) and self.src[self.current_index]['type'] == 'sb_comma':
          self.current_index += 1
          continue
        else:
          break
    return {'type': 'params', 'value': content}
  def check_expression(self):
    content = []
    content.append(self.check_math_ex())
    symbols = ["keyword_and", "keyword_or", "sb_eq", "sb_lt", "sb_gt", "sb_lte", "sb_gte", "sb_noteq"]
    while self.current_index < len(self.src) and (self.src[self.current_index]['type'] in symbols):
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
    return {'type': 'math_expression', 'value': content}
  def check_term(self):
    content = []
    content.append(self.check_operand())
    while self.current_index < len(self.src) and (self.src[self.current_index]['type'] == 'sb_time' or self.src[self.current_index]['type'] == 'sb_slash'):
      content.append(self.src[self.current_index])
      self.current_index += 1
      content.append(self.check_operand())
    return {'type': 'term', 'value': content}
  def check_operand(self):
    type = ['indent', 'number', 'expression', 'string']
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
######################################### phân tích ngữ nghĩa ###########################################
  def check_meaning(self, tokens):
    for x in tokens:
      if x['type'] == 'call_method':
        self.check_call_method_mean(x)
        if self.get_params_amount(x) != var.params_amount[x['value'][1]['value']]:
          self.err.append("Params amount is wrong. Must have " + str(var.params_amount[x['value'][1]['value']]) +' param' )
      elif x['type'] == 'if_clause' or x['type'] == 'while_clause':
        if x['value'][1]['type'] == 'block':
          self.check_meaning(x['value'][1]['value'])

  def get_params_amount(self, x):
    if x['value'][2]['type'] == 'params':
      return len(x['value'][2]['value'])
    else:
      return -1
  def check_call_method_mean(self, x):
    if self.check_agent_name(x['value'][0]['value']) == False:
      self.err.append('not exist agent  ' + x['value'][0]['value'])
  def check_agent_name(self, name):
    if name == 'env' or name in self.agents:
      return True
    else:
      return False
#########################################################################################################
# agents = ['sensor1', 'actuator']
# compile = Compile(agents)
# src = "left = sensor1.getValue()\n if left != \"#F6F6F6\" {actuator run \n} elif left != \"#F6F6F6\" {actuator run \n}  "
# compile.setSrc(src)
# print(compile.transToPython(compile.syntax_tree['value'], 0))
# print(compile.err)
