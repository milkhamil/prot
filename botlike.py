# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re
cl = LINETCR.LINE()
cl.login(token="EmwLgKqDySkJORBv48N5.r5ASasddV+NqkdGxLRGGHq.mgHVJ2lh2AZhJfp8MCzfozvgdAOSa2wqhM8DwIdd8U4=")
cl.loginResult()
reload(sys)
sys.setdefaultencoding('utf-8')

helo=""

admsa = "u4fe4d946d5525821a17d1b877d7edb7c"

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':False,
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me 􀜁􀆚pray􏿿You can drop a message if you need a some thing",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"SelfBotON",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":True,
    "inviteprotect":True,
    "linkprotect":True,
}

autoKomentar =""".                   􀔃􀇣blue􏿿Autolike by: றіԼ􀔃􀇣blue􏿿
         􀐂􀇰pin􏿿Open pemasangan selfbot􀐂􀇰pin􏿿
         Minat or tanya tanya apa aja fitur &
         keuntungan pake selfbot? Pm aja
          http://line.me/ti/p/aS9kQvOukB
          http://line.me/ti/p/aS9kQvOukB
"""

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u1b3ce3c7bfbbc5f4b5f2f6ded16ba3a5":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already banned")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already banned")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Target in banned")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = cl.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "cl Like"
          except:
            pass
        else:
            print "cl Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki Like"
          except:
            pass
        else:
            print "ki Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki2.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki2 Like"
          except:
            pass
        else:
            print "ki2 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki3.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki3 Like"
          except:
            pass
        else:
            print "ki3 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki4.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki4 Like"
          except:
            pass
        else:
            print "ki4 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki5.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki5 Like"
          except:
            pass
        else:
            print "ki5 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki6.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki6 Like"
          except:
            pass
        else:
            print "ki6 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki7.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki7.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki7.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki7 Like"
          except:
            pass
        else:
            print "ki7 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki8.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki8.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki8.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki8 Like"
          except:
            pass
        else:
            print "ki8 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki9.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki9.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki9.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki9 Like"
          except:
            pass
        else:
            print "ki9 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#########################################################################################################################3
def autolike():
     for zx in range(0,50):
        hasil = ki10.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            ki10.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki10.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],autoKomentar)
            print "ki10 Like"
          except:
            pass
        else:
            print "ki10 Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
