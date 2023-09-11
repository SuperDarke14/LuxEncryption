import cryptography
from cryptography.fernet import Fernet
import tkinter
from tkinter import *
global key
global l

def generateToken():
    global key
    global l
    key = Fernet.generate_key()
    #l = Fernet(key)
    #print(l)
    with open("LuxTokens", 'ab') as LuxTokens:
        LuxTokens.write(key)
    #with open("LuxTokens", "a") as lMod:
        #LuxTokens.write(bytes(l))
def loadToken():
    global key
    global l
    numberOfTokenToRead = int(input("Input index number of key/token pair (should only be even) "))
    numberOfTokenToRead2 = numberOfTokenToRead * 32
    with open("LuxTokens", 'rb') as LuxTokensKey:
        key = LuxTokensKey.read() ## I don't know why doing .read(numberOfTokensToRead2) doesn't let me read the whole byte
    #key = bytes(convertedKey)
    l = Fernet(key)
def batchEncrypt():
    numberOfFilesToEncrypt = int(input("Input number of files to encrypt. \n"))
    for i in range(0, numberOfFilesToEncrypt):
        encryptFile()
def batchDecrypt():
    numberOfFilesToDecrypt = int(input("Input number of files to decrypt. \n"))
    for i in range(0, numberOfFilesToDecrypt):
        decryptFile()
    
#global inputBox

#global continueVar
#continueVar = 0
#class uiButton:
 #   def __init__(self, windowInheritor, commandClick):
  #             self.windowInheritor = windowInheritor
   #            self.commandClick = commandClick
#
 #              Tk.Button__init__(self, windowInheritor, commandClick)
  #             self.__createWidgets
#def mainWindow(): I HATE TKINTER I HATE TKINTER GUI SUCK 
#    homeWindow = Tk()
#    homeWindow.title("Lux Encryption")
#    homeWindow.geometry('800x325')
#    frame = Frame(homeWindow)
#    frame.grid()
#    welcomeLabel = Label(homeWindow, text= "Lux Encryption Methods")
#    welcomeLabel.grid(row = 0, column = 1)
#    encryptAFile = Button(homeWindow, command = encryptButtonClicked, text = 'Encrypt A File')
#    encryptAFile.grid(row = 1, column = 1)
#    decryptAFile = Button(homeWindow, command = decryptButtonClicked, text = "Decrypt a File")
#    decryptAFile.grid(row = 2, column = 1) 
#    global inputBox
#    global continueVar
#    inputBoxLabel = Label(homeWindow, text = "Input: ")
#    inputBoxLabel.grid(row = 0, column = 0)
#    inputBox = Entry(homeWindow, text = "Directory of file to use")
#    inputBox.grid(row = 3, column = 0)
#    inputButton = Button(homeWindow, text = 'Entry', command = sendEntry)
#    inputButton.grid(row = 4, column = 0)
#    if continueVar == 0:
#        inputBox.delete(0)
#        entryShenaniganWindow()
#    homeWindow.mainloop()
#def entryShenaniganWindow():
#    global okButton
#    global entryShenanigan
#    entryShenanigan = Tk()
#    entryShenanigan.title("Input") 
#    entryShenanigan.geometry('2000x200')
#    info = Label(entryShenanigan, text = "Input the text of the file directory, click the ENTRY button, \n and then type in the file name to be decrypted/encrypted, and then click OK in this window") 
#    info.grid(row = 0, column = 1)
#    okButton = Button(entryShenanigan, text = "OK", command = quitCommand)
#    okButton.grid(row = 1, column = 1)
#    entryShenanigan.mainloop()
#def quitCommand():
#    global okButton
#    global continueVar
#    global entryShenanigan
#    continueVar = 1
#    entryShenanigan.destroy()
#def sendEntry():
#    global enteredText
#    global inputBox
#
#    enteredText = inputBox.get()
#def encryptButtonClicked():
#    global continueVar
#    continueVar = 1
#    encryptFile()
#def decryptButtonClicked():
#    global continueVar
continueVar = 1
#    decryptFile()
def encryptFile():
    global l
    global key
    #global enteredText
    #global continueVar
    #cryptWindow()
    continueVar = 1
    activeDirectory = input("Input the path to the file for encryption. ")
    try:
        os.chdir(activeDirectory)
    except:
        print("Something went wrong here. Staying in this file")
    finally:
        if continueVar == 1:
            activeFile = input("Input file for encryption")
            ygrec = open(activeFile, "r")
            stringOfFile = ygrec.read()
            ygrec.close()
            ygrec = open(activeFile, 'wb')
            xray = bytes(stringOfFile, 'utf-8')
            papa = l.encrypt(xray)
            funky = ygrec.write(papa)
            ygrec.close()
            continueVar = 0
def decryptFile():
    global l
    global key
    continueVar = 1
    #global continueVar
    #global enteredText
    #cryptWindow()
    activeDirectory = input("Input file path for decryption")
    #entryShenaniganWindow()
    
    try:
        os.chdir(activeDirectory)
    except:
        print("Something went wrong here. Staying in this file")
    finally:
        if continueVar == 1:
            activeFile = input("Input file name for decryption")
            foxtrot = open(activeFile, "rb")
            encryptedData = foxtrot.read()
            foxtrot.close()
            kilo = open(activeFile, "wb")
            sierra = l.decrypt(encryptedData)
            omicron = kilo.write(sierra)
            continueVar = 0
def initialize():
    print("Welcome to Lux File encryption. \n  Please input a mode to activate. [encrypt / decrypt /generateToken / load token / quit]")
    holdingCell = input()
    if holdingCell == "encrypt":
        encryptFile()
        initialize()
    elif holdingCell == "decrypt":
        decryptFile()
        initialize()
    elif holdingCell == "load token":
        loadToken()
        initialize()
    elif holdingCell == "generateToken":
        generateToken()
        initialize()
    elif holdingCell == "batchEncrypt":
        batchEncrypt()
        initialize()
    elif holdingCell == "batchDecrypt":
        batchDecrypt()
        initialize()
    elif holdingCell == "q" or "quit":
        print("Goodbye. \n")
    else:
        print("Invalid input. Please input as [encrypt / decrypt / generate token / load token /quit]")
        initialize()
initialize()

#def encryptFunction():
 #   global key
  #  global token
   # f = Fernet(key)#
#    token = input("Message to be encrypted")
 #   print(token)
  #  token = f.encrypt(b"token")
   # print(token)
   # while True:
  #      repeatAnswer = input("Encrypt another message? [y/n]")
 #       print(repeatAnswer)
#        if repeatAnswer == "y":
 #           repeatAnswer = None
  #          encryptFunction()
   #     else:
    #        repeatAnswer = None
     #       break
      #  break
