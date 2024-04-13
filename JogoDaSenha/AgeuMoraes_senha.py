import tkinter as tk # Importa a biblioteca gráfica Tkinter
import random # Importa a biblioteca random
import os # Módulo que reinicia o programa do zero
import sys # Módulo que reincia o programa do zero


# Cria a tela
tela = tk.Tk()

tela.geometry("1300x700")

# Traz o atributo da tela acima de outras telas como verdade
tela.attributes("-topmost", True)

# Configura a tela para branca
tela.configure(bg="white")

def mostrar_triunfo():
    parabens = tk.Label(tela, text="PARABÉNS VOCÊ VENCEEU!!!", bg="white", fg="green", font=("Times_New_Roman", 16))
    parabens.place(x = 920, y = 150)


def mostrar_derrota():
    derrota = tk.Label(tela, text="VOCÊ PERDEU!!", bg="white", fg="red", font=("Times_New_Roman", 16))
    derrota.place(x = 984, y = 150)


# Função para fechar tela
def fecha_tela(event):
    # Comando que desliga a tela
    tela.destroy()


# Função para reiniciar o jogo utilizando módulos
def reiniciar(event=None):

    python = sys.executable
    os.execl(python, python, *sys.argv)


# Função para criar o botão de reiniciar
def criar_botao_reiniciar():
    
    # Cria botão de Reiniciar
    botao_reiniciar = tk.Button(tela, text="Reiniciar", command=lambda:[reiniciar()], bg = "blue", fg = "white")

    # Aplica as coordenadas do botão
    botao_reiniciar.place(x = 1030, y = 330)


#Função para mover o canvasJogo para a direita
def mover_direita():

    def desabilitar_botao():
        botao_roxo.config(state="disable")
        botao_azul.config(state="disable")
        botao_verde.config(state="disable")
        botao_amarelo.config(state="disable")
        botao_vermelho.config(state="disable")
        botao_marrom.config(state="disable")

    # Mover o retângulo de 50 em 50 pixels para a direita 
    canvas_jogo.move(retangulo, 50, 0)

    # Verificar se o retângulo alcançou a coordenada (400, 50)
    if canvas_jogo.coords(retangulo)[0] < 500:
        
        # Agenda a chamada da função novamente após 100ms
        canvas_jogo.after(150, mover_direita)

    # É executada se a primeira condicional não for satisfeita
    else:

        # Lista de cores
        lista_cores = ["blue", "purple", "brown", "green", "red", "orange"]
        # Embaralha as cores
        random.shuffle(lista_cores)
        # Seleciona quatro cores da lista e cria uma nova
        sorteada = random.sample(lista_cores, 4)
        # Teste que mostra a primeira cor da nova lista
        print(sorteada[1])

        # Contador
        s = 0

        # Contador
        r = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for _ in range(0, 4):  

            # Cria o fundo do canvas que fica atrás da bola
            resposta_certa = tk.Canvas(tela, width=42, height=42, highlightthickness=0)
            # Cria a bola
            resposta_certa.create_oval(0, 0, 40, 40, fill=sorteada[0 + s], outline="black")
            # Configura o canvas para branco
            resposta_certa.configure(bg="white")
            # posiciona a bola na tela
            resposta_certa.place(x = 920 + r, y = 250)

            # Soma 1 ao contador
            s += 1
            
            # Soma 90 ao contador 
            r += 90


        esconder = tk.Canvas(tela, width=320, height=60, highlightthickness=0)
        esconder.configure(bg="white")
        esconder.place(x = 920, y = 245)


        # Cria o canvas por trás da faixa cinza
        canva_faixa = tk.Canvas(tela, width=64.2, height=460)
        # Cria o retangulo cinza na tela
        canva_faixa.create_rectangle(0, 0, 64.8, 462, fill="grey", outline="white", width=10)
        # Configura o canvas para cinza
        canva_faixa.configure(bg="grey")
        # Posiciona o retangulo na tela
        canva_faixa.place(x=538, y=90)

        # Contador
        n = 0

        # Estrutura de repetição para criar as linhas que dividem as fases do jogo
        for _ in range(0,9):
            
            # Soma 79 ao contador
            n += 47.4

            # Cria o canvas por trás da linha
            canvas_linhas = tk.Canvas(tela, width=289.2, height=6, highlightthickness=0)
            # Mostra o canvas na tela

            # Cria a linha na tela
            canvas_linhas.create_line(0, 3, 600, 3, fill="white", width=3)
            # Configura o canvas para preto
            canvas_linhas.configure(bg="black")
            # Posiciona a linha na tela
            canvas_linhas.place(x = 533, y = 555.4 - n)


        # Lista vazia das bolas que não foram preenchidas ainda
        bolas_sem_preencher = []

        # Contador
        c = 0
        
        # Estrutura de repetição para a criação das bolas que o usuário irá preencher com as escolhas dele durante o jogo
        for _ in range (0, 4):
            
            # Soma 90 ao contador
            c += 54


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola1 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)        
            canva_bola1.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola1.configure(bg= "black")
            canva_bola1.place(x = 560 + c, y = 520 )
            bolas_sem_preencher.append(canva_bola1)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola2 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola2.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola2.configure(bg= "black")
            canva_bola2.place(x = 560 + c, y = 474 )
            bolas_sem_preencher.append(canva_bola2)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola3 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola3.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola3.configure(bg= "black")
            canva_bola3.place(x = 560 + c, y = 428 )
            bolas_sem_preencher.append(canva_bola3)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola4 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola4.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola4.configure(bg= "black")
            canva_bola4.place(x = 560 + c, y = 380 )
            bolas_sem_preencher.append(canva_bola4)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola5 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola5.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola5.configure(bg= "black")
            canva_bola5.place(x = 560 + c, y = 334 )
            bolas_sem_preencher.append(canva_bola5)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola6 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola6.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola6.configure(bg= "black")
            canva_bola6.place(x = 560 + c, y = 283.5 )
            bolas_sem_preencher.append(canva_bola6)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola7 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola7.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola7.configure(bg= "black")
            canva_bola7.place(x = 560 + c, y = 236.5 )
            bolas_sem_preencher.append(canva_bola7)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola8 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola8.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola8.configure(bg= "black")
            canva_bola8.place(x = 560 + c, y = 190 )
            bolas_sem_preencher.append(canva_bola8)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola9 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola9.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola9.configure(bg= "black")
            canva_bola9.place(x = 560 + c, y = 142 )
            bolas_sem_preencher.append(canva_bola9)


            # Repecitivamente, cria o canvas, mostra ele na tela, cria a bola, configura o canva para preto, posiciona a bola na tela, e manda para a lista das bolas não preenchidas  
            canva_bola10 = tk.Canvas(tela, width=25.2, height=24.3, highlightthickness=0)
            canva_bola10.create_oval(0, 0, 24, 24, fill="white", outline="black")
            canva_bola10.configure(bg= "black")
            canva_bola10.place(x = 560 + c, y = 96 )
            bolas_sem_preencher.append(canva_bola10)


        instruir = tk.Label(tela, text="DESCUBRA A ORDEM CORRETA DAS CORES.", bg="white", fg="black", font=("Times_New_Roman",12))
        instruir.place(x = 50, y = 180)

        instruir2 = tk.Label(tela, text="EXEMPLO:", bg="white", fg="black", font=("Times_New_Roman",12))
        instruir2.place(x = 50, y = 200)

        instruir3 = tk.Label(tela, text="BOLA BRANCA SIGNIFICA QUE A COR ESTÁ CERTA,", bg="white", fg="black", font=("Times_New_Roman",10))
        instruir3.place(x = 50, y = 260)

        instruir4 = tk.Label(tela, text=" MAS NO LUGAR ERRADO", bg="white", fg="black", font=("Times_New_Roman",10))
        instruir4.place(x = 45, y = 280)

        instruir5 = tk.Label(tela, text="BOLA PRETA SIGNIFICA QUE A COR ESTÁ CERTA", bg="white", fg="black", font=("Times_New_Roman",10))
        instruir5.place(x = 50, y = 400)

        instruir6 = tk.Label(tela, text=" E NO LUGAR CERTO", bg="white", fg="black", font=("Times_New_Roman",10))
        instruir6.place(x = 45, y = 420)


        # Contador
        v = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for _ in range(0, 2):  

            # Cria o fundo do canvas que fica atrás da bola
            resposta_certa = tk.Canvas(tela, width=45, height=45, highlightthickness=0)
            # Cria a bola
            resposta_certa.create_oval(0, 0, 40, 40, fill="white", outline="black")
            # Configura o canvas para branco
            resposta_certa.configure(bg="white")
            # posiciona a bola na tela
            resposta_certa.place(x = 80 + v, y = 320)

            
            # Soma 90 ao contador 
            v += 90

        
        # Contador
        t = 0

        # Estrutura de repetição para a criação das bolas que foram selecionadas aleatóriamente
        for _ in range(0, 2):  

            # Cria o fundo do canvas que fica atrás da bola
            resposta_certa = tk.Canvas(tela, width=45, height=45, highlightthickness=0)
            # Cria a bola
            resposta_certa.create_oval(0, 0, 40, 40, fill="black", outline="black")
            # Configura o canvas para branco
            resposta_certa.configure(bg="white")
            # posiciona a bola na tela
            resposta_certa.place(x = 80 + t, y = 455)

            
            # Soma 90 ao contador 
            t += 90


        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado2 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado3 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado4 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado5 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado6 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado7 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado8 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado9 = []

        # Lista vazia que irá receber a escolha dos botões feitas pelo usuário
        bolas_resultado10 = []


        # Função verificadora de lista
        def verificar_lista():
            
            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado[0] in set(sorteada) and bolas_resultado[0] != sorteada[0]:
                    lista_bolas[19].itemconfig(1, fill="white")

                if bolas_resultado[1] in set(sorteada) and bolas_resultado[1] != sorteada[1]:
                    lista_bolas[39].itemconfig(1, fill="white")

                if bolas_resultado[2] in set(sorteada) and bolas_resultado[2] != sorteada[2]:
                    lista_bolas[38].itemconfig(1, fill="white")

                if bolas_resultado[3] in set(sorteada) and bolas_resultado[3] != sorteada[3]:
                    lista_bolas[18].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolas_resultado[0] in set(sorteada) and bolas_resultado[0] == sorteada[0]:
                    lista_bolas[19].itemconfig(1, fill="black")

                if bolas_resultado[1] in set(sorteada) and bolas_resultado[1] == sorteada[1]:
                    lista_bolas[39].itemconfig(1, fill="black")

                if bolas_resultado[2] in set(sorteada) and bolas_resultado[2] == sorteada[2]:
                    lista_bolas[38].itemconfig(1, fill="black")

                if bolas_resultado[3] in set(sorteada) and bolas_resultado[3] == sorteada[3]:
                    lista_bolas[18].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado2) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolas_resultado2[0] in set(sorteada) and bolas_resultado2[0] != sorteada[0]:
                    lista_bolas[17].itemconfig(1, fill="white")

                if bolas_resultado2[1] in set(sorteada) and bolas_resultado2[1] != sorteada[1]:
                    lista_bolas[37].itemconfig(1, fill="white")

                if bolas_resultado2[2] in set(sorteada) and bolas_resultado2[2] != sorteada[2]:
                    lista_bolas[36].itemconfig(1, fill="white")

                if bolas_resultado2[3] in set(sorteada) and bolas_resultado2[3] != sorteada[3]:
                    lista_bolas[16].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolas_resultado2[0] in set(sorteada) and bolas_resultado2[0] == sorteada[0]:
                    lista_bolas[17].itemconfig(1, fill="black")

                if bolas_resultado2[1] in set(sorteada) and bolas_resultado2[1] == sorteada[1]:
                    lista_bolas[37].itemconfig(1, fill="black")

                if bolas_resultado2[2] in set(sorteada) and bolas_resultado2[2] == sorteada[2]:
                    lista_bolas[36].itemconfig(1, fill="black")

                if bolas_resultado2[3] in set(sorteada) and bolas_resultado2[3] == sorteada[3]:
                    lista_bolas[16].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado3) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolas_resultado3[0] in set(sorteada) and bolas_resultado3[0] != sorteada[0]:
                    lista_bolas[15].itemconfig(1, fill="white")

                if bolas_resultado3[1] in set(sorteada) and bolas_resultado3[1] != sorteada[1]:
                    lista_bolas[35].itemconfig(1, fill="white")

                if bolas_resultado3[2] in set(sorteada) and bolas_resultado3[2] != sorteada[2]:
                    lista_bolas[34].itemconfig(1, fill="white")

                if bolas_resultado3[3] in set(sorteada) and bolas_resultado3[3] != sorteada[3]:
                    lista_bolas[14].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada               
                if bolas_resultado3[0] in set(sorteada) and bolas_resultado3[0] == sorteada[0]:
                    lista_bolas[15].itemconfig(1, fill="black")

                if bolas_resultado3[1] in set(sorteada) and bolas_resultado3[1] == sorteada[1]:
                    lista_bolas[35].itemconfig(1, fill="black")

                if bolas_resultado3[2] in set(sorteada) and bolas_resultado3[2] == sorteada[2]:
                    lista_bolas[34].itemconfig(1, fill="black")

                if bolas_resultado3[3] in set(sorteada) and bolas_resultado3[3] == sorteada[3]:
                    lista_bolas[14].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado4) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado4[0] in set(sorteada) and bolas_resultado4[0] != sorteada[0]:
                    lista_bolas[13].itemconfig(1, fill="white")

                if bolas_resultado4[1] in set(sorteada) and bolas_resultado4[1] != sorteada[1]:
                    lista_bolas[33].itemconfig(1, fill="white")

                if bolas_resultado4[2] in set(sorteada) and bolas_resultado4[2] != sorteada[2]:
                    lista_bolas[32].itemconfig(1, fill="white")

                if bolas_resultado4[3] in set(sorteada) and bolas_resultado4[3] != sorteada[3]:
                    lista_bolas[12].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada                
                if bolas_resultado4[0] in set(sorteada) and bolas_resultado4[0] == sorteada[0]:
                    lista_bolas[13].itemconfig(1, fill="black")

                if bolas_resultado4[1] in set(sorteada) and bolas_resultado4[1] == sorteada[1]:
                    lista_bolas[33].itemconfig(1, fill="black")

                if bolas_resultado4[2] in set(sorteada) and bolas_resultado4[2] == sorteada[2]:
                    lista_bolas[32].itemconfig(1, fill="black")

                if bolas_resultado4[3] in set(sorteada) and bolas_resultado4[3] == sorteada[3]:
                    lista_bolas[12].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado5) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado5[0] in set(sorteada) and bolas_resultado5[0] != sorteada[0]:
                    lista_bolas[11].itemconfig(1, fill="white")

                if bolas_resultado5[1] in set(sorteada) and bolas_resultado5[1] != sorteada[1]:
                    lista_bolas[31].itemconfig(1, fill="white")

                if bolas_resultado5[2] in set(sorteada) and bolas_resultado5[2] != sorteada[2]:
                    lista_bolas[30].itemconfig(1, fill="white")

                if bolas_resultado5[3] in set(sorteada) and bolas_resultado5[3] != sorteada[3]:
                    lista_bolas[10].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada   
                if bolas_resultado5[0] in set(sorteada) and bolas_resultado5[0] == sorteada[0]:
                    lista_bolas[11].itemconfig(1, fill="black")

                if bolas_resultado5[1] in set(sorteada) and bolas_resultado5[1] == sorteada[1]:
                    lista_bolas[31].itemconfig(1, fill="black")

                if bolas_resultado5[2] in set(sorteada) and bolas_resultado5[2] == sorteada[2]:
                    lista_bolas[30].itemconfig(1, fill="black")

                if bolas_resultado5[3] in set(sorteada) and bolas_resultado5[3] == sorteada[3]:
                    lista_bolas[10].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado6) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado6[0] in set(sorteada) and bolas_resultado6[0] != sorteada[0]:
                    lista_bolas[9].itemconfig(1, fill="white")

                if bolas_resultado6[1] in set(sorteada) and bolas_resultado6[1] != sorteada[1]:
                    lista_bolas[29].itemconfig(1, fill="white")

                if bolas_resultado6[2] in set(sorteada) and bolas_resultado6[2] != sorteada[2]:
                    lista_bolas[28].itemconfig(1, fill="white")

                if bolas_resultado6[3] in set(sorteada) and bolas_resultado6[3] != sorteada[3]:
                    lista_bolas[8].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado6[0] in set(sorteada) and bolas_resultado6[0] == sorteada[0]:
                    lista_bolas[9].itemconfig(1, fill="black")

                if bolas_resultado6[1] in set(sorteada) and bolas_resultado6[1] == sorteada[1]:
                    lista_bolas[29].itemconfig(1, fill="black")

                if bolas_resultado6[2] in set(sorteada) and bolas_resultado6[2] == sorteada[2]:
                    lista_bolas[28].itemconfig(1, fill="black")

                if bolas_resultado6[3] in set(sorteada) and bolas_resultado6[3] == sorteada[3]:
                    lista_bolas[8].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado7) == 4:

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado7[0] in set(sorteada) and bolas_resultado7[0] != sorteada[0]:
                    lista_bolas[7].itemconfig(1, fill="white")

                if bolas_resultado7[1] in set(sorteada) and bolas_resultado7[1] != sorteada[1]:
                    lista_bolas[27].itemconfig(1, fill="white")

                if bolas_resultado7[2] in set(sorteada) and bolas_resultado7[2] != sorteada[2]:
                    lista_bolas[26].itemconfig(1, fill="white")

                if bolas_resultado7[3] in set(sorteada) and bolas_resultado7[3] != sorteada[3]:
                    lista_bolas[6].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado7[0] in set(sorteada) and bolas_resultado7[0] == sorteada[0]:
                    lista_bolas[7].itemconfig(1, fill="black")

                if bolas_resultado7[1] in set(sorteada) and bolas_resultado7[1] == sorteada[1]:
                    lista_bolas[27].itemconfig(1, fill="black")

                if bolas_resultado7[2] in set(sorteada) and bolas_resultado7[2] == sorteada[2]:
                    lista_bolas[26].itemconfig(1, fill="black")

                if bolas_resultado7[3] in set(sorteada) and bolas_resultado7[3] == sorteada[3]:
                    lista_bolas[6].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado8) == 4:
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado8[0] in set(sorteada) and bolas_resultado8[0] != sorteada[0]:
                    lista_bolas[5].itemconfig(1, fill="white")
                
                if bolas_resultado8[1] in set(sorteada) and bolas_resultado8[1] != sorteada[1]:
                    lista_bolas[25].itemconfig(1, fill="white")
                
                if bolas_resultado8[2] in set(sorteada) and bolas_resultado8[2] != sorteada[2]:
                    lista_bolas[24].itemconfig(1, fill="white")
                
                if bolas_resultado8[3] in set(sorteada) and bolas_resultado8[3] != sorteada[3]:
                    lista_bolas[4].itemconfig(1, fill="white")
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado8[0] in set(sorteada) and bolas_resultado8[0] == sorteada[0]:
                    lista_bolas[5].itemconfig(1, fill="black")
                
                if bolas_resultado8[1] in set(sorteada) and bolas_resultado8[1] == sorteada[1]:
                    lista_bolas[25].itemconfig(1, fill="black")
                
                if bolas_resultado8[2] in set(sorteada) and bolas_resultado8[2] == sorteada[2]:
                    lista_bolas[24].itemconfig(1, fill="black")
                
                if bolas_resultado8[3] in set(sorteada) and bolas_resultado8[3] == sorteada[3]:
                    lista_bolas[4].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista
            if len(bolas_resultado9) == 4:
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado9[0] in set(sorteada) and bolas_resultado9[0] != sorteada[0]:
                    lista_bolas[3].itemconfig(1, fill="white")

                if bolas_resultado9[1] in set(sorteada) and bolas_resultado9[1] != sorteada[1]:
                    lista_bolas[23].itemconfig(1, fill="white")

                if bolas_resultado9[2] in set(sorteada) and bolas_resultado9[2] != sorteada[2]:
                    lista_bolas[22].itemconfig(1, fill="white")

                if bolas_resultado9[3] in set(sorteada) and bolas_resultado9[3] != sorteada[3]:
                    lista_bolas[2].itemconfig(1, fill="white")

                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado9[0] in set(sorteada) and bolas_resultado9[0] == sorteada[0]:
                    lista_bolas[3].itemconfig(1, fill="black")

                if bolas_resultado9[1] in set(sorteada) and bolas_resultado9[1] == sorteada[1]:
                    lista_bolas[23].itemconfig(1, fill="black")

                if bolas_resultado9[2] in set(sorteada) and bolas_resultado9[2] == sorteada[2]:
                    lista_bolas[22].itemconfig(1, fill="black")

                if bolas_resultado9[3] in set(sorteada) and bolas_resultado9[3] == sorteada[3]:
                    lista_bolas[2].itemconfig(1, fill="black")


            # Condicional que avalia se há quatro cores na lista   
            if len(bolas_resultado10) == 4:
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado10[0] in set(sorteada) and bolas_resultado10[0] != sorteada[0]:
                    lista_bolas[1].itemconfig(1, fill="white")
                
                if bolas_resultado10[1] in set(sorteada) and bolas_resultado10[1] != sorteada[1]:
                    lista_bolas[21].itemconfig(1, fill="white")
                
                if bolas_resultado10[2] in set(sorteada) and bolas_resultado10[2] != sorteada[2]:
                    lista_bolas[20].itemconfig(1, fill="white")
                
                if bolas_resultado10[3] in set(sorteada) and bolas_resultado10[3] != sorteada[3]:
                    lista_bolas[0].itemconfig(1, fill="white")
                
                # Condicionais que avaliam se os itens da lista estão condigentes com os itens da lista de cores sorteada
                if bolas_resultado10[0] in set(sorteada) and bolas_resultado10[0] == sorteada[0]:
                    lista_bolas[1].itemconfig(1, fill="black")
                
                if bolas_resultado10[1] in set(sorteada) and bolas_resultado10[1] == sorteada[1]:
                    lista_bolas[21].itemconfig(1, fill="black")
                
                if bolas_resultado10[2] in set(sorteada) and bolas_resultado10[2] == sorteada[2]:
                    lista_bolas[20].itemconfig(1, fill="black")
                
                if bolas_resultado10[3] in set(sorteada) and bolas_resultado10[3] == sorteada[3]:
                    lista_bolas[0].itemconfig(1, fill="black")


                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado[0] != sorteada[0] or bolas_resultado[1] != sorteada[1] or bolas_resultado[2] != sorteada[2] or bolas_resultado[3] != sorteada[3]:
                    # Limpa lista
                    bolas_resultado.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado2[0] != sorteada[0] or bolas_resultado2[1] != sorteada[1] or bolas_resultado2[2] != sorteada[2] or bolas_resultado2[3] != sorteada[3]:
                    # Limpa lista
                    bolas_resultado2.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado3[0] != sorteada[0] or bolas_resultado3[1] != sorteada[1] or bolas_resultado3[2] != sorteada[2] or bolas_resultado3[3] != sorteada[3]:   
                    # Limpa lista
                    bolas_resultado3.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado4[0] != sorteada[0] or bolas_resultado4[1] != sorteada[1] or bolas_resultado4[2] != sorteada[2] or bolas_resultado4[3] != sorteada[3]:      
                    # Limpa lista
                    bolas_resultado4.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado5[0] != sorteada[0] or bolas_resultado5[1] != sorteada[1] or bolas_resultado5[2] != sorteada[2] or bolas_resultado5[3] != sorteada[3]:   
                    # Limpa lista
                    bolas_resultado5.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado6[0] != sorteada[0] or bolas_resultado6[1] != sorteada[1] or bolas_resultado6[2] != sorteada[2] or bolas_resultado6[3] != sorteada[3]:      
                    # Limpa lista
                    bolas_resultado6.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado7[0] != sorteada[0] or bolas_resultado7[1] != sorteada[1] or bolas_resultado7[2] != sorteada[2] or bolas_resultado7[3] != sorteada[3]:      
                    # Limpa lista
                    bolas_resultado7.clear()
                    
                 # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado8[0] != sorteada[0] or bolas_resultado8[1] != sorteada[1] or bolas_resultado8[2] != sorteada[2] or bolas_resultado8[3] != sorteada[3]:     
                    # Limpa lista
                    bolas_resultado8.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições
                if bolas_resultado9[0] != sorteada[0] or bolas_resultado9[1] != sorteada[1] or bolas_resultado9[2] != sorteada[2] or bolas_resultado9[3] != sorteada[3]:    
                    # Limpa lista
                    bolas_resultado.clear()
                    
                # Condicional que avalia se o botão clicado pelo usuário é diferente das cores sorteadas nas suas respecitivas posições, limpa lista, cria botão de reiniciar, desabilita botões, declara derrota e mostra o resultado certo na tela
                if bolas_resultado10[0] != sorteada[0] or bolas_resultado10[1] != sorteada[1] or bolas_resultado10[2] != sorteada[2] or bolas_resultado10[3] != sorteada[3]:
                        
                    bolas_resultado10.clear()
                    criar_botao_reiniciar()
                    desabilitar_botao()
                    mostrar_derrota()  
                    esconder.place_forget()

            
            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolas_resultado) == 4 and bolas_resultado[0] == sorteada[0] and bolas_resultado[1] == sorteada[1] and bolas_resultado[2] == sorteada[2] and bolas_resultado[3] == sorteada[3]:
                # Parâmentro teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado.clear()
                esconder.place_forget()
            
            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolas_resultado2) == 4 and bolas_resultado2[0] == sorteada[0] and bolas_resultado2[1] == sorteada[1] and bolas_resultado2[2] == sorteada[2] and bolas_resultado2[3] == sorteada[3]:
                # Parâmetro de teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado2.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolas_resultado3) == 4 and bolas_resultado3[0] == sorteada[0] and bolas_resultado3[1] == sorteada[1] and bolas_resultado3[2] == sorteada[2] and bolas_resultado3[3] == sorteada[3]:
                # Parâmetro de teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado3.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolas_resultado4) == 4 and bolas_resultado4[0] == sorteada[0] and bolas_resultado4[1] == sorteada[1] and bolas_resultado4[2] == sorteada[2] and bolas_resultado4[3] == sorteada[3]:
                # Parâmetro de teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado4.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolas_resultado5) == 4 and bolas_resultado5[0] == sorteada[0] and bolas_resultado5[1] == sorteada[1] and bolas_resultado5[2] == sorteada[2] and bolas_resultado5[3] == sorteada[3]:
                # Parâmetro de teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado5.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada
            if len(bolas_resultado6) == 4 and bolas_resultado6[0] == sorteada[0] and bolas_resultado6[1] == sorteada[1] and bolas_resultado6[2] == sorteada[2] and bolas_resultado6[3] == sorteada[3]:
                # Parâmetro de teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado6.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada           
            if len(bolas_resultado7) == 4 and bolas_resultado7[0] == sorteada[0] and bolas_resultado7[1] == sorteada[1] and bolas_resultado7[2] == sorteada[2] and bolas_resultado7[3] == sorteada[3]:
                # Parâmetro teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado7.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada           
            if len(bolas_resultado8) == 4 and bolas_resultado8[0] == sorteada[0] and bolas_resultado8[1] == sorteada[1] and bolas_resultado8[2] == sorteada[2] and bolas_resultado8[3] == sorteada[3]:
                # Parâmetro teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado8.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada           
            if len(bolas_resultado9) == 4 and bolas_resultado9[0] == sorteada[0] and bolas_resultado9[1] == sorteada[1] and bolas_resultado9[2] == sorteada[2] and bolas_resultado9[3] == sorteada[3]:
                # Parâmetro teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado9.clear()
                esconder.place_forget()

            # Se a lista dos botões clicados pelo usuário for igual a lista de cores aleatórias, a condicional será executada           
            if len(bolas_resultado10) == 4 and bolas_resultado10[0] == sorteada[0] and bolas_resultado10[1] == sorteada[1] and bolas_resultado10[2] == sorteada[2] and bolas_resultado10[3] == sorteada[3]:
                # Parâmetro teste
                mostrar_triunfo()
                desabilitar_botao()
                criar_botao_reiniciar()
                # Verifica a lista
                bolas_resultado10.clear()
                esconder.place_forget()   
            

            # Se a condicional acima não for satisfeita, o código abaixo é chamado
            else:
                # Agenda a execução da função novamente a cada 100 milissegundos
                tela.after(1000, verificar_lista)



        # Função para mudar a cor
        def mudar_cor(cor):  
            # Estrutura de repetição que vai ler e ordenar tudo que esta na lista de bolasSemPreencher
            for inteiros_divisiveis, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número divísivel por 10 for inteiro
                if inteiros_divisiveis % 10 == 0:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()

                        # Retorna para o começo para esperar a próxima ação
                        return     

            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 1  or bolas_especificas == 11 or bolas_especificas == 21 or bolas_especificas == 31:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado2.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return
                    
            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 2  or bolas_especificas == 12 or bolas_especificas == 22 or bolas_especificas == 32:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado3.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return
                    
            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 3  or bolas_especificas == 13 or bolas_especificas == 23 or bolas_especificas == 33:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado4.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 

            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 4  or bolas_especificas == 14 or bolas_especificas == 24 or bolas_especificas == 34:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado5.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return
                    
            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 5  or bolas_especificas == 15 or bolas_especificas == 25 or bolas_especificas == 35:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado6.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 

            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 6  or bolas_especificas == 16 or bolas_especificas == 26 or bolas_especificas == 36:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado7.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 
                    
            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 7  or bolas_especificas == 17 or bolas_especificas == 27 or bolas_especificas == 37:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado8.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 


            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 8  or bolas_especificas == 18 or bolas_especificas == 28 or bolas_especificas == 38:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado9.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return 

            for bolas_especificas, bola in enumerate(bolas_sem_preencher):
                # Condicional que só muda de cor se o número for igual aos propostos
                if bolas_especificas == 9  or bolas_especificas == 19 or bolas_especificas == 29 or bolas_especificas == 39:
                    # Obtém a cor atual de qualquer uma das bolas
                    cor_atual = bola.itemcget(1, "fill")
                    # Se a cor atual for igual a branco, ele executará a condicional a baixo
                    if cor_atual == "white":
                        # Muda a cor para a cor que o usuário selecionou
                        bola.itemconfig(1, fill=cor)
                        # Acrescenta as cores na lista
                        bolas_resultado10.append(cor)
                        # Verifica a lista de escolhas                       
                        verificar_lista()
                        # Retorna para o começo para esperar a próxima ação             
                        return
   

        # Criar botões com certas características específicas
        botao_roxo = tk.Button(tela, command=lambda: (mudar_cor("purple")), bg="purple", fg= "white")

        # Determina o lugar através de coordenadas
        botao_roxo.place(x=462, y=600)

        # Criar botões com certas características específicas
        botao_azul = tk.Button(tela, command=lambda: (mudar_cor("blue")), bg="blue", fg= "white")
        # Determina o lugar através de coordenada
        botao_azul.place(x=544, y=600)

        # Criar botões com certas características específicas
        botao_verde = tk.Button(tela, command=lambda: (mudar_cor("green")), bg="green", fg= "white")
        # Determina o lugar através de coordenada
        botao_verde.place(x=626, y=600)

        # Criar botões com certas características específicas
        botao_amarelo = tk.Button(tela, command=lambda: (mudar_cor("orange")), bg="orange", fg= "white")
        # Determina o lugar através de coordenada
        botao_amarelo.place(x=708, y=600)

        # Criar botões com certas características específicas
        botao_vermelho = tk.Button(tela, command=lambda: (mudar_cor("red")), bg="red", fg= "white")
        # Determina o lugar através de coordenada
        botao_vermelho.place(x=790, y=600)

        # Criar botões com certas características específicas
        botao_marrom = tk.Button(tela, command=lambda: (mudar_cor("brown")), bg="brown", fg="white")
        # Determina o lugar através de coordenada
        botao_marrom.place(x=872, y=600)

        # Legenda para o título do jogo
        titulo = tk.Label(tela, text="JOGO DA SENHA", bg = "white", fg = "black", font = ("Times_New_Roman", 18))
        # Posiciona o título na tela
        titulo.place(x = 580, y = 30)

        # Instrução para sair da tela
        instrucao = tk.Label(tela, text="Pressione 'ESC', para sair do jogo", bg = "white", fg = "black", font = ("Times_New_Roman", 10))
        # Posiciona a instrução na tela
        instrucao.place(x = 570)

        # contador
        a = 0
        
        # Mostra todas as cooordenadas de y
        posicoes_y = [97, 112, 140, 155, 187, 202, 235, 250, 281, 296, 329, 344, 376, 391, 424, 439, 471, 486, 515, 530]

        # Lista vazia para armazenar as bolas que irão indicar se o usuário está no caminho certo
        lista_bolas = []

        # Estrutura de repetição para criação de bolas
        for _ in range(0,2):
            # Soma 40 ao contador
            a += 24
            # Estrutura de repetição que posiciona cada bola no seu devido lugar
            for y in posicoes_y:
                # Cria o fundo das bolas
                canvas_acertos = tk.Canvas(tela, width=16.8, height=16.8, highlightthickness=0)
                # Cria as bolas
                canvas_acertos.create_oval(0, 0, 15, 15, fill="grey", outline="grey")
                # Configura a cor para cinza
                canvas_acertos.configure(bg="grey")
                # Define as posições variáveis
                canvas_acertos.place(x=525 + a, y=y)
                # Acrescentas as bolas em uma lista vazia para facilitar a chamada 
                lista_bolas.append(canvas_acertos)


# Cria o canvas dentro da janela principal e o deixa com as bordas transparentes
canvas_jogo = tk.Canvas(tela, width=1000, height=1000, highlightthickness=0)

# Desenha um quadrado ou rentângulo
retangulo = canvas_jogo.create_rectangle(30, 30, 330, 510, fill="black", outline="blue", width=15)

# Configura o fundo do elemento canva para branco
canvas_jogo.configure(bg="white")

# Determina o lugar através de coordenadas
canvas_jogo.place(x=0, y=50)


# Chamar a função move_right() após um atraso de 10 mílisegundo
canvas_jogo.after(10, mover_direita)



# Vincula o botão "ESC" a função fechar tela
tela.bind("<Escape>", fecha_tela)

# Mantêm a tela aberta e operando para sempre verificar quaisquer movomentações dentro dela
tela.mainloop()

