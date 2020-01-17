import requests
import xmltodict
import json
import os




POST_URL = "https://pastebin.com/api/api_post.php"
LOGIN_URL = "https://pastebin.com/api/api_login.php"

class Pastebin(): #TODO modify

    def __init__(self, token, username, password):
        
        self.token = token
        #creating User ID
        data = {
            'api_dev_key' : self.token,
            'api_user_name' : username,
            'api_user_password' : password,
        }

        login = requests.post(LOGIN_URL, data)
        self.uid = login.text
    
    
    def paste(self,code,privateorno,title,expduration,txtformat):#ex:obj.paste("print("hello world")","1","Python Script","1M","python")
        self.code = code
        self.privateorno = privateorno
        self.title = title
        self.expduration = expduration
        self.format = txtformat
        self.data = {
            'api_dev_key' : self.token,
            'api_paste_code' : self.code,
            'api_paste_private': self.privateorno,#0=public 1=unlisted 2=private
            'api_paste_name': self.title,
            'api_paste_expire_date': self.expduration, #N = Never 10M = 10 Minutes 1H = 1 Hour 1D = 1 Day 1W = 1 Week 1M = 1 Month 1Y = 1 Year 
            'api_paste_format': self.format, #python php javascript cpp
            'api_user_key':self.uid,
            'api_option':'paste'
        }

        self.post = requests.post(POST_URL, self.data)
        return self.post.text
        
        
    def delete(self,pastekey): # Insert the paste link or the paste id 

        if "https" in pastekey:
            self.pastekey = pastekey.replace("https://pastebin.com/",'')
        else:
            self.pastekey = pastekey

        self.data = {
            'api_dev_key' : self.token,
            'api_user_key' : self.uid,
            'api_paste_key' : self.pastekey,
            'api_option' : 'delete'
        }

        self.post = requests.post(POST_URL, self.data)
        return self.post.text
        
        
    def list_pastes(self,resultlimit):
        self.resultlimit = resultlimit
        self.data = {
            'api_dev_key' : self.token,
            'api_user_key' : self.uid,
            'api_results_limit' : self.resultlimit, #min is 1, max is 100 and default is 50
            'api_option' : 'list'
        }

        self.post = requests.post(POST_URL, self.data)
        
        temp = open("temp.txt","w")
        temp.write("<root>\n")
        temp.write(self.post.text)
        temp.write("</root>")
        temp.close()

        temp = open("temp.txt","r")
        xmltext = ""
        c = 0
        for line in temp.readlines():
            line = line.replace("\n",'')
            
            if line == "<paste>":
                if c == 0:
                    pass
                else:    
                    line = "<paste"+str(c)+">"

            if line == "</paste>":
                if c == 0:
                    pass
                else:
                    line = "</paste"+str(c)+">"
                c+=1
            xmltext+=line+'\n'

        os.remove("temp.txt")
        print(xmltext)
        dictconv = xmltodict.parse(xmltext)
        response = json.dumps(dictconv)
        return response

