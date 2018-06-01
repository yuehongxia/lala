# -*- coding: utf-8 -*-
__author__ = 'River'
import cv2,os,shutil,datetime,re,time
from threading import Thread
from hashlib import md5

# im = cv2.imread("1.jpg")  #读取图片
# im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# cv2.imwrite("test/1/1.jpg", im_gray)
PICHASH= {}


def md5_file(name):
    try:
        m = md5()
        a_file = open(name, 'rb')
        m.update(a_file.read())
        a_file.close()
        return m.hexdigest()
    except:
        return None


def nowater(dir,newdir,dirlist):
    global PICHASH
    for ppicdir in dirlist:
        if(os.path.isdir(dir+ppicdir)):
            sortfiles=os.listdir(dir+ppicdir)
            if '.DS_Store' in sortfiles:
                sortfiles.remove('.DS_Store')
            sortfiles.sort()
            for oldfile in sortfiles:
                filetype="."+oldfile.split(".")[len(oldfile.split("."))-1]
                picname_front=oldfile.split(filetype)[0]
                oldfile=dir+ppicdir+"/"+oldfile
                jpgname=picname_front+".jpg"
                jpgname=newdir+ppicdir+"/"+jpgname
                try:
                    oldfile_hash=md5_file(oldfile)
                    oldfile_tmphashvalue=PICHASH.get(oldfile_hash)
                    file_object = open('pichash.txt', 'a')
                    file_object.write(oldfile+":"+oldfile_hash+'\n')
                    file_object.close()
                    if(oldfile_tmphashvalue==None):#新文件,已经处理过的图片，就不会再次处理了
                        if not os.path.exists(newdir+ppicdir):
                            os.makedirs(newdir+ppicdir)
                        #print oldfile  哈哈
                        #print jpgname
                        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+","+oldfile+",img\n")
                        img=cv2.imread(oldfile)
                        x,y,z=img.shape
                        if x < 10:#太小文件不处理
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+","+jpgname+"文件太小，跳过")
                        elif x >8000:#太大的;文件不处理
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+","+jpgname+"文件太大，跳过")


                        elif not os.path.exists(jpgname):#这就是最关键的代码了
                            for i in range(x):
                                for j in range(y):
                                    varP=img[i,j]
                                    if sum(varP)>350 and sum(varP)<765:#大于250，小于765（sum比白色的小）
                                        img[i,j]=[255,255,255]
                            #cv2.imwrite(jpgname,img,[int(cv2.IMWRITE_JPEG_QUALITY),70])#linux跑悲剧了
                            cv2.imwrite(jpgname,img)
                            print ("jpgname:"+jpgname)
                            PICHASH[oldfile_hash]=oldfile
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+","+oldfile+",done\n")
                        else:
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+","+jpgname+"文件已存在，跳过\n")
                    elif(oldfile_tmphashvalue!=None):
                        if(os.path.exists(jpgname)):
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+","+jpgname+"文件已存在，跳过\n")
                        else:
                            shutil.copyfile(oldfile_tmphashvalue,oldfile)
                            shutil.copyfile(oldfile,jpgname)
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+","+jpgname+"和老文件一样，拷贝旧文件，跳过")
                except Exception as e:
                    print ("Exception:",e)
                    continue


if __name__=='__main__':
    dir="old/"
    newdir="new/"
    list0=[]
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for ppicdir in os.listdir(dir) :#生成多个list，主要是为了并发处理多个目录的图片
        if(os.path.isdir(dir+ppicdir)):
            if (re.compile(r'^[0-1].*').match(str(ppicdir))):
                list0.append(ppicdir)
            elif(re.compile(r'^[2-3].*').match(str(ppicdir))):
                list1.append(ppicdir)
            elif(re.compile(r'^[4-5].*').match(str(ppicdir))):
                list2.append(ppicdir)
            elif(re.compile(r'^[6-7].*').match(str(ppicdir))):
                list3.append(ppicdir)
            elif(re.compile(r'^[8-9].*').match(str(ppicdir))):
                list4.append(ppicdir)
            else:
                continue
    #启n线程并行处理
    Thread(target=nowater,args=(dir,newdir,list0)).start()#这里只有
    Thread(target=nowater,args=(dir,newdir,list1,)).start()
    Thread(target=nowater,args=(dir,newdir,list2,)).start()
    Thread(target=nowater,args=(dir,newdir,list3,)).start()
    Thread(target=nowater,args=(dir,newdir,list4,)).start()