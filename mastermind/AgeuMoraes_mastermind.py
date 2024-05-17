import tkinter as tk # Importa a biblioteca gráfica Tkinter
import random # Importa a biblioteca random
import os # Módulo que reinicia o programa do zero
import sys # Módulo que reincia o programa do zero


# Cria a tela
screen = tk.Tk()

screen.geometry("1300x700")

# Traz o atributo da tela acima de outras telas como verdade
screen.attributes("-topmost", True)

# Configura a tela para branca
screen.configure(bg="white")

def show_victoria():
    Congratulations = tk.Label(screen, text="PARABÉNS VOCÊ VENCEEU!!!", bg="white", fg="green", font=("Times_New_Roman", 16))
    Congratulations.place(x = 920, y = 150)


def show_defeat():
    derrota = tk.Label(screen, text="VOCÊ PERDEU!!", bg="white", fg="red", font=("Times_New_Roman", 16))
    derrota.place(x = 984, y = 150)


# Função para fechar tela
def close_screen(event):
    # Comando que desliga a tela
    screen.destroy()


# Função para reiniciar o jogo utilizando módulos
def restart(event=None):

    python = sys.executable
    os.execl(python, python, *sys.argv)


# Função para criar o botão de reiniciar
def creates_restart_button():
    
    # Cria botão de Reiniciar
    restart_button = tk.Button(screen, text="Reiniciar", command=lambda:[restart()], bg = "blue", fg = "white")

    # Aplica as coordenadas do botão
    restart_button.place(x = 1030, y = 330)


#Função para mover o canvasJogo para a direita
def move_right():

    def disable_button():
        purple_button.config(state="disable")
        blue_button.config(state="disable")
        green_button.config(state="disable")
        yellow_button.config(state="disable")
        red_button.config(state="disable")
        brown_button.config(state="disable")

    # Mover o retângulo de 50 em 50 pixels para a direita 
    canvas_game.move(rectangle, 50, 0)

    # Verificar se o retângulo alcançou a coordenada (400, 50)
    if canvas_game.coords(rectangle)[0] < 500:
        
        # Agenda a chamada da função novamente após 100ms
        canvas_game.after(150, move_right)

    # É executada se a primeira condicional não for satisfeita
    else:

        # Lista de cores
        colors_list = ["blue", "purple", "brown", "green", "red", "orange"]
        # Embaralha as cores
        random.shuffle(colors_list)
        # Seleciona quatro cores da lista e cria uma nova
        drawn = random.sample(colors_list, 4)
        # Teste que mostra a primeira cor da nova lista
        print(drawn[1])

        # Contador
        s = 0

        # Contador
        r = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for _ in range(0, 4):  

            # Cria o fundo do canvas que fica atrás da bola
            right_answear = tk.Canvas(screen, width=42, height=42, highlightthickness=0)
            # Cria a bola
            right_answear.create_oval(0, 0, 40, 40, fill=drawn[0 + s], outline="black")
            # Configura o canvas para branco
            right_answear.configure(bg="white")
            # posiciona a bola na tela
            right_answear.place(x = 920 + r, y = 250)

            # Soma 1 ao contador
            s += 1
            
            # Soma 90 ao contador 
            r += 90


        hide = tk.Canvas(screen, width=320, height=60, highlightthickness=0)
        hide.configure(bg="white")
        hide.place(x = 920, y = 245)


        # Cria o canvas por trás da faixa cinza
        canva_line_Grey = tk.Canvas(screen, width=64.2, height=460)
        # Cria o retangulo cinza na tela
        canva_line_Grey.create_rectangle(0, 0, 64.8, 462, fill="grey", outline="white", width=10)
        # Configura o canvas para cinza
        canva_line_Grey.configure(bg="grey")
        # Posiciona o retangulo na tela
        canva_line_Grey.place(x=538, y=90)

        # Contador
        n = 0

        # Estrutura de repetição para criar as linhas que dividem as fases do jogo
        for _ in range(0,9):
            
            # Soma 79 ao contador
            n += 47.4

            # Cria o canvas por trás da linha
            canvas_lines = tk.Canvas(screen, width=289.2, height=6, highlightthickness=0)
            # Mostra o canvas na tela

            # Cria a linha na tela
            canvas_lines.create_line(0, 3, 600, 3, fill="white", width=3)
            # Configura o canvas para preto
            canvas_lines.configure(bg="black")
            # Posiciona a linha na tela
            canvas_lines.place(x = 533, y = 555.4 - n)


        # Lista vazia das bolas que não foram preenchidas ainda
        unfilled_balls = []

        # Contador
        c = 0
        
        # Estrutura de repetição para a criação das bolas que o usuário irá preencher com as escolhas dele durante o jogo
        for _ in range (0, 4):
            
            # Soma 90 ao contador
            c += 54


            # Repecitivamente, criam o canvas, mostram eles na tela, criam as bolas, configuram os canvas para preto, posicionam as bolas na tela, e mandam para as listas das bolas não preenchidas  
            canva_ball1 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)        
            canva_ball1.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball1.configure(bg= "black")
            canva_ball1.place(x = 560 + c, y = 520 )
            unfilled_balls.append(canva_ball1)

            canva_ball2 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball2.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball2.configure(bg= "black")
            canva_ball2.place(x = 560 + c, y = 474 )
            unfilled_balls.append(canva_ball2)
 
            canva_ball3 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball3.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball3.configure(bg= "black")
            canva_ball3.place(x = 560 + c, y = 428 )
            unfilled_balls.append(canva_ball3)
  
            canva_ball4 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball4.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball4.configure(bg= "black")
            canva_ball4.place(x = 560 + c, y = 380 )
            unfilled_balls.append(canva_ball4)
 
            canva_ball5 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball5.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball5.configure(bg= "black")
            canva_ball5.place(x = 560 + c, y = 334 )
            unfilled_balls.append(canva_ball5)
 
            canva_ball6 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball6.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball6.configure(bg= "black")
            canva_ball6.place(x = 560 + c, y = 283.5 )
            unfilled_balls.append(canva_ball6)

            canva_ball7 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball7.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball7.configure(bg= "black")
            canva_ball7.place(x = 560 + c, y = 236.5 )
            unfilled_balls.append(canva_ball7)
 
            canva_ball8 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball8.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball8.configure(bg= "black")
            canva_ball8.place(x = 560 + c, y = 190 )
            unfilled_balls.append(canva_ball8)
  
            canva_ball9 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball9.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball9.configure(bg= "black")
            canva_ball9.place(x = 560 + c, y = 142 )
            unfilled_balls.append(canva_ball9)
 
            canva_ball10 = tk.Canvas(screen, width=25.2, height=24.3, highlightthickness=0)
            canva_ball10.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_ball10.configure(bg= "black")
            canva_ball10.place(x = 560 + c, y = 96 )
            unfilled_balls.append(canva_ball10)


        instruct = tk.Label(screen, text="DESCUBRA A ORDEM CORRETA DAS CORES.", bg="white", fg="black", font=("Times_New_Roman",12))
        instruct.place(x = 50, y = 180)

        instruct2 = tk.Label(screen, text="EXEMPLO:", bg="white", fg="black", font=("Times_New_Roman",12))
        instruct2.place(x = 50, y = 200)

        instruct3 = tk.Label(screen, text="BOLA BRANCA SIGNIFICA QUE A COR ESTÁ CERTA,", bg="white", fg="black", font=("Times_New_Roman",10))
        instruct3.place(x = 50, y = 260)

        instruct4 = tk.Label(screen, text=" MAS NO LUGAR ERRADO", bg="white", fg="black", font=("Times_New_Roman",10))
        instruct4.place(x = 45, y = 280)

        instruct5 = tk.Label(screen, text="BOLA PRETA SIGNIFICA QUE A COR ESTÁ CERTA", bg="white", fg="black", font=("Times_New_Roman",10))
        instruct5.place(x = 50, y = 400)

        instruct6 = tk.Label(screen, text=" E NO LUGAR CERTO", bg="white", fg="black", font=("Times_New_Roman",10))
        instruct6.place(x = 45, y = 420)


        # Contador
        v = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for _ in range(0, 2):  

            # Cria o fundo do canvas que fica atrás da bola
            right_answear = tk.Canvas(screen, width=45, height=45, highlightthickness=0)
            # Cria a bola
            right_answear.create_oval(0, 0, 40, 40, fill="white", outline="black")
            # Configura o canvas para branco
            right_answear.configure(bg="white")
            # posiciona a bola na tela
            right_answear.place(x = 80 + v, y = 320)

            
            # Soma 90 ao contador 
            v += 90

        
        # Contador
        t = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for _ in range(0, 2):  

            # Cria o fundo do canvas que fica atrás da bola
            right_answear = tk.Canvas(screen, width=45, height=45, highlightthickness=0)
            # Cria a bola
            right_answear.create_oval(0, 0, 40, 40, fill="black", outline="black")
            # Configura o canvas para branco
            right_answear.configure(bg="white")
            # posiciona a bola na tela
            right_answear.place(x = 80 + t, y = 455)

            
            # Soma 90 ao contador 
            t += 90


        # Listas vazias que irão receber a escolha dos botões feitas pelo usuário
        ball_result = []
        ball_result2 = []
        ball_result3 = []
        ball_result4 = []
        ball_result5 = []
        ball_result6 = []
        ball_result7 = []
        ball_result8 = []
        ball_result9 = []
        ball_result10 = []


        # Função verificadora de lista
        def list_checks():
            
            # Condicionais que avaliam se há quatro cores na lista

            if len(ball_result) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if ball_result[0] in set(drawn) and ball_result[0] != drawn[0]:
                    balls_list[19].itemconfig(1, fill="white")

                if ball_result[1] in set(drawn) and ball_result[1] != drawn[1]:
                    balls_list[39].itemconfig(1, fill="white")

                if ball_result[2] in set(drawn) and ball_result[2] != drawn[2]:
                    balls_list[38].itemconfig(1, fill="white")

                if ball_result[3] in set(drawn) and ball_result[3] != drawn[3]:
                    balls_list[18].itemconfig(1, fill="white")

                
                if ball_result[0] in set(drawn) and ball_result[0] == drawn[0]:
                    balls_list[19].itemconfig(1, fill="black")

                if ball_result[1] in set(drawn) and ball_result[1] == drawn[1]:
                    balls_list[39].itemconfig(1, fill="black")

                if ball_result[2] in set(drawn) and ball_result[2] == drawn[2]:
                    balls_list[38].itemconfig(1, fill="black")

                if ball_result[3] in set(drawn) and ball_result[3] == drawn[3]:
                    balls_list[18].itemconfig(1, fill="black")


            if len(ball_result2) == 4:
              
                if ball_result2[0] in set(drawn) and ball_result2[0] != drawn[0]:
                    balls_list[17].itemconfig(1, fill="white")

                if ball_result2[1] in set(drawn) and ball_result2[1] != drawn[1]:
                    balls_list[37].itemconfig(1, fill="white")

                if ball_result2[2] in set(drawn) and ball_result2[2] != drawn[2]:
                    balls_list[36].itemconfig(1, fill="white")

                if ball_result2[3] in set(drawn) and ball_result2[3] != drawn[3]:
                    balls_list[16].itemconfig(1, fill="white")

              
                if ball_result2[0] in set(drawn) and ball_result2[0] == drawn[0]:
                    balls_list[17].itemconfig(1, fill="black")

                if ball_result2[1] in set(drawn) and ball_result2[1] == drawn[1]:
                    balls_list[37].itemconfig(1, fill="black")

                if ball_result2[2] in set(drawn) and ball_result2[2] == drawn[2]:
                    balls_list[36].itemconfig(1, fill="black")

                if ball_result2[3] in set(drawn) and ball_result2[3] == drawn[3]:
                    balls_list[16].itemconfig(1, fill="black")


            if len(ball_result3) == 4:
               
                if ball_result3[0] in set(drawn) and ball_result3[0] != drawn[0]:
                    balls_list[15].itemconfig(1, fill="white")

                if ball_result3[1] in set(drawn) and ball_result3[1] != drawn[1]:
                    balls_list[35].itemconfig(1, fill="white")

                if ball_result3[2] in set(drawn) and ball_result3[2] != drawn[2]:
                    balls_list[34].itemconfig(1, fill="white")

                if ball_result3[3] in set(drawn) and ball_result3[3] != drawn[3]:
                    balls_list[14].itemconfig(1, fill="white")

            
                if ball_result3[0] in set(drawn) and ball_result3[0] == drawn[0]:
                    balls_list[15].itemconfig(1, fill="black")

                if ball_result3[1] in set(drawn) and ball_result3[1] == drawn[1]:
                    balls_list[35].itemconfig(1, fill="black")

                if ball_result3[2] in set(drawn) and ball_result3[2] == drawn[2]:
                    balls_list[34].itemconfig(1, fill="black")

                if ball_result3[3] in set(drawn) and ball_result3[3] == drawn[3]:
                    balls_list[14].itemconfig(1, fill="black")


            if len(ball_result4) == 4:

                if ball_result4[0] in set(drawn) and ball_result4[0] != drawn[0]:
                    balls_list[13].itemconfig(1, fill="white")

                if ball_result4[1] in set(drawn) and ball_result4[1] != drawn[1]:
                    balls_list[33].itemconfig(1, fill="white")

                if ball_result4[2] in set(drawn) and ball_result4[2] != drawn[2]:
                    balls_list[32].itemconfig(1, fill="white")

                if ball_result4[3] in set(drawn) and ball_result4[3] != drawn[3]:
                    balls_list[12].itemconfig(1, fill="white")

             
                if ball_result4[0] in set(drawn) and ball_result4[0] == drawn[0]:
                    balls_list[13].itemconfig(1, fill="black")

                if ball_result4[1] in set(drawn) and ball_result4[1] == drawn[1]:
                    balls_list[33].itemconfig(1, fill="black")

                if ball_result4[2] in set(drawn) and ball_result4[2] == drawn[2]:
                    balls_list[32].itemconfig(1, fill="black")

                if ball_result4[3] in set(drawn) and ball_result4[3] == drawn[3]:
                    balls_list[12].itemconfig(1, fill="black")


            if len(ball_result5) == 4:

                if ball_result5[0] in set(drawn) and ball_result5[0] != drawn[0]:
                    balls_list[11].itemconfig(1, fill="white")

                if ball_result5[1] in set(drawn) and ball_result5[1] != drawn[1]:
                    balls_list[31].itemconfig(1, fill="white")

                if ball_result5[2] in set(drawn) and ball_result5[2] != drawn[2]:
                    balls_list[30].itemconfig(1, fill="white")

                if ball_result5[3] in set(drawn) and ball_result5[3] != drawn[3]:
                    balls_list[10].itemconfig(1, fill="white")


                if ball_result5[0] in set(drawn) and ball_result5[0] == drawn[0]:
                    balls_list[11].itemconfig(1, fill="black")

                if ball_result5[1] in set(drawn) and ball_result5[1] == drawn[1]:
                    balls_list[31].itemconfig(1, fill="black")

                if ball_result5[2] in set(drawn) and ball_result5[2] == drawn[2]:
                    balls_list[30].itemconfig(1, fill="black")

                if ball_result5[3] in set(drawn) and ball_result5[3] == drawn[3]:
                    balls_list[10].itemconfig(1, fill="black")


            if len(ball_result6) == 4:

                if ball_result6[0] in set(drawn) and ball_result6[0] != drawn[0]:
                    balls_list[9].itemconfig(1, fill="white")

                if ball_result6[1] in set(drawn) and ball_result6[1] != drawn[1]:
                    balls_list[29].itemconfig(1, fill="white")

                if ball_result6[2] in set(drawn) and ball_result6[2] != drawn[2]:
                    balls_list[28].itemconfig(1, fill="white")

                if ball_result6[3] in set(drawn) and ball_result6[3] != drawn[3]:
                    balls_list[8].itemconfig(1, fill="white")


                if ball_result6[0] in set(drawn) and ball_result6[0] == drawn[0]:
                    balls_list[9].itemconfig(1, fill="black")

                if ball_result6[1] in set(drawn) and ball_result6[1] == drawn[1]:
                    balls_list[29].itemconfig(1, fill="black")

                if ball_result6[2] in set(drawn) and ball_result6[2] == drawn[2]:
                    balls_list[28].itemconfig(1, fill="black")

                if ball_result6[3] in set(drawn) and ball_result6[3] == drawn[3]:
                    balls_list[8].itemconfig(1, fill="black")


            if len(ball_result7) == 4:

                if ball_result7[0] in set(drawn) and ball_result7[0] != drawn[0]:
                    balls_list[7].itemconfig(1, fill="white")

                if ball_result7[1] in set(drawn) and ball_result7[1] != drawn[1]:
                    balls_list[27].itemconfig(1, fill="white")

                if ball_result7[2] in set(drawn) and ball_result7[2] != drawn[2]:
                    balls_list[26].itemconfig(1, fill="white")

                if ball_result7[3] in set(drawn) and ball_result7[3] != drawn[3]:
                    balls_list[6].itemconfig(1, fill="white")


                if ball_result7[0] in set(drawn) and ball_result7[0] == drawn[0]:
                    balls_list[7].itemconfig(1, fill="black")

                if ball_result7[1] in set(drawn) and ball_result7[1] == drawn[1]:
                    balls_list[27].itemconfig(1, fill="black")

                if ball_result7[2] in set(drawn) and ball_result7[2] == drawn[2]:
                    balls_list[26].itemconfig(1, fill="black")

                if ball_result7[3] in set(drawn) and ball_result7[3] == drawn[3]:
                    balls_list[6].itemconfig(1, fill="black")


            if len(ball_result8) == 4:

                if ball_result8[0] in set(drawn) and ball_result8[0] != drawn[0]:
                    balls_list[5].itemconfig(1, fill="white")
                
                if ball_result8[1] in set(drawn) and ball_result8[1] != drawn[1]:
                    balls_list[25].itemconfig(1, fill="white")
                
                if ball_result8[2] in set(drawn) and ball_result8[2] != drawn[2]:
                    balls_list[24].itemconfig(1, fill="white")
                
                if ball_result8[3] in set(drawn) and ball_result8[3] != drawn[3]:
                    balls_list[4].itemconfig(1, fill="white")
                

                if ball_result8[0] in set(drawn) and ball_result8[0] == drawn[0]:
                    balls_list[5].itemconfig(1, fill="black")
                
                if ball_result8[1] in set(drawn) and ball_result8[1] == drawn[1]:
                    balls_list[25].itemconfig(1, fill="black")
                
                if ball_result8[2] in set(drawn) and ball_result8[2] == drawn[2]:
                    balls_list[24].itemconfig(1, fill="black")
                
                if ball_result8[3] in set(drawn) and ball_result8[3] == drawn[3]:
                    balls_list[4].itemconfig(1, fill="black")


            if len(ball_result9) == 4:

                if ball_result9[0] in set(drawn) and ball_result9[0] != drawn[0]:
                    balls_list[3].itemconfig(1, fill="white")

                if ball_result9[1] in set(drawn) and ball_result9[1] != drawn[1]:
                    balls_list[23].itemconfig(1, fill="white")

                if ball_result9[2] in set(drawn) and ball_result9[2] != drawn[2]:
                    balls_list[22].itemconfig(1, fill="white")

                if ball_result9[3] in set(drawn) and ball_result9[3] != drawn[3]:
                    balls_list[2].itemconfig(1, fill="white")


                if ball_result9[0] in set(drawn) and ball_result9[0] == drawn[0]:
                    balls_list[3].itemconfig(1, fill="black")

                if ball_result9[1] in set(drawn) and ball_result9[1] == drawn[1]:
                    balls_list[23].itemconfig(1, fill="black")

                if ball_result9[2] in set(drawn) and ball_result9[2] == drawn[2]:
                    balls_list[22].itemconfig(1, fill="black")

                if ball_result9[3] in set(drawn) and ball_result9[3] == drawn[3]:
                    balls_list[2].itemconfig(1, fill="black")

  
            if len(ball_result10) == 4:

                if ball_result10[0] in set(drawn) and ball_result10[0] != drawn[0]:
                    balls_list[1].itemconfig(1, fill="white")
                
                if ball_result10[1] in set(drawn) and ball_result10[1] != drawn[1]:
                    balls_list[21].itemconfig(1, fill="white")
                
                if ball_result10[2] in set(drawn) and ball_result10[2] != drawn[2]:
                    balls_list[20].itemconfig(1, fill="white")
                
                if ball_result10[3] in set(drawn) and ball_result10[3] != drawn[3]:
                    balls_list[0].itemconfig(1, fill="white")
                

                if ball_result10[0] in set(drawn) and ball_result10[0] == drawn[0]:
                    balls_list[1].itemconfig(1, fill="black")
                
                if ball_result10[1] in set(drawn) and ball_result10[1] == drawn[1]:
                    balls_list[21].itemconfig(1, fill="black")
                
                if ball_result10[2] in set(drawn) and ball_result10[2] == drawn[2]:
                    balls_list[20].itemconfig(1, fill="black")
                
                if ball_result10[3] in set(drawn) and ball_result10[3] == drawn[3]:
                    balls_list[0].itemconfig(1, fill="black")


                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if ball_result[0] != drawn[0] or ball_result[1] != drawn[1] or ball_result[2] != drawn[2] or ball_result[3] != drawn[3]:
                    # Limpa lista
                    ball_result.clear()
                    
                if ball_result2[0] != drawn[0] or ball_result2[1] != drawn[1] or ball_result2[2] != drawn[2] or ball_result2[3] != drawn[3]:
                    ball_result2.clear()
 
                if ball_result3[0] != drawn[0] or ball_result3[1] != drawn[1] or ball_result3[2] != drawn[2] or ball_result3[3] != drawn[3]:   
                    ball_result3.clear()

                if ball_result4[0] != drawn[0] or ball_result4[1] != drawn[1] or ball_result4[2] != drawn[2] or ball_result4[3] != drawn[3]:      
                    ball_result4.clear()

                if ball_result5[0] != drawn[0] or ball_result5[1] != drawn[1] or ball_result5[2] != drawn[2] or ball_result5[3] != drawn[3]:   
                    ball_result5.clear()
 
                if ball_result6[0] != drawn[0] or ball_result6[1] != drawn[1] or ball_result6[2] != drawn[2] or ball_result6[3] != drawn[3]:      
                    ball_result6.clear()

                if ball_result7[0] != drawn[0] or ball_result7[1] != drawn[1] or ball_result7[2] != drawn[2] or ball_result7[3] != drawn[3]:      
                    ball_result7.clear()

                if ball_result8[0] != drawn[0] or ball_result8[1] != drawn[1] or ball_result8[2] != drawn[2] or ball_result8[3] != drawn[3]:     
                    ball_result8.clear()

                if ball_result9[0] != drawn[0] or ball_result9[1] != drawn[1] or ball_result9[2] != drawn[2] or ball_result9[3] != drawn[3]:    
                    ball_result.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições, limpa lista, cria botão de reiniciar, desabilita botões, declara derrota e mostra o resultado certo na tela
                if ball_result10[0] != drawn[0] or ball_result10[1] != drawn[1] or ball_result10[2] != drawn[2] or ball_result10[3] != drawn[3]:
                        
                    ball_result10.clear()
                    creates_restart_button()
                    disable_button()
                    show_defeat()  
                    hide.place_forget()

            
            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(ball_result) == 4 and ball_result[0] == drawn[0] and ball_result[1] == drawn[1] and ball_result[2] == drawn[2] and ball_result[3] == drawn[3]:
                # Parâmentro teste
                show_victoria()
                disable_button()
                creates_restart_button()
                # Verifica a lista
                ball_result.clear()
                hide.place_forget()
            
            if len(ball_result2) == 4 and ball_result2[0] == drawn[0] and ball_result2[1] == drawn[1] and ball_result2[2] == drawn[2] and ball_result2[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result2.clear()
                hide.place_forget()

            if len(ball_result3) == 4 and ball_result3[0] == drawn[0] and ball_result3[1] == drawn[1] and ball_result3[2] == drawn[2] and ball_result3[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result3.clear()
                hide.place_forget()

            if len(ball_result4) == 4 and ball_result4[0] == drawn[0] and ball_result4[1] == drawn[1] and ball_result4[2] == drawn[2] and ball_result4[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result4.clear()
                hide.place_forget()

            if len(ball_result5) == 4 and ball_result5[0] == drawn[0] and ball_result5[1] == drawn[1] and ball_result5[2] == drawn[2] and ball_result5[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result5.clear()
                hide.place_forget()

            if len(ball_result6) == 4 and ball_result6[0] == drawn[0] and ball_result6[1] == drawn[1] and ball_result6[2] == drawn[2] and ball_result6[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result6.clear()
                hide.place_forget()
         
            if len(ball_result7) == 4 and ball_result7[0] == drawn[0] and ball_result7[1] == drawn[1] and ball_result7[2] == drawn[2] and ball_result7[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result7.clear()
                hide.place_forget()
       
            if len(ball_result8) == 4 and ball_result8[0] == drawn[0] and ball_result8[1] == drawn[1] and ball_result8[2] == drawn[2] and ball_result8[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result8.clear()
                hide.place_forget()
          
            if len(ball_result9) == 4 and ball_result9[0] == drawn[0] and ball_result9[1] == drawn[1] and ball_result9[2] == drawn[2] and ball_result9[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result9.clear()
                hide.place_forget()
         
            if len(ball_result10) == 4 and ball_result10[0] == drawn[0] and ball_result10[1] == drawn[1] and ball_result10[2] == drawn[2] and ball_result10[3] == drawn[3]:
                show_victoria()
                disable_button()
                creates_restart_button()
                ball_result10.clear()
                hide.place_forget()   
            

            # Se a condicional acima não for satisfeita, o código abaixo é chamado
            else:
                # Agenda a execução da função novamente a cada 100 milissegundos
                screen.after(1000, list_checks)



        # Função para mudar a cor
        def color_change(cor):  
            # Estrutura de repetição que vai ler e ordenar tudo que esta na lista de bolasSemPreencher
            for divisive_integers, ball in enumerate(unfilled_balls):
                # Condicional que só muda de cor se o número divísivel por 10 for inteiro
                if divisive_integers % 10 == 0:
                    # Obtém a cor atual de qualquer uma das bolas
                    current_color = ball.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if current_color == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        ball.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        ball_result.append(cor)
                        # Verifica a lista de escolhas                       
                        list_checks()

                        # Retorna para o começo para esperar a próxima ação
                        return     

            for specifics_balls, ball in enumerate(unfilled_balls):
                # Condicional que só muda de cor se o número for igual aos propostos
                if specifics_balls == 1  or specifics_balls == 11 or specifics_balls == 21 or specifics_balls == 31:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result2.append(cor)                   
                        list_checks()          
                        return
                    
            for specifics_balls, ball in enumerate(unfilled_balls):
                if specifics_balls == 2  or specifics_balls == 12 or specifics_balls == 22 or specifics_balls == 32:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result3.append(cor)                      
                        list_checks()            
                        return
                    
            for specifics_balls, ball in enumerate(unfilled_balls):
                if specifics_balls == 3  or specifics_balls == 13 or specifics_balls == 23 or specifics_balls == 33:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result4.append(cor)                       
                        list_checks()            
                        return 

            for specifics_balls, ball in enumerate(unfilled_balls):
                if specifics_balls == 4  or specifics_balls == 14 or specifics_balls == 24 or specifics_balls == 34:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result5.append(cor)                      
                        list_checks()             
                        return
                    
            for specifics_balls, ball in enumerate(unfilled_balls):
                if specifics_balls == 5  or specifics_balls == 15 or specifics_balls == 25 or specifics_balls == 35:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result6.append(cor)                      
                        list_checks()            
                        return 

            for specifics_balls, ball in enumerate(unfilled_balls):
                if specifics_balls == 6  or specifics_balls == 16 or specifics_balls == 26 or specifics_balls == 36:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result7.append(cor)            
                        list_checks()         
                        return 
                    
            for specifics_balls, ball in enumerate(unfilled_balls):
                if specifics_balls == 7  or specifics_balls == 17 or specifics_balls == 27 or specifics_balls == 37:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result8.append(cor)                    
                        list_checks()            
                        return 


            for specifics_balls, ball in enumerate(unfilled_balls):
                if specifics_balls == 8  or specifics_balls == 18 or specifics_balls == 28 or specifics_balls == 38:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result9.append(cor)                  
                        list_checks()             
                        return 

            for specifics_balls, ball in enumerate(unfilled_balls):
                if specifics_balls == 9  or specifics_balls == 19 or specifics_balls == 29 or specifics_balls == 39:
                    current_color = ball.itemcget(1, "fill")
                    if current_color == "white":
                        ball.itemconfig(1, fill=cor)
                        ball_result10.append(cor)      
                        list_checks()            
                        return
   

        # Criar botões com certas características específicas
        purple_button = tk.Button(screen, command=lambda: (color_change("purple")), bg="purple", fg= "white")
        purple_button.place(x=462, y=600)

        blue_button = tk.Button(screen, command=lambda: (color_change("blue")), bg="blue", fg= "white")
        blue_button.place(x=544, y=600)

        green_button = tk.Button(screen, command=lambda: (color_change("green")), bg="green", fg= "white")
        green_button.place(x=626, y=600)

        yellow_button = tk.Button(screen, command=lambda: (color_change("orange")), bg="orange", fg= "white")
        yellow_button.place(x=708, y=600)

        red_button = tk.Button(screen, command=lambda: (color_change("red")), bg="red", fg= "white")
        red_button.place(x=790, y=600)

        brown_button = tk.Button(screen, command=lambda: (color_change("brown")), bg="brown", fg="white")
        brown_button.place(x=872, y=600)

        # Legenda para o título do jogo
        title = tk.Label(screen, text="JOGO DA SENHA", bg = "white", fg = "black", font = ("Times_New_Roman", 18))
        # Posiciona o título na tela
        title.place(x = 580, y = 30)

        # Instrução para sair da tela
        instruction = tk.Label(screen, text="Pressione 'ESC', para sair do jogo", bg = "white", fg = "black", font = ("Times_New_Roman", 10))
        # Posiciona a instrução na tela
        instruction.place(x = 570)

        # contador
        a = 0
        
        # Mostra todas as cooordenadas de y
        positions_y = [97, 112, 140, 155, 187, 202, 235, 250, 281, 296, 329, 344, 376, 391, 424, 439, 471, 486, 515, 530]

        # Lista vazia para armazenar as bolas que irão indicar se o usuário está no caminho certo
        balls_list = []

        # Estrutura de repetição para criação de bolas
        for _ in range(0,2):
            # Soma 40 ao contador
            a += 24
            # Estrutura de repetição que posiciona cada bola no seu devido lugar
            for y in positions_y:
                # Cria o fundo das bolas
                canvas_hits = tk.Canvas(screen, width=16.8, height=16.8, highlightthickness=0)
                # Cria as bolas
                canvas_hits.create_oval(0, 0, 15, 15, fill="grey", outline="grey")
                # Configura a cor para cinza
                canvas_hits.configure(bg="grey")
                # Define as posições variáveis
                canvas_hits.place(x=525 + a, y=y)
                # Acrescentas as bolas em uma lista vazia para facilitar a chamada 
                balls_list.append(canvas_hits)


# Cria o canvas dentro da janela principal e o deixa com as bordas transparentes
canvas_game = tk.Canvas(screen, width=1000, height=1000, highlightthickness=0)

# Desenha um quadrado ou rentângulo
rectangle = canvas_game.create_rectangle(30, 30, 330, 510, fill="black", outline="blue", width=15)

# Configura o fundo do elemento canva para branco
canvas_game.configure(bg="white")

# Determina o lugar através de coordenadas
canvas_game.place(x=0, y=50)


# Chamar a função move_right() após um atraso de 10 mílisegundo
canvas_game.after(10, move_right)

# Vincula o botão "ESC" a função fechar tela
screen.bind("<Escape>", close_screen)

# Mantêm a tela aberta e operando para sempre verificar quaisquer movomentações dentro dela
screen.mainloop()
