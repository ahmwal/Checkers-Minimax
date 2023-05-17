from auxil import *
from minimax_alphabeta import *

def checkWindow(fig1):
    if not (plt.fignum_exists(fig1.number)):
        quit()
        
def main():
    
    m = tk.Tk()
    def closeWindow():
        m.destroy()
    
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            quit()

    m.protocol("WM_DELETE_WINDOW", on_closing)
    
    diff = tk.IntVar()
    cType = tk.IntVar()

    diff1 = tk.Radiobutton(m, text='Difficulty 1', variable=diff, value=0)
    diff1.pack()
    
    diff2 = tk.Radiobutton(m, text='Difficulty 2', variable=diff, value=1)
    diff2.pack()
    
    diff3 = tk.Radiobutton(m, text='Difficulty 3', variable=diff, value=2)
    diff3.pack()

    def dis(diff1, diff2, diff3):
        s = tk.DISABLED
        diff1.configure(state=s)
        diff2.configure(state=s)
        diff3.configure(state=s)

    def en(diff1, diff2, diff3):
        s = tk.NORMAL
        diff1.configure(state=s)
        diff2.configure(state=s)
        diff3.configure(state=s)
    
    type1 = tk.Radiobutton(m, text='Minimax player', variable=cType, value=0, command= lambda: en(diff1, diff2, diff3))
    type1.pack()
    type2 = tk.Radiobutton(m, text='Random player', variable=cType, value=1, command= lambda: dis(diff1, diff2, diff3))
    type2.pack()
    
    B = tk.Button(m, text ="Start", command = closeWindow)
    B.pack()
    m.mainloop()
    
    diff = diff.get()
    cType = cType.get()
    
    base_board = [[ 0,'W',0,'W',0,'W',0,'W'],
                  ['W',0,'W',0,'W',0,'W',0 ],
                  [ 0,'W',0,'W',0,'W',0,'W'],
                  [ 1, 0, 1, 0, 1, 0, 1, 0 ],
                  [ 0, 1 ,0 ,1, 0, 1, 0, 1 ],
                  ['B',0,'B',0,'B',0,'B',0 ],
                  [ 0,'B',0,'B',0,'B',0,'B'],
                  ['B',0,'B',0,'B',0,'B',0 ]]   
    
    currentState = copy.deepcopy(base_board)
       
    dst = Image.new('RGB', color = (255, 255, 255), size = (200 * 8, 200 * 8))
    
    fig1, ax = plt.subplots()
    ax.axis('off')
    im = ax.imshow(dst)   
    
    drawBoard(fig1, im, base_board)

    alpha = -math.inf
    beta = math.inf
    maxdepth = 5
    
    while True:
        
        checkWindow(fig1)
        max = "B"
        w = checkWin(max, currentState)
        if w:
            break
            
        #Agent(Black) starts game.
        ax.set_title("Black's turn.")
        _, currentState = minimax(currentState, max, alpha, beta, 0, maxdepth)
        drawBoard(fig1, im, currentState)
        for i in range(3):
            checkWindow(fig1)
            time.sleep(1)
        
        #Computer(White) turn.
        max = "W"
        ax.set_title("White's turn.")
        if(not cType):
            _, currentState = minimax(currentState, max, alpha, beta, 0, 2 + diff)
        else:
            currentState = randomPlayer(currentState, max)
            
        drawBoard(fig1, im, currentState)
        for i in range(3):
            checkWindow(fig1)
            time.sleep(1)
    
    if (w == "B"):
        ax.set_title("Black wins!")
    else:
        ax.set_title("White wins!")
    
    drawBoard(fig1, im, currentState)
    time.sleep(5)
    
if __name__ == "__main__":
    main()