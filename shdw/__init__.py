import random as r
import os
import io
try:
  import pygame
  import pyfiglet
  from replit import db
  import requests
  import ShdwDB
except ModuleNotFoundError:
  userpip = input('Do you use pip or pip3?: ')
try:
  import pygame
  import pygame.locals as GUI_keys
except ModuleNotFoundError:
  os.system(userpip +  ' install pygame')
try:
  import pyfiglet
except ModuleNotFoundError:
  os.system(userpip + ' install pyfiglet')
try:
  from replit import db
except ModuleNotFoundError:
  os.system(userpip + ' install replit')
try:
  import requests
except ModuleNotFoundError:
  os.system(userpip + ' install requests')
import time
clock = time
try:
  import ShdwDB as DB
except ModuleNotFoundError:
  os.system(userpip + ' install ShdwDB')
#print('Type "view()" to view all the functions.')
zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
nums = [zero, one, two, three, four, five, six, seven, eight, nine]
def init_pygame(width, height, title):
  pygame.init()
  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption(title)
  return screen
GUI = pygame
GUI_events = pygame.event
GUI_out = GUI.draw
GUI_clock = GUI.time
GUI_change = GUI.transform
def show_text(screen, msg, x, y, color, bold=False, italic=False, size=20):
  pygame.font.init()
  font = pygame.font.SysFont('monospace', size, bold, italic)
  text = font.render(msg, True, color)
  screen.blit(text, (x, y))
  return text
def colorize(image, newColor):
  image = image.copy()
  image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
  image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
  return image
def __():
  pass
def ask(screen, question, x, y, end_to_do=__):
  up = {
    '`':'~',
    '1':'!',
    '2':'@',
    '3':'#',
    '4':'$',
    '5':'%',
    '6':'^',
    '7':'&',
    '8':'*',
    '9':'(',
    '0':')',
    '-':'_',
    '=':'+',
    '[':'{',
    ']':'}',
    '\\':'|',
    ';':':',
    "'":'"',
    ',':'<',
    '.':'>',
    '/':'?'
  }
  answer = ''
  upper = False
  breaker = False
  cursor = False
  while True:
    time.sleep(0.5)
    if breaker:
      end_to_do()
      GUI.display.update()
      break
    screen.fill((0, 0, 0))
    show_text(screen, question, x, y, (255, 255, 255))
    show_text(screen, answer, x, y+32, (255, 255, 255))
    GUI.display.update()
    if cursor:
      GUI.font.init()
      font = GUI.font.SysFont('freesans', 20)
      text = font.render('|', True, (167, 167, 167))
      screen.blit(text, (len(answer) * 12, y+32))
    GUI.display.update()
    for event in GUI.event.get():
      if event.type == GUI_keys.QUIT:
        GUI.quit()
        exit()
      if event.type == GUI_keys.KEYDOWN:
        if event.key == GUI_keys.K_RETURN:
          breaker = True
        elif event.key == GUI_keys.K_BACKSPACE:
          listed = list(answer)
          try:
            listed[-1] = ''
          except IndexError:
            pass
          answer = ''.join(listed)
        elif 'shift' in GUI.key.name(event.key):
          upper = True
        elif event.key == GUI_keys.K_SPACE:
          answer += ' '
        elif len(GUI.key.name(event.key)) > 1:
          pass
        else:
          if upper:
            if GUI.key.name(event.key) in up:
              answer += up[GUI.key.name(event.key)]
            else:
              answer += GUI.key.name(event.key).capitalize()
            upper = False
          else:
            answer += GUI.key.name(event.key)
        screen.fill((0, 0, 0))
        show_text(screen, question, x, y, (255, 255, 255))
        show_text(screen, answer, x, y+32, (255, 255, 255))
        GUI.display.update()
    if cursor:
      cursor = False
    else:
      cursor = True
  return answer
setattr(GUI_out, 'text', show_text)
setattr(GUI_change, 'colorize', colorize)
setattr(GUI.display, 'input', ask)
setattr(GUI_keys, 'K_ARROWS', [GUI_keys.K_UP, GUI_keys.K_LEFT, GUI_keys.K_DOWN, GUI_keys.K_RIGHT])
k = GUI_keys
setattr(GUI_keys, 'K_LETTERS', [k.K_a, k.K_b, k.K_c, k.K_d, k.K_e, k.K_f, k.K_g, k.K_h, k.K_i, k.K_j, k.K_k, k.K_l, k.K_m, k.K_n, k.K_o, k.K_p, k.K_q, k.K_r, k.K_s, k.K_t, k.K_u, k.K_v, k.K_w, k.K_x, k.K_y, k.K_z])
setattr(GUI_keys, 'K_NUMBERS', [k.K_1, k.K_2, k.K_3, k.K_4, k.K_5, k.K_6, k.K_7, k.K_8, k.K_9, k.K_0])
del k
setattr(GUI_keys, 'K_WASD', [GUI_keys.K_w, GUI_keys.K_a, GUI_keys.K_s, GUI_keys.K_d])
def url_load(url):
  c = requests.get(url).content
  c = io.BytesIO(c)
  return GUI.image.load(c)
setattr(GUI.image, 'url_load', url_load)
GUI.__doc__ = 'Shdw\'s GUI system has many attributes of the pygame module(https://pypi.org/project/pygame/) and attributes of its own.'
GUI_change.__doc__ = GUI_change.__doc__.replace('pygame', 'Shdw GUI').replace('module', 'section')
GUI_clock.__doc__ = GUI_clock.__doc__.replace('pygame', 'Shdw GUI').replace('module', 'section')
GUI_events.__doc__ = GUI_events.__doc__.replace('pygame', 'Shdw GUI').replace('module', 'section')
GUI_keys.__doc__ = GUI_keys.__doc__.replace('PyGame', 'Shdw GUI').replace('module', 'file')
GUI_out.__doc__ = GUI_out.__doc__.replace('pygame', 'Shdw GUI').replace('module', 'section')
class GUI_colors:
  red = (255, 0, 0)
  green = (0, 255, 0)
  blue = (0, 0, 255)
  pink = (255, 0, 255)
  cyan = (0, 255, 255)
  yellow = (255, 255, 0)
  def gray(x=256/2):
    return (x, x, x)
  black = (0, 0, 0)
  white = (255, 255, 255)

def sublists(list1=[], list2=[]) -> list:
  for i in list1:
    for j in list2:
      if i == j:
        list1.remove(i)
  return list1

def mergelists(list1, list2) -> list:
  for ite in list2:
    if ite not in list1:
      list1.append(ite)
  return list1

def sublist_example():
  print('All of list2\'s elements will be removed from list1 then return the new list1.')


def requester():
  """
  Do not use. This is only for Shdw.
  """
  usr = input('Username: ')
  pwd = input('pwd: ')
  if usr == 'Shdw' and pwd == 'S-h-d-w-BOOM':
    r = requests.get("https://client.shivankchhaya.repl.co/requests", data={'update':'\x1b[0;32mUpdate Alert! Please go to the original repl for update.'})
    print(r.text)
  #u = requests.head('http://192.168.86.38/Users/deepchhaya1/Documents/flask_web_app/flaskr.py')
  #print(u.text)


def empty(what):
  if what == str:
    return ''
  elif what == int:
    return 0
  elif what == list:
    return []
  elif what == dict:
    return {}
  elif what == tuple:
    return ()
  elif what == bool:
    return False
  elif what == set:
    return set()
  elif what == 'function':
    return __
  elif what == 'any':
    return None


class replitdb:
  """
  Use this for the repl.it database
  """
  def store(key, value):
    db[key] = value
  def get(key):
    return db[key]
  def delit(key):
    del db[key]
  def allkeys():
    return db.keys()
  def allvalues():
    return db.values()


#Make a color pattern. Use the ANSI escape codes for colors, and you have to use four colors.
def flashcol(text, col1, col2, col3, col4):
  lentxt = 0
  while lentxt < len(text):
    lentxt += 1
    if lentxt % 4 == 0:
      color = col1
    elif lentxt % 4 == 1:
      color = col2
    elif lentxt % 4 == 2:
      color = col3
    elif lentxt % 4 == 3:
      color = col4
    print(color + text[lentxt - 1], end='')
  print()
class num_makers:
  """
  Create numbers.
  """
  #Make a two-digit number
  def twodigit(num1, num2):
      num3 = str(num1) + str(num2)
      return int(num3)
  #Make a three-digit number
  def threedigit(num1, num2, num3):
      num4 = str(num1) + str(num2) + str(num3)
      return int(num4)
  #Make a four-digit number
  def fourdigit(num1, num2, num3, num4):
      num5 = str(num1) + str(num2) + str(num3) + str(num4)
      return int(num5)
class files:
  """
  File operations.
  """
  #Find how many lines in a file
  def linesinfile(file):
      fillo = open(file)
      lenger = fillo.readlines()
      return len(lenger)
  #Save some text in a file. Have mode='a' for appending text, mode='w' for overwriting the file, and mode='x' for creating a new file
  def save_to_file(file, whattosave, mode):
    filo = open(file, mode)
    filo.write(whattosave)
  #Delete files
  def clearfiles(f1, f2=None, f3=None, f4=None, f5=None, f6=None):
    a = [f1]
    if f2 != None:
      a.append(f2)
    if f3 != None:
      a.append(f3)
    if f4 != None:
      a.append(f4)
    if f5 != None:
      a.append(f5)
    if f6 != None:
      a.append(f6)
    lena = len(a)
    while lena > 0:
      lena -= 1
      import os
      os.remove(a[lena])
class randoms:
  """
  Useless but Useful functions.
  """
  def series(st):
    a = st + 1
    b = a * 2
    c = b + 3
    d = c * 4
    e = d + 5
    f = e * 6
    g = f + 7
    h = g * 8
    i = h + 9
    j = i * 10
    return j
  def wrdnums(num):
      import random as r
      for n in range(1, num+1):
        print(r.randint(1, n), end=', ')
      print(num)
  def chattify(word):
    if len(word) >= 3:
      word = word.split()[0]
      if word == 'why' or word == 'you':
        word = word[-1]
      elif 'h' == word[0]:
        word = word.strip('h')
      elif 'ing' == word.strip(word[:-3]):
        word = word.strip(word[-1])
      else:
        vowels = ['a', 'e', 'i', 'o', 'u']
        word = list(word)
        for i in vowels:
          if i in word:
            word.remove(i)
        word = ''.join(word)
    return word
#Replace the first item in a list, replace all with mode='all'
def replace(list, element, put_in, mode='first'):
  if mode == 'first':
    eleinde = list.index(element)
    list.insert(eleinde, put_in)
    list.remove(element)
    return list
  elif mode == 'all':
    while element in list:
      eleinde = list.index(element)
      list.insert(eleinde, put_in)
      list.remove(element)
    return list
#Length of something
def length():
    ace = input("Type Something: ")
    print("The length of that is {0}.".format(len(ace)))
#Division
def div(num1, num2):
    bdf = num1/num2
    print("Your first number divided by your second is {0}. As a fraction it is {1}/{2}.".format(bdf, num1, num2))
#Multiplication
def mult(num1, num2):
    ceg = num1*num2
    print("Your first number multiplied by your second is {0}.".format(ceg))
#Addition
def add(num1, num2):
    dfh = num1+num2
    print("Your first number added to your second is {0}.".format(dfh))
#Subtraction
def sub(num1, num2):
    egi = num2-num1
    print("Your first number subtacted from your second is {0}.".format(egi))
#Modulus
def mod(num1, num2):
    hub = num1 % num2
    print('Your first number divided by your second\'s remainder is {0}.'.format(hub))
#Math function Chooser
def mathypleep():
    hjl = input('[1]Divide, [2]Multiply, [3]Add, [4]Subtract, [5]Exponent, [6]Modulus: ')
    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))
    if int(hjl) == 1:
        div(num1, num2)
    if int(hjl) == 2:
        mult(num1, num2)
    if int(hjl) == 3:
        add(num1, num2)
    if int(hjl) == 4:
        sub(num1, num2)
    if int(hjl) == 5:
        exponent(num1, num2)
    if int(hjl) == 6:
        mod(num1, num2)
#Outputs to the console
def text(str):
    print(str)
#Asks a question
def question(str):
    fhj = input(str)
    print("You said, \"{0}\"".format(fhj))
#Exponent
def exponent(num1, num2):
    gik = num1**num2
    print("Your first number to the power of your second number is {0}.".format(gik))
#Smiley face
def imhappy():
    print("   |     |    ")
    print("   |     |    ")
    print("   |     |    ")
    print("   |     |    ")
    print("_            _")
    print(" _          _ ")
    print("  _        _  ")
    print("   _     _    ")
    print("    _   _     ")
    print("      _       ")
#Greeting
def hi():
    print('Hi! I hope you are having a really good day! If not, I hope this cheers you up.')
    imhappy()
#Clear terminal
def clear():
    import os
    os.system('clear')
#Ascii
def ascii(str, font='stantard', mode='print'):
    b = pyfiglet.Figlet(font=font)
    c = b.renderText(str)
    if mode == 'print':
      print(c)
    elif mode =='return':
      return c
#Function chooser
def pleep():
    print('[1]Length')
    print('[2]Text')
    print('[3]Question')
    print('[4]Imhappy')
    print('[5]Hi')
    print('[6]Math Pleep')
    print('[7]Clear The terminal')
    print('[8]Ascii')
    ree = int(input('Which one?: '))
    if ree == 1:
        length()
    if ree == 2:
        mee = input('What text?: ')
        text(mee)
    if ree == 3:
        AHH = input('What question?: ')
        question(AHH)
    if ree == 4:
        imhappy()
    if ree == 5:
        hi()
    if ree == 6:
        mathypleep()
    if ree == 7:
        clear()
    if ree == 8:
        hii = input('Text: ')
        ffont = input('Font?: ')
        ascii(hii, font=ffont)
#View functions
def view():
    print('These are not all the functions, but these include some of them.')
    print('1. Pleep(Type \"pleep()\")')
    print('2. Math Pleep(Type \"mathypleep()\")')

#Unicode, Hexadecimal, Octal, Binary
class funfuncs:
    """
    Fun functions.
    """
    def uni_ques(uni):
        print('Unicode: ' + chr(uni))
    def hex_ques(hexa):
        print('Hexadecimal: ' + hex(hexa).strip('0x'))
    def oct_ques(octa):
        print('Octal: ' + oct(octa).strip('0o'))
    def bin_ques(bina):
        print('Binary: ' + bin(bina).strip('0b'))
    def uni_rand(fromm, to):
        uni = r.randint(fromm, to)
        print('Random Unicode: ' + chr(uni))
    def hex_rand(fromm, to):
        hexa = r.randint(fromm, to)
        print('Random Hexadecimal: ' + hex(hexa).strip('0x'))
    def oct_rand(fromm, to):
        octa = r.randint(fromm, to)
        print('Random Octal: ' + oct(octa.strip('0o')))
    def bin_rand(fromm, to):
        bina = r.randint(fromm, to)
        print('Random Binary: ' + bin(bina).strip('0b'))
os.system('clear')
