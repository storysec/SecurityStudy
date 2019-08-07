#coding=utf-8
# 根据 URL 生成特定目标网站备份文件猜测字典
#Test By： AnCoLin|影风
#http://www.storysec.com
suffixList = ['.rar','.zip','.sql','.gz','.tar','.bz2','.tar.gz','.bak','.dat']
keyList=['install','INSTALL','index','INDEX','ezweb','EZWEB','flashfxp','FLASHFXP']
# 请输入目标 URL
url =input("Please input the URL:")
if (url[:5] == 'http:'):
    url = url[7:].strip()
if (url[:6] == 'https:'):
    url = url[8:].strip()
numT = url.find('/')
if(numT != -1):
    url = url - url[:numT]

# 根据 URL，推测一些针对性的文件名:
num1 = url.find('.')
num2 = url.find('.',num1 + 1)

keyList.append(url[num1 + 1:num2])
keyList.append(url[num1 + 1:num2].upper())
keyList.append(url)  # www.test.com
keyList.append(url.upper())
keyList.append(url.replace('.','_'))  # www_test_com
keyList.append(url.replace('.','_').upper())
keyList.append(url.replace('.',''))  # wwwtestcom
keyList.append(url.replace('.','').upper())
keyList.append(url[num1 + 1:])   # test.com
keyList.append(url[num1 + 1:].upper())   
keyList.append(url[num1 + 1:].replace('.','_'))  # test_com
keyList.append(url[num1 + 1:].replace('.','_').upper())

# 生成字典列表，并写入 txt 文件:
tempList =[]
for key in keyList:
    for suff in suffixList:
        tempList.append(key + suff)
        fileName = url+'.'+'txt'
fobj = open(fileName,'w')

for each in tempList:
    each ='/' + each
    fobj.write('%s%s' %(each,'\n'))
    fobj.flush()

print("OK!")