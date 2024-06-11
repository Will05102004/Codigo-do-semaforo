import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

contador = 0

#Setup dos semaforos de carro
GPIO.setup(2,  GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


#Setup dos semaforos de pedestre
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)


#Função para deixar os semaforos principais verdes
def verdes():
    #semaforos pedestres
    GPIO.output(8, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    #semaforos principais
    GPIO.output(4, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)

#Função para deixar os semaforos principais amarelos
def amarelos1():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    
def amarelo2():
    GPIO.output(9, GPIO.HIGH)
  

#Função para deixar os semaforos principais verdes
def vermelhos():
    #semaforos pedestres
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    #semaforos principais
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    
def temporizador():
  contador = 0
  
  while contador < 3:
    time.sleep(1)
    print("Aguarde")
    contador += 1
  print("Pode pressionar")
    
    
#Função para vefificar se o botão de pedestre foi apertado
def botao():
  #Setup do botão 1
  btn1 = 5
  GPIO.setup(btn1, GPIO.IN, GPIO.PUD_DOWN)
  
  temporizador()
    
  for i in range(50):
    #Se for apertado, para com o loop e continua o código
    if GPIO.input(btn1)== GPIO.HIGH:
      time.sleep(1)
      return
    #Se não, faz uma pausa e roda novamente
    else:
        time.sleep(0.1)

#Função para vefificar se o botão de pedestre foi apertado
def botao2():
  #Setup do botão 2
  btn2 = 6
  GPIO.setup(btn2, GPIO.IN, GPIO.PUD_DOWN)
  
  temporizador()
    
  for i in range(50):
    #Se for apertado, para com o loop e continua o código
    if GPIO.input(btn2)== GPIO.HIGH:
      time.sleep(1)
      return
    #Se não, faz uma pausa e roda novamente
    else:
        time.sleep(0.1)
        
        
#Função principal com todas outras
def main():
  for i in range(10):
    verdes()
    botao()
    amarelos1()
    time.sleep(1)
    vermelhos()
    botao2()
    amarelo2()
    time.sleep(1)

main()