## Python Tips & Tricks

**Tips and Tricks** based on [video](https://www.youtube.com/watch?v=C-gEQdGVXbk)

1. [Ternary Conditionals](#Ternary-Conditionals)

2. [Underscore Placeholders](#Underscore-Placeholders)

3. [Context Managers](#Context-Managers)

4. [Enumerate](#Enumerate)

5. [Zip](#Zip)

6. [Unpacking](#Unpacking)

7. [Setattr/Getattr](#Setattr/Getattr)

8. [GetPass](#GetPass)

9. [Python dash m](#Python-dash-m)

10. [Help/Dir](#Help/Dir)

#### Ternary Conditionals

- before:   
  
  ```python
  condition = True
  if condition:
      x = 1    
  else:
      x = 0
  print x
  ```

- after:
  
  ```python
  x = 1 if condition else 0
   print x
  ```

#### Underscore Placeholders

**This feature was added in Python 3.6. It is used for separating digits of numbers using underscore for readability.**

- before:
  
  ```python
  num1 = 1000000000
  num2 = 100000000
  total = num1 + num2
  print total
  ```

- after:
        
  
  ```python
   num1 = 10_000_000_000
   num2 = 100_000_000
  ```

#### Context Managers

- before:
  
  ```python
  f = open('D:\\repiter.txt', 'r')
  file_content = f.read()
  f.close()
  
  words = file_content.split(' ')
  word_count = len(words)
  
  print word_count
  ```

- after:
  
  ```python
  with open('D:\\repiter.txt', 'r') as f:
      file_content = f.read()
      words = file_content.split(' ')
      word_count = len(words)
      print word_count
  ```

#### Enumerate

- before:

```python
 names = ['Corey','Cris','Dave','Travis']
 for name in names:
     print name
```

or indexing:

```python
names = ['Corey','Cris','Dave','Travis']
index =0
for name in names:
    print index, name
    index += 1
```

- after:

```python
  names = ['Corey','Cris','Dave','Travis']
  for index, name in enumerate(names):
      print index, name
```

or if need start with 1:

```python
names = ['Corey','Cris','Dave','Travis']
for index, name in enumerate(names,start=1):
    print index, name
```

#### Zip

- before:

```python
 names = ['Peter Spark','Shkvark Cunt','Wood Weelsoon','Brace Wayn']
 heroes = ['speederman','uberman','dedploo','Buttman']

 for index, name in enumerate(names):
     hero = heroes[index]
     print "%s is actualy %s" % (name, hero)
```

- after:

```python
  names = ['Peter Spark','Shkvark Cunt','Wood Weelsoon','Brace Wayn']
  heroes = ['speederman','uberman','dedploo','Buttman']

  for name, hero in zip(names, heroes):
      print "%s is actualy %s" % (name, hero)
```

#### Unpacking

###### for python 3.4 (PEP448) see in video

- before:

```python
  a, _ = (1 ,2)

  print a
  #print b
```

- after:

```python
a, b, *c = (1, 2, 3, 4, 5)
print a
print b
print c
```

#### Setattr/Getattr

- before:
  
  ```python
  class Person():
      pass
  
  person = Person()
  
  person.first = "Kory"
  person.last = "Cookie"
  
  print person.first
  print person.last
  ```

- after:
  
  ```python
  class Person():
      pass
  
  person = Person()
  
  first_key = 'first'
  first_val = 'Corey'
  
  #person.first_key = first_val
  #setattr(person,'first','Corey')
  setattr(person,first_key,first_val)
  
  print person.first
  
  first = getattr(person,first_key)
  
  print first
  ```

- after2:
  
  ```python
  class Person():
      pass
  
  person = Person()
  
  person_info = {'first':'Cprey','last':'Cookey'}
  
  for key, value in person_info.items():
      setattr(person, key, value)
  
  print person.first
  print person.last
  
  for key in person_info.keys():
      print getattr(person,key)
  ```

#### GetPass

- before:
  
  ```python
  username = input('Username:')
  password = input('Password:')
  
  print('Logging in...')
  ```

- after:
  
  ```python
  from getpass import getpass
  
  username = input('Username:')
  password = getpass('Password:')
  
  print('Logging in...')
  ```

#### Python dash m

- before:
  
  ```batch
  python3 -m smtpd -c DebuggingServer -n localhost:25
  ```

- after:

#### Help/Dir

- before:
  
  ```python
  import smtpd
  from datetime import datetime
  help(smtpd)
  dir(datetime)
  ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get
  attribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__
  new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__'
  , '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'f
  old', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isof
  ormat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution',
  'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 't
  zinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
  
  datetime.today
  <built-in method today of type object at 0x000007FEBDB7B530>
  
  datetime.today()
  datetime.datetime(2020, 10, 15, 23, 25, 37, 101100)
  ```

```
- after:
```
