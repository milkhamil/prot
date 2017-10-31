# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="Emo29WvlUkXkKinu7IJc.t/tzrTvswcgHFrUhFx7BFa.2/DORZ5uWY5tGXH5aFQEJRZXLd8Gme3ONnQz4L/7Uro=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmnwGhWxOCF64hLJ4JJ5.r5ASasddV+NqkdGxLRGGHq.DpOCdf/vu2GNGImdBJVOeYVP4TTiSIsF3mRyX1S0lmY=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="Emk6OA7h6439Ea5Ge5t7.MD52GENmv7QC+jzY4LrPnW.Iz2FD1cO4gwXM1NFsnvKaTGWXRsy8WPCGHNPhg+KXXo=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Em3zqcvjHI3BWm7JRVE4.qg6VVUI/PoXpVH5p0VPXDa.t4B/c5fJKAfr2vpPv516fSp2pPex6/wb/Ad+JW7Hc8w=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EmzfaX9LtmN8zCRhSVn6.OikFWOAFZhj9k9i054J/TG.MYbMlMG5Yk1ygggWduk1aIP04oN1CVqMiSRv65NPuz0=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EmTw94G6h9h3l2kSjNnc.mTnlxsO+mIWobeSYdF8pha./q751+VU9UBeIOrbKX5duGmLgkUnq25qVOOPlAools8=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EmDAU3gr9fzCCY6PejY0.lWc6gZKLYV6I2qqnrAEL0a.64ve6dMTUH7H9OOk+QKtU2whQpAvB0trhpBuxzTgHSo=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="Emvgm5yll741MQ9uLgo6.qQpTK0NZa6/6xxY6Jy3Y5G.mvjHJzRD+JmdBXeydfD38q8+TF63C2kCKKnKx592otY=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EmnL1KUEMDoaBA1tFAI2.LVCH9BDnkebonnB9Me8YiG.tj5g+HsNwrEXDS5UZ5GIJPCrIoV9aPBmH9Hz0HY3sWU=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EmFzQHVLsuP06Lt3xTXa.9T0b8sAiYvExDCQYszxOMG.Budd0WE+wHIgQWDi1Luxh+k3bjOFzQy//qw/izKFgNw=")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="Emd4A46TRf9oymH0WkV5.5gQEr8ecm2aUhvbUE32cnq.hVWlX5uZz8buTWQZaDXPC21flCbgmKe8P9Olkin/5PA=")
ki10.loginResult()

ki11 = LINETCR.LINE()
ki11.login(token="EmCMX0Va5HULlX3s4WUe.7B33ygXp4+DxrWBAcC5dJG.2mbbiOZ+pkz9H7fDck1JlLmkkTtUoXlBt9S1ohNarnE=")
ki11.loginResult()

ki12 = LINETCR.LINE()
ki12.login(token="EmzPHjAXBAFNK1tRCvw3.McqffasvYlHg5wpCtZkC0W.1mZMekUBpWcC5QqD4kNrXXkhS7aZK3VPG3dY3Kwl5hk=")
ki12.loginResult()

ki13 = LINETCR.LINE()
ki13.login(token="Em8F8PENfnXxqS1Q5fQ7.Cg8LM/agUTZ6Itk4QicbLW.nkhek+YYHVLoT5GyvZyCyAtYK26IREs9MKlhFj+FMJA=")
ki13.loginResult()

ki14 = LINETCR.LINE()
ki14.login(token= "EmQVc0Sz4ZXMaIe8iGC7.gm3n8vuhUniChGhvuhmfjW.jTALa88EK96dP77kHbvvt/2zTGPpGyX8dBhQfij5LDI=")
ki14.loginResult()

ki15 = LINETCR.LINE()
ki15.login(token="EmwcJ1dRhfUUUuoP81ae.JSv04xZ8L8fucg7D2EAj+G.akhWQaAuD9SqIr5P2PiBwJJvF3AZqLRIsNEfSiy6P5A=")
ki15.loginResult()

ki16 = LINETCR.LINE()
ki16.login(token="Em4DVjsaWB5JTahLB0K8.z0XfRJ4l+IIzH/yTHM6eoa.EptBp3lTCywgpSLOqQpzKiPbgRCam4/vcTkMVrJDS0E=")
ki16.loginResult()

ki17 = LINETCR.LINE()
ki17.login(token="EmgEViAFQNduI7OSfI4e.FWNDI/3GwgQckZYEmSqmxG.3LdWqPOxmQ+MYbYeXepJrJFNW9HNZ34ZlSSNW3tOlAg=")
ki17.loginResult()

ki18 = LINETCR.LINE()
ki18.login(token="EmKXlquCOWYAbluNFJ14.aRoLVdSq4H6iNsx6nReTra.yy3T00sS6gd7BWpTeGlQsg4LUtXnOHYftX6t0sviWa0=")
ki18.loginResult()
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""         ӍіL ՏЄLҒ ѣѺҬՏ 
         -------------------------✁ 
✔ [Mid]
✔ [Me] 
✔ [TL  "Text"]
✔ [Cn "Name"]
✔ [Cbio]
✔ [Gift]
✔ [Getcontact "mid"]
✔ [Allgid]
✔ [Ban "Send contact"]
✔ [Unban "Send contact"]
✔ [Banlist]
✔ [Comment set "Text"]
✔ [Comment cek]
✔ [Message set "Text"]
✔ [Message cek] 
✔ [Set]

      Command In Group
      -------------------------------✁ 
✔ [Ourl]
✔ [Curl]
✔ [Gurl] 
✔ [Mid "@"]
✔ [Invite "Mid"] 
✔ [Kick "Mid"] 
✔ [Ginfo] 
✔ [Cancel]
✔ [Tagall] 
✔ [Burn]
✔ [Gname "Text"
✔ [Nk "@"]
✔ [Ban "@"]
✔ [Unban"@"]

         Auto Command
         -------------------------✁ 
✔ [Contact on/off] 
✔ [Join on/off] 
✔ [Leave on/off]
✔ [Add on/off] 
✔ [Comment on/off]
✔ [Protection on/off]
✔ [Linkprotect on/off]
✔ [Blockinvite on/off]
✔ [Procancel on/off]

   Kicker Only Command
   -----------------------------------✁
• [All in/out]
• [Absen]
• [Kcancel]
• [Kkick "@"]
• [All cn "Name"]
• [Cn1-18 "Name"]
• [All cb "Bio"]
• [Cb1-18 "Bio"]
• [Mid1-18]
• [All speed]
"""
helo=""
KAC=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
ki11mid = ki11.getProfile().mid
ki12mid = ki12.getProfile().mid
ki13mid = ki13.getProfile().mid
ki14mid = ki14.getProfile().mid
ki15mid = ki15.getProfile().mid
ki16mid = ki16.getProfile().mid
ki17mid = ki17.getProfile().mid
ki18mid = ki18.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid,ki12mid,ki13mid,ki14mid,ki15mid,ki16mid,ki17mid,ki18mid]
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
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
}


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
                                
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif msg.text.lower() == 'kicker only':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,kickerkey)
                else:
                    cl.sendText(msg.to,kickerkey)
            elif ("Gname " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gname ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Kkick " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "1kick " in msg.text:
                midd = msg.text.replace("1kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "2kick " in msg.text:
                midd = msg.text.replace("2kick ","")
                ki2.kickoutFromGroup(msg.to,[midd])
            elif "3kick " in msg.text:
                midd = msg.text.replace("4kick ","")
                ki3.kickoutFromGroup(msg.to,[midd])
            elif "4kick " in msg.text:
                midd = msg.text.replace("3kick ","")
                ki4.kickoutFromGroup(msg.to,[midd])
            elif "5kick " in msg.text:
                midd = msg.text.replace("5kick ","")
                ki5.kickoutFromGroup(msg.to,[midd])
            elif "6kick " in msg.text:
                midd = msg.text.replace("6kick ","")
                ki6.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif msg.text.lower() == 'mybot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki11mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki12mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki13mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki14mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki15mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki16mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki17mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki18mid}
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'kicker':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki11mid}
                ki11.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki12mid}
                ki12.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki13mid}
                ki13.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki14mid}
                ki14.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki15mid}
                ki15.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki16mid}
                ki16.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki17mid}
                ki17.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki18mid}
                ki18.sendMessage(msg)

            elif msg.text in ["Bcancel","Cancel dong","Kcancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        random.choice(klist).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No invites")
                        else:
                            ki.sendText(msg.to,"Invite people inside not")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Tidak ada undangan")
                    else:
                        ki.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text.lower() == 'ourl':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gurl = cl.reissueGroupTicket(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL:\nline://ti/g/" + gurl)
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text.lower() == 'curl':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
            elif msg.text in ["tagall","Tagall"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
            elif msg.text in ["/Out","/out"]:
				if msg.toType == 2:
					ginfo = cl.getGroup(msg.to)
					try:
						cl.leaveGroup(msg.to)
					except:
						pass
                    
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Procces...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text in ["Allspeed"]:
                start = time.time()
                ki.sendText(msg.to, "Procces...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki6.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki7.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki8.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki9.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki10.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki11.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki12.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki13.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki14.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki15.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki16.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki17.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki18.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nMembers:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "\n􀔃􀅗bawah􏿿Group Creator􀔃􀅗bawah􏿿")
                cl.sendMessage(msg)
            elif "Gid" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Mid1" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Mid2" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Mid3" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Mid4" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "Mid5" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "Mid6" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "Mid7" == msg.text:
                ki7.sendText(msg.to,ki7mid)
            elif "Mid8" == msg.text:
                ki8.sendText(msg.to,ki8mid)
            elif "Mid" == msg.text:
                ki9.sendText(msg.to,ki9mid)
            elif "Mid10" == msg.text:
                ki10.sendText(msg.to,ki10mid)
            elif "Mid11" == msg.text:
                ki11.sendText(msg.to,ki11mid)
            elif "Mid12" == msg.text:
                ki12.sendText(msg.to,ki12mid)
            elif "Mid13" == msg.text:
                ki13.sendText(msg.to,ki13mid)
            elif "Mid14" == msg.text:
                ki14.sendText(msg.to,ki14mid)
            elif "Mid15" == msg.text:
                ki15.sendText(msg.to,ki15mid)
            elif "Mid16" == msg.text:
                ki16.sendText(msg.to,ki16mid)
            elif "Mid17" == msg.text:
                ki17.sendText(msg.to,ki17mid)
            elif "Mid18" == msg.text:
                ki18.sendText(msg.to,ki18mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
                ki11.sendText(msg.to,ki11mid)
                ki12.sendText(msg.to,ki12mid)
                ki13.sendText(msg.to,ki13mid)
                ki14.sendText(msg.to,ki14mid)
                ki15.sendText(msg.to,ki15mid)
                ki16.sendText(msg.to,ki16mid)
                ki17.sendText(msg.to,ki17mid)
                ki18.sendText(msg.to,ki18mid)
            elif "Burn" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Burn","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"􀔃􀄝burn􏿿Yout group will be burned􀔃􀄝burn􏿿")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                cl.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"Group burned")
            elif msg.text in ["tagall","Tagall"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
            elif "TL " in msg.text:
                tl_text = msg.text.replace("TL ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All cb " in msg.text:
                string = msg.text.replace("All cb","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki11.getProfile()
                    profile.statusMessage = string
                    ki11.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki12.getProfile()
                    profile.statusMessage = string
                    ki12.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki13.getProfile()
                    profile.statusMessage = string
                    ki13.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki14.getProfile()
                    profile.statusMessage = string
                    ki14.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki15.getProfile()
                    profile.statusMessage = string
                    ki15.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki16.getProfile()
                    profile.statusMessage = string
                    ki16.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki17.getProfile()
                    profile.statusMessage = string
                    ki17.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki18.getProfile()
                    profile.statusMessage = string
                    ki18.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
#--------------------------------------------------
            elif "All cn" in msg.text:
                string = msg.text.replace("All cn","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki11.getProfile()
                    profile.displayName = string
                    ki11.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki12.getProfile()
                    profile.displayName = string
                    ki12.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki13.getProfile()
                    profile.displayName = string
                    ki13.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki14.getProfile()
                    profile.displayName = string
                    ki14.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki15.getProfile()
                    profile.displayName = string
                    ki15.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki16.getProfile()
                    profile.displayName = string
                    ki16.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki17.getProfile()
                    profile.displayName = string
                    ki17.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki18.getProfile()
                    profile.displayName = string
                    ki18.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names:\n👉 " + string + "👈")
            elif "All cbio " in msg.text:
                string = msg.text.replace("All cbio ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki11.getProfile()
                    profile.statusMessage = string
                    ki11.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki12.getProfile()
                    profile.statusMessage = string
                    ki12.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki13.getProfile()
                    profile.statusMessage = string
                    ki13.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki14.getProfile()
                    profile.statusMessage = string
                    ki14.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki15.getProfile()
                    profile.statusMessage = string
                    ki15.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki16.getProfile()
                    profile.statusMessage = string
                    ki16.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki17.getProfile()
                    profile.statusMessage = string
                    ki17.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki18.getProfile()
                    profile.statusMessage = string
                    ki18.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
#----------------------------------------------------------------------------
            elif "Cb1 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb2 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb3 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb4 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb5 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb6 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb7 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb8 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb9 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb10 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb11 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki11.getProfile()
                    profile.statusMessage = string
                    ki11.updateProfile(profile)
                    ki11.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb12 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki12.getProfile()
                    profile.statusMessage = string
                    ki12.updateProfile(profile)
                    ki12.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb13 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki13.getProfile()
                    profile.statusMessage = string
                    ki13.updateProfile(profile)
                    ki13.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb14 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki14.getProfile()
                    profile.statusMessage = string
                    ki14.updateProfile(profile)
                    ki14.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb15 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki15.getProfile()
                    profile.statusMessage = string
                    ki15.updateProfile(profile)
                    ki15.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb16 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki16.getProfile()
                    profile.statusMessage = string
                    ki16.updateProfile(profile)
                    ki16.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb17 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki17.getProfile()
                    profile.statusMessage = string
                    ki17.updateProfile(profile)
                    ki17.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Cb18 " in msg.text:
                if len(string.decode('utf-8')) <= 500:
                    profile = ki18.getProfile()
                    profile.statusMessage = string
                    ki18.updateProfile(profile)
                    ki18.sendText(msg.to,"Bio berubah menjadi " + string + "")

            elif "Cn  " in msg.text:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names:\n👉 " + string + "👈")
#---------------------------------------------------------
            elif "Cn1 " in msg.text:
                string = msg.text.replace("Cn1 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn2 " in msg.text:
                string = msg.text.replace("Cn2 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn3 " in msg.text:
                string = msg.text.replace("Cn3 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn4 " in msg.text:
                string = msg.text.replace("Cn4 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn5 " in msg.text:
                string = msg.text.replace("Cn5 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn6 " in msg.text:
                string = msg.text.replace("Cn6 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn7 " in msg.text:
                string = msg.text.replace("Cn7 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn8 " in msg.text:
                string = msg.text.replace("Cn8 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn9 " in msg.text:
                string = msg.text.replace("Cn9 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn10 " in msg.text:
                string = msg.text.replace("Cn10 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cn11 " in msg.text:
                string = msg.text.replace("Cn11 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki11.getProfile()
                    profile.displayName = string
                    ki11.updateProfile(profile)
                    ki11.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Cn12 " in msg.text:
                string = msg.text.replace("Cn12 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki12.getProfile()
                    profile.displayName = string
                    ki12.updateProfile(profile)
                    ki12.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Cn13 " in msg.text:
                string = msg.text.replace("Cn13 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki13.getProfile()
                    profile.displayName = string
                    ki13.updateProfile(profile)
                    ki13.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Cn14 " in msg.text:
                string = msg.text.replace("Cn14 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki14.getProfile()
                    profile.displayName = string
                    ki14.updateProfile(profile)
                    ki14.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Cn15 " in msg.text:
                string = msg.text.replace("Cn15 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki15.getProfile()
                    profile.displayName = string
                    ki15.updateProfile(profile)
                    ki15.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Cn16 " in msg.text:
                string = msg.text.replace("Cn16 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki16.getProfile()
                    profile.displayName = string
                    ki16.updateProfile(profile)
                    ki16.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Cn17 " in msg.text:
                string = msg.text.replace("Cn17 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki17.getProfile()
                    profile.displayName = string
                    ki17.updateProfile(profile)
                    ki17.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Cn18 " in msg.text:
                string = msg.text.replace("Cn18 ","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki18.getProfile()
                    profile.displayName = string
                    ki18.updateProfile(profile)
                    ki18.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Getcontact " in msg.text:
                mmid = msg.text.replace("Getcontact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to on")
                    else:
                        cl.sendText(msg.to,"contact already on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to on")
                    else:
                        cl.sendText(msg.to,"contact already on")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to off")
                    else:
                        cl.sendText(msg.to,"contact already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to off")
                    else:
                        cl.sendText(msg.to,"contact already off")
            elif msg.text.lower() == 'protection on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
            elif msg.text.lower() == 'linkprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to on")
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to on")
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
            elif msg.text.lower() == 'blockinvite on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to on")
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to on")
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
            elif msg.text.lower() == 'procancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
            elif msg.text.lower() == 'join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on")
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on")
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text.lower() == 'join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off")
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off")
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
            elif msg.text.lower() == 'protection off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
            elif msg.text.lower() == 'linkprotect off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
            elif msg.text.lower() == 'blockinvite off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
            elif msg.text.lower() == 'procancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
            elif "Gcancel " in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"alrady off")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text.lower() == 'leave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'leave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+="􀐂􀇰pin􏿿 Contact:on 􀜁􀄯􏿿\n"
                else: md+="􀐂􀇰pin􏿿 Contact:off􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀐂􀇰pin􏿿 Auto Comment:on 􀜁􀄯􏿿\n"
                else:md+="􀐂􀇰pin􏿿 Auto Comment:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀐂􀇰pin􏿿 Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􀐂􀇰pin􏿿 Auto Join:off􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀐂􀇰pin􏿿 Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􀐂􀇰pin􏿿 Auto leave:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀐂􀇰pin􏿿 Share:on 􀜁􀄯􏿿\n"
                else:md+="􀐂􀇰pin􏿿 Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀐂􀇰pin􏿿 Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􀐂􀇰pin􏿿 Auto add:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􀐂􀇰pin􏿿 Protection:on 􀜁􀄯􏿿\n"
                else:md+="􀐂􀇰pin􏿿 Protection:off 􀜁􀄰􏿿\n"
                if wait["linkprotect"] == True: md+="􀐂􀇰pin􏿿 Linkprotect:on 􀜁􀄯􏿿\n"
                else:md+="􀐂􀇰pin􏿿 Linkprotect:off 􀜁􀄰􏿿\n"
                if wait["inviteprotect"] == True: md+="􀐂􀇰pin􏿿 Blockinvite:on 􀜁􀄯􏿿\n"
                else:md+="􀐂􀇰pin􏿿 Blockinvite:off 􀜁􀄰􏿿\n"
                if wait["cancelprotect"] == True: md+="􀐂􀇰pin􏿿 Procancel:on 􀜁􀄯􏿿\n"
                else:md+="􀐂􀇰pin􏿿 Procancel:off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,"                  Settings\n                  -------------✁\n" + md)
                msg.contentType = 13
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿")
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text in ["tagall","Tagall"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
            elif msg.text in ["Out."]:
				if msg.toType == 2:
					ginfo = cl.getGroup(msg.to)
					try:
						cl.leaveGroup(msg.to)
					except:
						pass
            elif msg.text.lower() == 'allgid':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "-[%s]:\n%s\n\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text.lower() == 'add on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'add off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
            elif "Message set " in msg.text:
                wait["message"] = msg.text.replace("Message set ","")
                cl.sendText(msg.to,"We changed the message")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif "Random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = '1234567890abcdefghijklmnopqrstufwxyz!@#$%^&*()+_=-'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")	
            elif msg.text in ["Message cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif "Message set " in msg.text:
                c = msg.text.replace("Message set ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
#---------------------------------
            elif "Comment set " in msg.text:
                c = msg.text.replace("Comment set ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Autocomment telah diubah\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autocomment is already on")
                    else:
                        cl.sendText(msg.to,"Autocomment is on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autocomment is turn on")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€")
            elif msg.text in ["Comment off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto comment is already off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autocomment is turn off")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment cek"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl","gurl"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“👈")
            
            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€��ô€…���👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"👉Jam sudah off👈")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"👉Jam off👈")
            elif "Jam say " in msg.text:
                n = msg.text.replace("Jam say ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.sendText(msg.to,"Good bye bitch")
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------

            elif ("Kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("1kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")

            elif ("2kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("3kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Error")
            elif ("4kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki4.kickoutFromGroup(msg.to,[target])
                       except:
                           ki4.sendText(msg.to,"Error")
            elif ("5kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif ("6kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki6.sendText(msg.to,"Error")
            elif ("Mid " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"" +  key1)

            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Cleanse","")
                        gs = cl.getGroup(msg.to)
                        ki.sendText(msg.to,"Group cleansing begin")
                        ki.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group cleansed")
#-----------------------------------------------------------
	    elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target in banned")
                            except:
                                cl.sendText(msg.to,"Error")
	    elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target is unbanned")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")
#-----------------------------------------------------------
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

#-----------------------------------------------------------
            elif msg.text.lower() == 'absen':
                profile = ki.getProfile()
                text = "BotNumber: 1\nDsiplay name: " + profile.displayName
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = "BotNumber: 2\nDsiplay name: " + profile.displayName
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = "BotNumber: 3\nDsiplay name: " + profile.displayName
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = "BotNumber: 4\nDsiplay name: " + profile.displayName
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = "BotNumber: 5\nDsiplay name: " + profile.displayName
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = "BotNumber: 6\nDsiplay name: " + profile.displayName
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = "BotNumber: 7\nDsiplay name: " + profile.displayName
                ki7.sendText(msg.to, text)
                profile = ki8.getProfile()
                text = "BotNumber: 8\nDsiplay name: " + profile.displayName
                ki8.sendText(msg.to, text)
                profile = ki9.getProfile()
                text = "BotNumber: 9\nDsiplay name: " + profile.displayName
                ki9.sendText(msg.to, text)
                profile = ki10.getProfile()
                text = "BotNumber: 10\nDsiplay name: " + profile.displayName
                ki10.sendText(msg.to, text)
                profile = ki11.getProfile()
                text = "BotNumber: 11\nDsiplay name: " + profile.displayName
                ki11.sendText(msg.to, text)
                profile = ki12.getProfile()
                text = "BotNumber: 12\nDsiplay name: " + profile.displayName
                ki12.sendText(msg.to, text)
                profile = ki13.getProfile()
                text = "BotNumber: 13\nDsiplay name: " + profile.displayName
                ki13.sendText(msg.to, text)
                profile = ki14.getProfile()
                text = "BotNumber: 14\nDsiplay name: " + profile.displayName
                ki14.sendText(msg.to, text)
                profile = ki15.getProfile()
                text = "BotNumber: 15\nDsiplay name: " + profile.displayName
                ki15.sendText(msg.to, text)
                profile = ki16.getProfile()
                text = "BotNumber: 16\nDsiplay name: " + profile.displayName
                ki16.sendText(msg.to, text)
                profile = ki17.getProfile()
                text = "BotNumber: 17\nDsiplay name: " + profile.displayName
                ki17.sendText(msg.to, text)
                profile = ki18.getProfile()
                text = "BotNumber: 18\nDsiplay name: " + profile.displayName
                ki18.sendText(msg.to, text)

#-----------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'banlist':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"The banlist is empty")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += ">" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"________Banlist________\n" + mc)
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"No blacklist found")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass

#-----------------------------------------------
            elif msg.text.lower() == 'all in':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
#-----------------------------------------------
            elif msg.text.lower() == 'backup':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text.lower() == 'sayang':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                        
            elif "K1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "K2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "K3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "K4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "K5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "K6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "K7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif "K8 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif "K9 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif "K10 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
#-----------------------------------------------
            elif "K11 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki11.updateGroup(G)
#-----------------------------------------------
            elif "K12 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki12.updateGroup(G)
#-----------------------------------------------
            elif "K13 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki13.updateGroup(G)
#-----------------------------------------------
            elif "K14 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki14.updateGroup(G)
#-----------------------------------------------
            elif "K15 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki15.updateGroup(G)
#-----------------------------------------------
            elif "K16 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki16.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki16.updateGroup(G)
            elif "K17 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki17.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki17.updateGroup(G)
            elif "K18 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki18.updateGroup(G)
#-----------------------------------------------
            elif msg.text.lower() == 'all out':
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = ki10.getGroupIdsJoined()
                gid = ki11.getGroupIdsJoined()
                gid = ki12.getGroupIdsJoined()
                gid = ki13.getGroupIdsJoined()
                gid = ki14.getGroupIdsJoined()
                gid = ki15.getGroupIdsJoined()
                gid = ki16.getGroupIdsJoined()
                gid = ki17.getGroupIdsJoined()
                gid = ki18.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)
                    ki9.leaveGroup(i)
                    ki10.leaveGroup(i)
                    ki11.leaveGroup(i)
                    ki12.leaveGroup(i)
                    ki13.leaveGroup(i)
                    ki14.leaveGroup(i)
                    ki15.leaveGroup(i)
                    ki16.leaveGroup(i)
                    ki17.leaveGroup(i)
                    ki18.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Good bye my friend")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
#-----------------------------------------------
            elif "K1 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K2 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K3 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K4 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K5 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------------
            elif "K6 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K7 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K8 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K9 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K10 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K11 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki11.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K12 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki12.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K13 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki13.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K14 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki14.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K15 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki15.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K16 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki16.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K17 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki17.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "K18 out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki18.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))

#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)

                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)

                elif op.param3 in ki10mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in ki11mid:
                    if op.param2 in ki10mid:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)

                        
                        ki10.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)

                elif op.param3 in ki12mid:
                    if op.param2 in ki11mid:
                        G = ki11.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)
                    else:
                        G = ki11.getGroup(op.param1)

                        
                        ki11.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)

                elif op.param3 in ki13mid:
                    if op.param2 in ki12mid:
                        G = ki12.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)
                    else:
                        G = ki12.getGroup(op.param1)

                        
                        ki12.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)

                elif op.param3 in ki14mid:
                    if op.param2 in ki13mid:
                        G = ki13.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)
                    else:
                        G = ki13.getGroup(op.param1)

                        
                        ki13.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)

                elif op.param3 in ki15mid:
                    if op.param2 in ki14mid:
                        G = ki14.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)
                    else:
                        G = ki14.getGroup(op.param1)

                        
                        ki14.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)

                elif op.param3 in ki16mid:
                    if op.param2 in ki15mid:
                        G = ki15.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki15.updateGroup(G)
                        Ticket = ki15.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)
                    else:
                        G = ki15.getGroup(op.param1)

                        
                        ki15.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki15.updateGroup(G)
                        Ticket = ki15.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ks.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    ki.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    ki.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    ki.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
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
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,50):
        hasil = cl.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by : Khamil\nhttp://instagram.com/milkhamil")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
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
