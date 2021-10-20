import cv2
"""
ALUNO: WANDERSON PAULINO BATISTA - 475663

TRABALAHO ESCOLHIDO: GIF ANIMADO

ESCOLHI A LISTA CIRCULAR, COMO O COMANDO DO TRABALHO QUE ESCOLHI
REQUERIA UM LOOP, A LISTA CIRCULAR FOI A QUE MELHOR SE ENCAIXOU
NESSE ESQUEMA DE LOOP(POIS O ÚLTIMO ELEMENTO APONTA PARA O PRIMEIRO), 
USEI A BIBLIOTECA OPENCV PARA O PROCESSAMENTO DAS IMAGENS.

TUTORIAL:
    1- RODE O CÓDIGO;
    2- INFORME O TEMPO;
    3- TECLE ESPAÇO PARA RODAR O GIF;
OBS.: TEM UM BUG QUE NÃO CONSEGUI RESOLVER, TEM QUE CLICAR MAIS DE
UMA VEZ NO 'X' PARA FECHAR A APLICAÇÃO.
"""
    
class Node:    
  def __init__(self,data):    
    self.data = data    
    self.next = None    
     
class CreateList:     
  def __init__(self):    
    self.head = Node(None)    
    self.tail = Node(None)    
    self.head.next = self.tail   
    self.tail.next = self.head   
        
    
  def add(self,data):    
    newNode = Node(data)     
    if self.head.data is None:      
      self.head = newNode   
      self.tail = newNode   
      newNode.next = self.head   
    else:       
      self.tail.next = newNode      
      self.tail = newNode    
      self.tail.next = self.head   
    
  
  def display(self,tempo):    
    current = self.head
    
    if self.head is None:    
      print("List is empty")    
      return 
   
    else:    
        cv2.imshow("GIF ANIMADO",current.data)
        cv2.waitKey(0)
        cv2.destroyWindow("GIF ANIMADO")
       
        while(current.next != self.head): 
            while True:
                current = current.next;
                cv2.namedWindow("GIF ANIMADO", cv2.WINDOW_KEEPRATIO)
                cv2.imshow("GIF ANIMADO", current.data)
                cv2.waitKey(tempo)
                if cv2.getWindowProperty('GIF ANIMADO', 1) < 0:
                   cv2.destroyAllWindows("GIF ANIMADO")
                   break
 

                    
                
                
                
cl = CreateList();

for i in range(23):
    cl.add(cv2.imread("{}.jpeg".format(i), cv2.IMREAD_ANYCOLOR))
print("Informe a quantidade de tempo (em milisegundos) de cada frame:")
w = int(input())
cl.display(w)
print("FINISH!")
