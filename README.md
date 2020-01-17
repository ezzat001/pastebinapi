# UnOfficial API for Pastebin.com
[![MIT license](https://img.shields.io/apm/l/vim-mode)](https://github.com/ezzat001/pastebinapi/blob/master/LICENSE)
[![built with Python3](https://img.shields.io/pypi/pyversions/requests)](https://www.python.org/)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://github.com/ezzat001/pastebinapi)
[![Downloads](https://img.shields.io/pypi/dm/pastebin)]()

## **Installation**
It is recomended to install using Git

We will be developing this Project

```bash
git clone https://github.com/ezzat001/pastebinapi
```

<br />

# Documentation

### Table of Contents

- **[Initiate](#initiate)**
- [Paste](#paste)
- [List Pastes](#listpastes)
- [Delete Pastes](#deletepastes)


<br />


### initiate

```python3
import pastebin

token = "XXXXXXXXXXXXXX" # your Dev Token Generated from pastebin.com/api
username = "ahmedezzatpy" # Your Username
password = "xxxxxxxxx" # Your Password

api = pastebin.Pastebin(token, username, password)
```

### paste

```python3
api = pastebin.Pastebin(token, username, password)

text = """Hello Ahmed Ezzat,
i am very glad to write this paste for you"""

privateorno = 0 # 0 = public , 1 = unlisting , 2 = private 
title = "Ahmed Ezzat's Paste"
expduration = "N" # N = Never Expires 10M = 10 Minutes 1H = 1 Hour 1D = 1 Day1 W = 1 Week 1M = 1 Month 1Y = 1 Year 
txtformat = "python" # can be python ,javascript , php or java

api.paste(text,privateorno,title,expduration,txtformat)
```
to get the paste link do the following

```python3 
paste = api.paste(text,privateorno,title,expduration,txtformat)

print(paste) 
```
```bash
https://pastebin.com/H32BxI
```
### listpastes
```python3
  pastes = paste.list_pastes(20) # Lists 20 Pastes .. Minimum 0 and Maximum 100 
  print(pastes)
```


### deletepastes
```python3
api.delete("https://pastebin.com/4HunZo9")
#or
api.delete("4HunZo9")
```
if you want check the response 

```python3
r = api.delete("https://pastebin.com/4HunZo9")
print(r)```

```bash
Paste Removed
```
