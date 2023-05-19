import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 
import copy
import math
import random
import tkinter as tk
from tkinter import messagebox
import time
import matplotlib.pyplot as plt
from collections import Counter

def drawBoard(fig1, im, state):
    white = Image.open("whiteChecker.png")
    white = white.convert("RGBA")
    black = Image.open("blackChecker.png")
    black = black.convert("RGBA")
    Kwhite = Image.open("KwhiteChecker.png")
    Kwhite = Kwhite.convert("RGBA")
    Kblack = Image.open("KblackChecker.png")
    Kblack = Kblack.convert("RGBA")
    box = Image.new('RGB', color = (0, 0, 0), size = (200 , 200))
    dst = Image.new('RGB', color = (245, 245, 245), size = (200 * 8, 200 * 8))
    x = 0
    y = 0

    for row in state:
        i = 0
        for el in row:
            if(el == 0):
                x += 200
            
            if(el == 1):
                dst.paste(box, (x, y))
                x += 200
             
            if(el == 'B'):
                dst.paste(box, (x, y))
                dst.paste(black, (x, y))
                x += 200
            
            if(el == 'W'):
                dst.paste(box, (x, y))
                dst.paste(white, (x, y))
                x += 200
                
            if(el == 'KB'):
                dst.paste(box, (x, y))
                dst.paste(Kblack, (x, y))
                x += 200
            
            if(el == 'KW'):
                dst.paste(box, (x, y))
                dst.paste(Kwhite, (x, y))
                x += 200
                
        y += 200
        x = 0
    
    im.set_data(dst)
    fig1.canvas.draw_idle()
    plt.pause(1)
    
def jump(k, m, ls, li, state, max):
    #Potentially modify to use heuristic in choosing which to check if can check more than one.
    while True:
        if (k+2 <= ls - 1 and m-2 >= 0 and state[k+1][m-1] != max and state[k+1][m-1] != 'K' + max and state[k+1][m-1] != 0 and state[k+1][m-1] != 1):
            if (state[k+2][m-2] == 1):                                
                state[k][m] = 1
                state[k+1][m-1] = 1
                state[k+2][m-2] = max
                if (k+2 == ls - 1):
                    state[k+2][m-2] = 'K' + max
                k += 2
                m -= 2
                continue
        
        if (k+2 <= ls - 1 and m+2 <= li - 1 and state[k+1][m+1] != max and state[k+1][m+1] != 'K' + max and state[k+1][m+1] != 0 and state[k+1][m+1] != 1):
            if (state[k+2][m+2] == 1):
                state[k][m] = 1
                state[k+1][m+1] = 1
                state[k+2][m+2] = max
                if (k+2 == ls - 1):
                    state[k+2][m+2] = 'K' + max          
                k += 2
                m += 2    
                continue
                
        break
    
    return state

def kJump(k, m, ls, li, state, max):
    #Potentially modify to use heuristic in choosing which to check if can check more than one.
    while True:
        if (k-2 >= 0 and m-2 >= 0 and state[k-1][m-1] != max and state[k-1][m-1] != 'K' + max and state[k-1][m-1] != 0 and state[k-1][m-1] != 1):
            if (state[k-2][m-2] == 1):
                state[k][m] = 1
                state[k-1][m-1] = 1
                state[k-2][m-2] = 'K' + max                       
                k -= 2
                m -= 2
                continue
        
        if (k-2 >= 0 and m+2 <= li - 1 and state[k-1][m+1] != max and state[k-1][m+1] != 'K' + max and state[k-1][m+1] != 0 and state[k-1][m+1] != 1):
            if (state[k-2][m+2] == 1):
                state[k][m] = 1
                state[k-1][m+1] = 1
                state[k-2][m+2] = 'K' + max                        
                k -= 2
                m += 2  
                continue

        if (k+2 <= ls - 1 and m-2 >= 0 and state[k+1][m-1] != max and state[k+1][m-1] != 'K' + max and state[k+1][m-1] != 0 and state[k+1][m-1] != 1):
            if (state[k+2][m-2] == 1):                               
                state[k][m] = 1
                state[k+1][m-1] = 1
                state[k+2][m-2] = 'K' + max                
                k += 2
                m -= 2
                continue

        if (k+2 <= ls - 1 and m+2 <= li - 1 and state[k+1][m+1] != max and state[k+1][m+1] != 'K' + max and state[k+1][m+1] != 0 and state[k+1][m+1] != 1):
            if (state[k+2][m+2] == 1):
                state[k][m] = 1
                state[k+1][m+1] = 1
                state[k+2][m+2] = 'K' + max                                        
                k += 2
                m += 2    
                continue
                
        break
    
    return state

def rev(n):
    n.reverse()
    for s in n:
        s.reverse()

def getPossibleMoves(max, state):
    moves = []
    ogState = []
    
    ogState = copy.deepcopy(state)
    if(max == "B"):
        rev(ogState)
    
    
    for i in range(len(ogState)):
        for j in range(len(ogState[i])):
            if(ogState[i][j] == max or ogState[i][j] == 'K' + max):
                if (i + 1 <= len(ogState) - 1):
                    if (j - 1 >= 0):
                        if(ogState[i+1][j-1] == 1):
                            if (i+1 == len(ogState) - 1 or ogState[i][j] == 'K' + max):
                                ogState[i+1][j-1] = 'K' + max
                            else:
                                ogState[i+1][j-1] = max
                                
                            ogState[i][j] = 1        
                        
                        
                        if(max == "B"):
                            rev(ogState)
                        
                        if(ogState in moves):
                            ogState = copy.deepcopy(state)
                        elif(state != ogState):
                            moves.append(ogState)
                            ogState = copy.deepcopy(state) 
                            
                        if(max == "B"):
                            rev(ogState)
                            
                        k = i
                        m = j
                        ogState = jump(k, m, len(ogState), len(ogState[i]), ogState, max)
                        
                        if(max == "B"):
                            rev(ogState)
                        
                        if(ogState in moves):
                            ogState = copy.deepcopy(state)
                        elif(state != ogState):
                            moves.append(ogState)
                            ogState = copy.deepcopy(state) 
                            
                        if(max == "B"):
                            rev(ogState)
                    
                    if (j + 1 <= len(ogState[i]) - 1):
                        if (ogState[i+1][j+1] == 1):
                            if (i+1 == len(ogState) - 1 or ogState[i][j] == 'K' + max):
                                ogState[i+1][j+1] = 'K' + max
                            else:
                                ogState[i+1][j+1] = max
                                
                            ogState[i][j] = 1
                            
                        if(max == "B"):
                            rev(ogState)
                        
                        if(ogState in moves):
                            ogState = copy.deepcopy(state)
                        elif(state != ogState):
                            moves.append(ogState)
                            ogState = copy.deepcopy(state) 
                            
                        if(max == "B"):
                            rev(ogState)
                            
                        k = i
                        m = j
                        ogState = jump(k, m, len(ogState), len(ogState[i]), ogState, max)
                       
                        
                        if(max == "B"):
                            rev(ogState)
                        
                        if(ogState in moves):
                            ogState = copy.deepcopy(state)
                        elif(state != ogState):
                            moves.append(ogState)
                            ogState = copy.deepcopy(state) 
                            
                        if(max == "B"):
                            rev(ogState) 
                    

                if(ogState[i][j] == 'K' + max):
                    if (i - 1 >= 0):
                        if (j - 1 >= 0):
                            if (ogState[i-1][j-1] == 1):
                                ogState[i][j] = 1
                                ogState[i-1][j-1] = 'K' + max                                  


                        if(max == "B"):
                            rev(ogState)
                        
                        if(ogState in moves):
                            ogState = copy.deepcopy(state)
                        elif(state != ogState):
                            moves.append(ogState)
                            ogState = copy.deepcopy(state) 
                            
                        if(max == "B"):
                            rev(ogState)
                             
                            k = i
                            m = j
                            ogState = kJump(k, m, len(ogState), len(ogState[i]), ogState, max)
                                    
                        if(max == "B"):
                            rev(ogState)
                        
                        if(ogState in moves):
                            ogState = copy.deepcopy(state)
                        elif(state != ogState):
                            moves.append(ogState)
                            ogState = copy.deepcopy(state) 
                            
                        if(max == "B"):
                            rev(ogState)


                        if (j + 1 <= len(ogState[i]) - 1):
                            if (ogState[i-1][j+1] == 1):
                                ogState[i][j] = 1
                                ogState[i-1][j+1] = 'K' + max                                    

                            if(max == "B"):
                                rev(ogState)
                            
                            if(ogState in moves):
                                ogState = copy.deepcopy(state)
                            elif(state != ogState):
                                moves.append(ogState)
                                ogState = copy.deepcopy(state) 
                                
                            if(max == "B"):
                                rev(ogState)

                                
                            k = i
                            m = j
                            ogState = kJump(k, m, len(ogState), len(ogState[i]), ogState, max)
                                
                            if(max == "B"):
                                rev(ogState)
                            
                            if(ogState in moves):
                                ogState = copy.deepcopy(state)
                            elif(state != ogState):
                                moves.append(ogState)
                                ogState = copy.deepcopy(state) 
                                
                            if(max == "B"):
                                rev(ogState)
 
 

    return moves                        


def getNumCapturesPos(max, state):
    cB = 1
    cW = 1
    ls = len(state)
    li = len(state[0])

    for i in range(ls):
        for j in range(li):  
            k = i
            m = j
            while True:
                if (state[i][j] == 'K' + max):
                    if (k-2 >= 0 and m-2 >= 0 and state[k-1][m-1] != max and state[k-1][m-1] != 'K' + max and state[k-1][m-1] != 0 and state[k-1][m-1] != 1):
                        if (state[k-2][m-2] == 1):
                            if state[i][j] == "B":
                                cB += 1
                            elif state[i][j] == "W":
                                cW += 1
                    
                    if (k-2 >= 0 and m+2 <= li - 1 and state[k-1][m+1] != max and state[k-1][m+1] != 'K' + max and state[k-1][m+1] != 0 and state[k-1][m+1] != 1):
                        if (state[k-2][m+2] == 1):
                            if state[i][j] == "B":
                                cB += 1
                            elif state[i][j] == "W":
                                cW += 1
                
                if (k+2 <= ls - 1 and m-2 >= 0 and state[k+1][m-1] != max and state[k+1][m-1] != 'K' + max and state[k+1][m-1] != 0 and state[k+1][m-1] != 1):
                    if (state[k+2][m-2] == 1):                               
                        if state[i][j] == "B":
                            cB += 1
                        elif state[i][j] == "W":
                            cW += 1

                if (k+2 <= ls - 1 and m+2 <= li - 1 and state[k+1][m+1] != max and state[k+1][m+1] != 'K' + max and state[k+1][m+1] != 0 and state[k+1][m+1] != 1):
                    if (state[k+2][m+2] == 1):
                        if state[i][j] == "B":
                            cB += 1
                        elif state[i][j] == "W":
                            cW += 1  
                        
                break    
    
    return cB*9, cW*9
                            
def getBoardValue(max, state):
    B = 0
    W = 0
    KB = 0
    KW = 0
    TB = 0
    cB = 1
    cW = 1
    for row in state:
        B += row.count("B")
        W += row.count("W")
        KB += row.count("KB")
        KW += row.count("KW")
    
    cB, cW = getNumCapturesPos(max, state)
    
    TB = int((((B + (1.30*KB))+cB) - (((W + (1.30*KW)))+cW)))
    
    return (B+KB), (W+KW), TB
    
def checkWin(max, state):
    TB, TW, _ = getBoardValue(max, state) 
    
    if (TW == 0):
        return "B"
    
    if (TB == 0):
        return "W"
    
    return False