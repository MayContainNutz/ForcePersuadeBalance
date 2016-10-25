#!/usr/bin/python

from Tkinter import *
import tkMessageBox

#master window
master = Tk()

#success = 1-(sum(maxdie - bonus(attacker-def))/maxdie^2
def calcSuccess(attacker,defender):
    attackerStat = int(attacker)
    defenderStat = int(defender)
    
    if (attackerStat-defenderStat>=0):
        sumOfBonus = 0
        for x in range(0,(100-(attackerStat-defenderStat))):
            sumOfBonus += x
        return ((sumOfBonus/float(10000)))*100 
    else:
        sumOfBonus = 0
        for x in range(0, 98 + (attackerStat-defenderStat)):
            sumOfBonus += x
        return (sumOfBonus/float(10000))*100




#Persuasion(offence)
Label(master, text="Persuasion bonus by rank").grid(row=0, columnspan =2)
Label(master, text="Acolyte").grid(row=1, sticky=W)
Label(master, text="Aspirant").grid(row=2, sticky=W)
Label(master, text="Sith").grid(row=3, sticky=W)
Label(master, text="Lord").grid(row=4, sticky=W)
Label(master, text="Darth").grid(row=5, sticky=W)
#watchers, watch for changes in the text box
PersuAcolyteWatcher = StringVar()
PersuAspirWatcher = StringVar()
PersuSithWatcher = StringVar()
PersuLordWatcher = StringVar()
PersuDarthWatcher = StringVar()
#creating the text boxes
PersuAcolyte =Entry(master,textvariable=PersuAcolyteWatcher)
PersuAspir =Entry(master,textvariable=PersuAspirWatcher)
PersuSith =Entry(master,textvariable=PersuSithWatcher)
PersuLord =Entry(master,textvariable=PersuLordWatcher)
PersuDarth =Entry(master,textvariable=PersuDarthWatcher)
#position the text box
PersuAcolyte.grid(row=1,column=1)
PersuAspir.grid(row=2,column=1)
PersuSith.grid(row=3,column=1) 
PersuLord.grid(row=4,column=1)
PersuDarth.grid(row=5,column=1)

#Natural defense
Label(master, text="Persuade defence by rank").grid(row=0,column=2,columnspan =2)
Label(master, text="Acolyte").grid(row=1,column=2, sticky=E)
Label(master, text="Aspirant").grid(row=2,column=2, sticky=E)
Label(master, text="Sith").grid(row=3,column=2, sticky=E)
Label(master, text="Lord").grid(row=4,column=2, sticky=E)
Label(master, text="Darth").grid(row=5,column=2, sticky=E)

DefAcolyteWatcher = StringVar()
DefAspirWatcher = StringVar()
DefSithWatcher = StringVar()
DefLordWatcher = StringVar()
DefDarthWatcher = StringVar()

DefAcolyte = Entry(master,textvariable=DefAcolyteWatcher)
DefAspir = Entry(master,textvariable=DefAspirWatcher)
DefSith = Entry(master,textvariable=DefSithWatcher)
DefLord = Entry(master,textvariable=DefLordWatcher)
DefDarth = Entry(master,textvariable=DefDarthWatcher)

DefAcolyte.grid(row=1,column=3)
DefAspir.grid(row=2,column=3)
DefSith.grid(row=3,column=3)
DefLord.grid(row=4,column=3)
DefDarth.grid(row=5,column=3)

#Skill Defense(Thought Shield and Echani_
Label(master, text="Thought Shield and Echani").grid(row=0,column=4,columnspan =2)
Label(master, text="Acolyte").grid(row=1,column=4, sticky=E)
Label(master, text="Aspirant").grid(row=2,column=4, sticky=E)
Label(master, text="Sith").grid(row=3,column=4, sticky=E)
Label(master, text="Lord").grid(row=4,column=4, sticky=E)
Label(master, text="Darth").grid(row=5,column=4, sticky=E)

TsAcolyteWatcher = StringVar()
TsAspirWatcher = StringVar()
TsSithWatcher = StringVar()
TsLordWatcher = StringVar()
TsDarthWatcher = StringVar()

TsAcolyte = Entry(master,textvariable=TsAcolyteWatcher)
TsAspir = Entry(master,textvariable=TsAspirWatcher)
TsSith = Entry(master,textvariable=TsSithWatcher)
TsLord = Entry(master,textvariable=TsLordWatcher)
TsDarth = Entry(master,textvariable=TsDarthWatcher)

TsAcolyte.grid(row=1,column=5)
TsAspir.grid(row=2,column=5)
TsSith.grid(row=3,column=5)
TsLord.grid(row=4,column=5)
TsDarth.grid(row=5,column=5)

#Dominate Mind
Label(master, text="Dominate Mind").grid(row=0,column=6,columnspan =2)
Label(master, text="Acolyte").grid(row=1,column=6, sticky=E)
Label(master, text="Aspirant").grid(row=2,column=6, sticky=E)
Label(master, text="Sith").grid(row=3,column=6, sticky=E)
Label(master, text="Lord").grid(row=4,column=6, sticky=E)
Label(master, text="Darth").grid(row=5,column=6, sticky=E)

DomAcolyteWatcher = StringVar()
DomAspirWatcher = StringVar()
DomSithWatcher = StringVar()
DomLordWatcher = StringVar()
DomDarthWatcher = StringVar()

DomAcolyte = Entry(master,textvariable=DomAcolyteWatcher)
DomAspir = Entry(master,textvariable=DomAspirWatcher)
DomSith = Entry(master,textvariable=DomSithWatcher)
DomLord = Entry(master,textvariable=DomLordWatcher)
DomDarth = Entry(master,textvariable=DomDarthWatcher)

DomAcolyte.grid(row=1,column=7)
DomAspir.grid(row=2,column=7)
DomSith.grid(row=3,column=7)
DomLord.grid(row=4,column=7)
DomDarth.grid(row=5,column=7)

#inputs above, tables outputs below

#Persuasion stat block
#attacker
Label(master, text="Persuasion with no defence").grid(row=7,column=1,columnspan =2)
Label(master, text="Acolyte").grid(row=8,column=0, sticky=W)
Label(master, text="Aspirant").grid(row=9,column=0, sticky=W)
Label(master, text="Sith").grid(row=10,column=0, sticky=W)
Label(master, text="Lord").grid(row=11,column=0, sticky=W)
Label(master, text="Darth").grid(row=12,column=0, sticky=W)
#defenders
Label(master, text="Acolyte").grid(row=13,column=1, sticky=W)
Label(master, text="Aspirant").grid(row=13,column=2, sticky=W)
Label(master, text="Sith").grid(row=13,column=3, sticky=W)
Label(master, text="Lord").grid(row=13,column=4, sticky=W)
Label(master, text="Darth").grid(row=13,column=5, sticky=W)
#statblock1 base persuasion, no defense skill
#acolyte down
AcvAc = Entry(master)
AsvAc = Entry(master)
SvAc = Entry(master)
LvAc = Entry(master)
DvAc = Entry(master)
#Aspirant down
AcvAs = Entry(master)
AsvAs = Entry(master)
SvAs = Entry(master)
LvAs = Entry(master)
DvAs = Entry(master)
#Sith down
AcvS = Entry(master)
AsvS = Entry(master)
SvS = Entry(master)
LvS = Entry(master)
DvS = Entry(master)
#Lord down
AcvL = Entry(master)
AsvL = Entry(master)
SvL = Entry(master)
LvL = Entry(master)
DvL = Entry(master)
#Darth down
AcvD = Entry(master)
AsvD = Entry(master)
SvD = Entry(master)
LvD = Entry(master)
DvD = Entry(master)

#acolyte down
AcvAc.grid(row=8,column=1)
AsvAc.grid(row=9,column=1)
SvAc.grid(row=10,column=1)
LvAc.grid(row=11,column=1)
DvAc.grid(row=12,column=1)
#Aspirant down
AcvAs.grid(row=8,column=2)
AsvAs.grid(row=9,column=2)
SvAs.grid(row=10,column=2)
LvAs.grid(row=11,column=2)
DvAs.grid(row=12,column=2)
#Sith down
AcvS.grid(row=8,column=3)
AsvS.grid(row=9,column=3)
SvS.grid(row=10,column=3)
LvS.grid(row=11,column=3)
DvS.grid(row=12,column=3)
#Lord down
AcvL.grid(row=8,column=4)
AsvL.grid(row=9,column=4)
SvL.grid(row=10,column=4)
LvL.grid(row=11,column=4)
DvL.grid(row=12,column=4)
#Darth down
AcvD.grid(row=8,column=5)
AsvD.grid(row=9,column=5)
SvD.grid(row=10,column=5)
LvD.grid(row=11,column=5)
DvD.grid(row=12,column=5)


#Persuasion /w 1 def skill stat block
#attacker
Label(master, text="Persuasion with either Thought Shield or Echani").grid(row=15,column=1,columnspan =2)
Label(master, text="Acolyte").grid(row=16,column=0, sticky=W)
Label(master, text="Aspirant").grid(row=17,column=0, sticky=W)
Label(master, text="Sith").grid(row=18,column=0, sticky=W)
Label(master, text="Lord").grid(row=19,column=0, sticky=W)
Label(master, text="Darth").grid(row=20,column=0, sticky=W)
#defenders
Label(master, text="Acolyte").grid(row=21,column=1, sticky=W)
Label(master, text="Aspirant").grid(row=21,column=2, sticky=W)
Label(master, text="Sith").grid(row=21,column=3, sticky=W)
Label(master, text="Lord").grid(row=21,column=4, sticky=W)
Label(master, text="Darth").grid(row=21,column=5, sticky=W)
#statblock2 base persuasion, 1 defense skill
#acolyte down
AcvAc1D = Entry(master)
AsvAc1D = Entry(master)
SvAc1D = Entry(master)
LvAc1D = Entry(master)
DvAc1D = Entry(master)
#Aspirant down
AcvAs1D = Entry(master)
AsvAs1D = Entry(master)
SvAs1D = Entry(master)
LvAs1D = Entry(master)
DvAs1D = Entry(master)
#Sith down
AcvS1D = Entry(master)
AsvS1D = Entry(master)
SvS1D = Entry(master)
LvS1D = Entry(master)
DvS1D = Entry(master)
#Lord down
AcvL1D = Entry(master)
AsvL1D = Entry(master)
SvL1D = Entry(master)
LvL1D = Entry(master)
DvL1D = Entry(master)
#Darth down
AcvD1D = Entry(master)
AsvD1D = Entry(master)
SvD1D = Entry(master)
LvD1D = Entry(master)
DvD1D = Entry(master)

#acolyte down
AcvAc1D.grid(row=16,column=1)
AsvAc1D.grid(row=17,column=1)
SvAc1D.grid(row=18,column=1)
LvAc1D.grid(row=19,column=1)
DvAc1D.grid(row=20,column=1)
#Aspirant down
AcvAs1D.grid(row=16,column=2)
AsvAs1D.grid(row=17,column=2)
SvAs1D.grid(row=18,column=2)
LvAs1D.grid(row=19,column=2)
DvAs1D.grid(row=20,column=2)
#Sith down
AcvS1D.grid(row=16,column=3)
AsvS1D.grid(row=17,column=3)
SvS1D.grid(row=18,column=3)
LvS1D.grid(row=19,column=3)
DvS1D.grid(row=20,column=3)
#Lord down
AcvL1D.grid(row=16,column=4)
AsvL1D.grid(row=17,column=4)
SvL1D.grid(row=18,column=4)
LvL1D.grid(row=19,column=4)
DvL1D.grid(row=20,column=4)
#Darth down
AcvD1D.grid(row=16,column=5)
AsvD1D.grid(row=17,column=5)
SvD1D.grid(row=18,column=5)
LvD1D.grid(row=19,column=5)
DvD1D.grid(row=20,column=5)


#Dominate Mindstat block
#attacker
Label(master, text="Dominate Mind with no defence").grid(row=22,column=1,columnspan =2)
Label(master, text="Acolyte").grid(row=23,column=0, sticky=W)
Label(master, text="Aspirant").grid(row=24,column=0, sticky=W)
Label(master, text="Sith").grid(row=25,column=0, sticky=W)
Label(master, text="Lord").grid(row=26,column=0, sticky=W)
Label(master, text="Darth").grid(row=27,column=0, sticky=W)
#defenders
Label(master, text="Acolyte").grid(row=28,column=1, sticky=W)
Label(master, text="Aspirant").grid(row=28,column=2, sticky=W)
Label(master, text="Sith").grid(row=28,column=3, sticky=W)
Label(master, text="Lord").grid(row=28,column=4, sticky=W)
Label(master, text="Darth").grid(row=28,column=5, sticky=W)
#statblock1 base persuasion, no defense skill
#acolyte down
AcvAcDm = Entry(master)
AsvAcDm = Entry(master)
SvAcDm = Entry(master)
LvAcDm = Entry(master)
DvAcDm = Entry(master)
#Aspirant down
AcvAsDm = Entry(master)
AsvAsDm = Entry(master)
SvAsDm = Entry(master)
LvAsDm = Entry(master)
DvAsDm = Entry(master)
#Sith down
AcvSDm = Entry(master)
AsvSDm = Entry(master)
SvSDm = Entry(master)
LvSDm = Entry(master)
DvSDm = Entry(master)
#Lord down
AcvLDm = Entry(master)
AsvLDm = Entry(master)
SvLDm = Entry(master)
LvLDm = Entry(master)
DvLDm = Entry(master)
#Darth down
AcvDDm = Entry(master)
AsvDDm = Entry(master)
SvDDm = Entry(master)
LvDDm = Entry(master)
DvDDm = Entry(master)

#acolyte down
AcvAcDm.grid(row=23,column=1)
AsvAcDm.grid(row=24,column=1)
SvAcDm.grid(row=25,column=1)
LvAcDm.grid(row=26,column=1)
DvAcDm.grid(row=27,column=1)
#Aspirant down
AcvAsDm.grid(row=23,column=2)
AsvAsDm.grid(row=24,column=2)
SvAsDm.grid(row=25,column=2)
LvAsDm.grid(row=26,column=2)
DvAsDm.grid(row=27,column=2)
#Sith down
AcvSDm.grid(row=23,column=3)
AsvSDm.grid(row=24,column=3)
SvSDm.grid(row=25,column=3)
LvSDm.grid(row=26,column=3)
DvSDm.grid(row=27,column=3)
#Lord down
AcvLDm.grid(row=23,column=4)
AsvLDm.grid(row=24,column=4)
SvLDm.grid(row=25,column=4)
LvLDm.grid(row=26,column=4)
DvLDm.grid(row=27,column=4)
#Darth down
AcvDDm.grid(row=23,column=5)
AsvDDm.grid(row=24,column=5)
SvDDm.grid(row=25,column=5)
LvDDm.grid(row=26,column=5)
DvDDm.grid(row=27,column=5)


def updateStatGrids(a,b,c):
    #collect all the values
        
    PersuAcolyteVal = 0
    PersuAspirVal = 0
    PersuSithVal = 0
    PersuLordVal = 0
    PersuDarthVal = 0
    DefAcolyteVal = 0
    DefAspirVal = 0
    DefSithVal = 0
    DefLordVal =0
    DefDarthVal = 0
    TsAcolyteVal = 0
    TsAspirVal = 0
    TsSithVal = 0
    TsLordVal = 0
    TsDarthVal = 0
    DomAcolyteVal = 0
    DomAspirVal = 0
    DomSithVal = 0
    DomLordVal = 0
    DomDarthVal = 0
    
    PersuAcolyteVal = int(PersuAcolyte.get())
    PersuAspirVal = int(PersuAspir.get())
    PersuSithVal = int(PersuSith.get())
    PersuLordVal = int(PersuLord.get())
    PersuDarthVal = int(PersuDarth.get())
    DefAcolyteVal = int(DefAcolyte.get())
    DefAspirVal = int(DefAspir.get())
    DefSithVal = int(DefSith.get())
    DefLordVal = int(DefLord.get())
    DefDarthVal = int(DefDarth.get())
    TsAcolyteVal = int(TsAcolyte.get())
    TsAspirVal = int(TsAspir.get())
    TsSithVal = int(TsSith.get())
    TsLordVal = int(TsLord.get())
    TsDarthVal = int(TsDarth.get())
    DomAcolyteVal = int(DomAcolyte.get())
    DomAspirVal = int(DomAspir.get())
    DomSithVal = int(DomSith.get())
    DomLordVal = int(DomLord.get())
    DomDarthVal = int(DomDarth.get())

    #delete to clear each field
    AcvAc.delete(0,END)
    AsvAc.delete(0,END)
    SvAc.delete(0,END)
    LvAc.delete(0,END)
    DvAc.delete(0,END)
    #Aspirant down
    AcvAs.delete(0,END)
    AsvAs.delete(0,END)
    SvAs.delete(0,END)
    LvAs.delete(0,END)
    DvAs.delete(0,END)
    #Sith down
    AcvS.delete(0,END)
    AsvS.delete(0,END)
    SvS.delete(0,END)
    LvS.delete(0,END)
    DvS.delete(0,END)
    #Lord down
    AcvL.delete(0,END)
    AsvL.delete(0,END)
    SvL.delete(0,END)
    LvL.delete(0,END)
    DvL.delete(0,END)
    #Darth down
    AcvD.delete(0,END)
    AsvD.delete(0,END)
    SvD.delete(0,END)
    LvD.delete(0,END)
    DvD.delete(0,END)
    #acolyte down
    AcvAc1D.delete(0,END)
    AsvAc1D.delete(0,END)
    SvAc1D.delete(0,END)
    LvAc1D.delete(0,END)
    DvAc1D.delete(0,END)
    #Aspirant down
    AcvAs1D.delete(0,END)
    AsvAs1D.delete(0,END)
    SvAs1D.delete(0,END)
    LvAs1D.delete(0,END)
    DvAs1D.delete(0,END)
    #Sith down
    AcvS1D.delete(0,END)
    AsvS1D.delete(0,END)
    SvS1D.delete(0,END)
    LvS1D.delete(0,END)
    DvS1D.delete(0,END)
    #Lord down
    AcvL1D.delete(0,END)
    AsvL1D.delete(0,END)
    SvL1D.delete(0,END)
    LvL1D.delete(0,END)
    DvL1D.delete(0,END)
    #Darth down
    AcvD1D.delete(0,END)
    AsvD1D.delete(0,END)
    SvD1D.delete(0,END)
    LvD1D.delete(0,END)
    DvD1D.delete(0,END)
    #acolyte down
    AcvAcDm.delete(0,END)
    AsvAcDm.delete(0,END)
    SvAcDm.delete(0,END)
    LvAcDm.delete(0,END)
    DvAcDm.delete(0,END)
    #Aspirant down
    AcvAsDm.delete(0,END)
    AsvAsDm.delete(0,END)
    SvAsDm.delete(0,END)
    LvAsDm.delete(0,END)
    DvAsDm.delete(0,END)
    #Sith down
    AcvSDm.delete(0,END)
    AsvSDm.delete(0,END)
    SvSDm.delete(0,END)
    LvSDm.delete(0,END)
    DvSDm.delete(0,END)
    #Lord down
    AcvLDm.delete(0,END)
    AsvLDm.delete(0,END)
    SvLDm.delete(0,END)
    LvLDm.delete(0,END)
    DvLDm.delete(0,END)
    #Darth down
    AcvDDm.delete(0,END)
    AsvDDm.delete(0,END)
    SvDDm.delete(0,END)
    LvDDm.delete(0,END)
    DvDDm.delete(0,END)
    #update each field
    AcvAc.insert(0,calcSuccess(PersuAcolyteVal,DefAcolyteVal))
    AsvAc.insert(0,calcSuccess(PersuAspirVal,DefAcolyteVal))
    SvAc.insert(0,calcSuccess(PersuSithVal,DefAcolyteVal))
    LvAc.insert(0,calcSuccess(PersuLordVal,DefAcolyteVal))
    DvAc.insert(0,calcSuccess(PersuDarthVal,DefAcolyteVal))
    #Aspirant down
    AcvAs.insert(0,calcSuccess(PersuAcolyteVal,DefAspirVal))
    AsvAs.insert(0,calcSuccess(PersuAspirVal,DefAspirVal))
    SvAs.insert(0,calcSuccess(PersuSithVal,DefAspirVal))
    LvAs.insert(0,calcSuccess(PersuLordVal,DefAspirVal))
    DvAs.insert(0,calcSuccess(PersuDarthVal,DefAspirVal))
    #Sith down
    AcvS.insert(0,calcSuccess(PersuAcolyteVal,DefSithVal))
    AsvS.insert(0,calcSuccess(PersuAspirVal,DefSithVal))
    SvS.insert(0,calcSuccess(PersuSithVal,DefSithVal))
    LvS.insert(0,calcSuccess(PersuLordVal,DefSithVal))
    DvS.insert(0,calcSuccess(PersuDarthVal,DefSithVal))
    #Lord down
    AcvL.insert(0,calcSuccess(PersuAcolyteVal,DefLordVal))
    AsvL.insert(0,calcSuccess(PersuAspirVal,DefLordVal))
    SvL.insert(0,calcSuccess(PersuSithVal,DefLordVal))
    LvL.insert(0,calcSuccess(PersuLordVal,DefLordVal))
    DvL.insert(0,calcSuccess(PersuDarthVal,DefLordVal))
    #Darth down
    AcvD.insert(0,calcSuccess(PersuAcolyteVal,DefDarthVal))
    AsvD.insert(0,calcSuccess(PersuAspirVal,DefDarthVal))
    SvD.insert(0,calcSuccess(PersuSithVal,DefDarthVal))
    LvD.insert(0,calcSuccess(PersuLordVal,DefDarthVal))
    DvD.insert(0,calcSuccess(PersuDarthVal,DefDarthVal))
    #acolyte down
    AcvAc1D.insert(0,calcSuccess(PersuAcolyteVal,DefAcolyteVal+TsAcolyteVal))
    AsvAc1D.insert(0,calcSuccess(PersuAspirVal,DefAcolyteVal+TsAcolyteVal))
    SvAc1D.insert(0,calcSuccess(PersuSithVal,DefAcolyteVal+TsAcolyteVal))
    LvAc1D.insert(0,calcSuccess(PersuLordVal,DefAcolyteVal+TsAcolyteVal))
    DvAc1D.insert(0,calcSuccess(PersuDarthVal,DefAcolyteVal+TsAcolyteVal))
    #Aspirant down
    AcvAs1D.insert(0,calcSuccess(PersuAcolyteVal,DefAspirVal+TsAspirVal))
    AsvAs1D.insert(0,calcSuccess(PersuAspirVal,DefAspirVal+TsAspirVal))
    SvAs1D.insert(0,calcSuccess(PersuSithVal,DefAspirVal+TsAspirVal))
    LvAs1D.insert(0,calcSuccess(PersuLordVal,DefAspirVal+TsAspirVal))
    DvAs1D.insert(0,calcSuccess(PersuDarthVal,DefAspirVal+TsAspirVal))
    #Sith down
    AcvS1D.insert(0,calcSuccess(PersuAcolyteVal,DefSithVal+TsSithVal))
    AsvS1D.insert(0,calcSuccess(PersuAspirVal,DefSithVal+TsSithVal))
    SvS1D.insert(0,calcSuccess(PersuSithVal,DefSithVal+TsSithVal))
    LvS1D.insert(0,calcSuccess(PersuLordVal,DefSithVal+TsSithVal))
    DvS1D.insert(0,calcSuccess(PersuDarthVal,DefSithVal+TsSithVal))
    #Lord down
    AcvL1D.insert(0,calcSuccess(PersuAcolyteVal,DefLordVal+TsLordVal))
    AsvL1D.insert(0,calcSuccess(PersuAspirVal,DefLordVal+TsLordVal))
    SvL1D.insert(0,calcSuccess(PersuSithVal,DefLordVal+TsLordVal))
    LvL1D.insert(0,calcSuccess(PersuLordVal,DefLordVal+TsLordVal))
    DvL1D.insert(0,calcSuccess(PersuDarthVal,DefLordVal+TsLordVal))
    #Darth down
    AcvD1D.insert(0,calcSuccess(PersuAcolyteVal,DefDarthVal+TsDarthVal))
    AsvD1D.insert(0,calcSuccess(PersuAspirVal,DefDarthVal+TsDarthVal))
    SvD1D.insert(0,calcSuccess(PersuSithVal,DefDarthVal+TsDarthVal))
    LvD1D.insert(0,calcSuccess(PersuLordVal,DefDarthVal+TsDarthVal))
    DvD1D.insert(0,calcSuccess(PersuDarthVal,DefDarthVal+TsDarthVal))
    #acolyte down
    AcvAcDm.insert(0,calcSuccess(PersuAcolyteVal+DomAcolyteVal,DefAcolyteVal))
    AsvAcDm.insert(0,calcSuccess(PersuAspirVal+DomAspirVal,DefAcolyteVal))
    SvAcDm.insert(0,calcSuccess(PersuSithVal+DomSithVal,DefAcolyteVal))
    LvAcDm.insert(0,calcSuccess(PersuLordVal+DomLordVal,DefAcolyteVal))
    DvAcDm.insert(0,calcSuccess(PersuDarthVal+DomDarthVal,DefAcolyteVal))
    #Aspirant down
    AcvAsDm.insert(0,calcSuccess(PersuAcolyteVal+DomAcolyteVal,DefAspirVal))
    AsvAsDm.insert(0,calcSuccess(PersuAspirVal+DomAspirVal,DefAspirVal))
    SvAsDm.insert(0,calcSuccess(PersuSithVal+DomSithVal,DefAspirVal))
    LvAsDm.insert(0,calcSuccess(PersuLordVal+DomLordVal,DefAspirVal))
    DvAsDm.insert(0,calcSuccess(PersuDarthVal+DomDarthVal,DefAspirVal))
    #Sith down
    AcvSDm.insert(0,calcSuccess(PersuAcolyteVal+DomAcolyteVal,DefSithVal))
    AsvSDm.insert(0,calcSuccess(PersuAspirVal+DomAspirVal,DefSithVal))
    SvSDm.insert(0,calcSuccess(PersuSithVal+DomSithVal,DefSithVal))
    LvSDm.insert(0,calcSuccess(PersuLordVal+DomLordVal,DefSithVal))
    DvSDm.insert(0,calcSuccess(PersuDarthVal+DomDarthVal,DefSithVal))
    #Lord down
    AcvLDm.insert(0,calcSuccess(PersuAcolyteVal+DomAcolyteVal,DefLordVal))
    AsvLDm.insert(0,calcSuccess(PersuAspirVal+DomAspirVal,DefLordVal))
    SvLDm.insert(0,calcSuccess(PersuSithVal+DomSithVal,DefLordVal))
    LvLDm.insert(0,calcSuccess(PersuLordVal+DomLordVal,DefLordVal))
    DvLDm.insert(0,calcSuccess(PersuDarthVal+DomDarthVal,DefLordVal))
    #Darth down
    AcvDDm.insert(0,calcSuccess(PersuAcolyteVal+DomAcolyteVal,DefDarthVal))
    AsvDDm.insert(0,calcSuccess(PersuAspirVal+DomAspirVal,DefDarthVal))
    SvDDm.insert(0,calcSuccess(PersuSithVal+DomSithVal,DefDarthVal))
    LvDDm.insert(0,calcSuccess(PersuLordVal+DomLordVal,DefDarthVal))
    DvDDm.insert(0,calcSuccess(PersuDarthVal+DomDarthVal,DefDarthVal))
    
PersuAcolyteWatcher.trace('w',updateStatGrids)
PersuAspirWatcher.trace('w',updateStatGrids)
PersuSithWatcher.trace('w',updateStatGrids)
PersuLordWatcher.trace('w',updateStatGrids)
PersuDarthWatcher.trace('w',updateStatGrids)


DefAcolyteWatcher.trace('w',updateStatGrids)
DefAspirWatcher.trace('w',updateStatGrids)
DefSithWatcher.trace('w',updateStatGrids)
DefLordWatcher.trace('w',updateStatGrids)
DefDarthWatcher.trace('w',updateStatGrids)


TsAcolyteWatcher.trace('w',updateStatGrids)
TsAspirWatcher.trace('w',updateStatGrids)
TsSithWatcher.trace('w',updateStatGrids)
TsLordWatcher.trace('w',updateStatGrids)
TsDarthWatcher.trace('w',updateStatGrids)

DomAcolyteWatcher.trace('w',updateStatGrids)
DomAspirWatcher.trace('w',updateStatGrids)
DomSithWatcher.trace('w',updateStatGrids)
DomLordWatcher.trace('w',updateStatGrids)
DomDarthWatcher.trace('w',updateStatGrids)




master.mainloop()

