from algo1 import *

class BinaryTree:
    root=None
class BinaryTreeNode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None
"-----------------------------------------------"
def insert(B,element,key): #Funciona el Insert
  NodeNew=BinaryTreeNode()
  NodeNew.value=element
  NodeNew.key=key
  
  if B.root==None:
    B.root=NodeNew
  
  Node=B.root
  insert_Recursivo(NodeNew,Node)

def insert_Recursivo(NodeNew,Node): #Funcion que coloca el nodo nuevo en el Arbol
  if NodeNew.key != Node.key:
    if NodeNew.key>Node.key:
      if Node.rightnode==None:
        Node.rightnode=NodeNew 
        NodeNew.parent=Node #Le agrego el padre a el nuevo nodo(Se puede utilizar para la busqueda)
      else:
        insert_Recursivo(NodeNew,Node.rightnode)
    else:
      if Node.leftnode==None:
        Node.leftnode=NodeNew
        NodeNew.parent=Node
      else:
        insert_Recursivo(NodeNew,Node.leftnode)

"-----------------------------------------------"
def search(B,element):#Retorna la Key del elemento_En otro caso None
  if B.root!=None: #Arbol con almenos 1 hijo
    return(buscador(B.root,element))
  return(None)

def buscador(node,element):
  
  
  if node.value == element:
    return(node.key)
  else:
    
    key_encontrada = None #La definimos
    
    if node.leftnode!=None:
      key_encontrada = buscador(node.leftnode,element)

    if node.rightnode!=None and key_encontrada == None:
      key_encontrada = buscador(node.rightnode,element)
    
    return(key_encontrada)

#-----------------------------------------------------------
def deleteKey(B,key):#Elimica un nodo mediante la Key
  deleteKeyRecursivo(B,B.root,key)
  
def deleteKeyRecursivo(Arbol,Nodo_act,key_borrar): #Retorna Nodo eliminado
  
  if Nodo_act.key == key_borrar:
    
    if Nodo_act.rightnode != None: #Buscamos al menor de los mayores
      Nodo_Cambio = Nodo_de_Menor_key(Nodo_act.rightnode)
    elif Nodo_act.leftnode != None: #Si no hay menor de mayores sera el mayor de menores
      Nodo_Cambio = Nodo_de_Mayor_key(Nodo_act.leftnode)
    else: #Nodo actual a borrar no tiene hijos por lo que lo borramos y retornamos Nodo

      if Nodo_act.parent == None: #Quiere borrar a la raiz del arbol
        Arbol.root == None 

      else: #No se trata del Nodo raiz

        Nodo_Padre_act = Nodo_act.parent
        
        if Nodo_Padre_act.leftnode == Nodo_act:
          Nodo_Padre_act.leftnode = None
        else:
          Nodo_Padre_act.rightnode = None
        
        Nodo_act.parent = None #Limpiamos la referencia al Nodo padre

        return(Nodo_act)      

    if Nodo_Cambio.leftnode != None or Nodo_Cambio.rightnode != None: #Nodo Cambio puede tener nodos hijos, alguien ocupa lugar de Nodo Cambio
      #Repetimos proceso pero para Nodo_Cambio deleteKeyRecursivo(Nodo_Cambio) 
      Nodo_Cambio = deleteKeyRecursivo(Arbol,Nodo_Cambio,Nodo_Cambio.key)

    #En este punto Nodo_Cambio ya puede usarce sin problemas
    #Nodo cambio o no tiene hijos o ya fue reemplazado por otro nodo 

    if Nodo_act.leftnode == Nodo_Cambio: #Por si apunta al nodo que cambia, sino se genera un puntero a si mismo
      Nodo_act.leftnode = None
    elif Nodo_act.rightnode == Nodo_Cambio:
      Nodo_act.rightnode = None

    Nodo_Padre_Cambio = Nodo_Cambio.parent
    if Nodo_Padre_Cambio!= None: #Sacamos toda existencia de Nodo Cambio del arbol, sera reimplantado
      if Nodo_Padre_Cambio.leftnode == Nodo_Cambio:
        Nodo_Padre_Cambio.leftnode = None
      else:
        Nodo_Padre_Cambio.rightnode = None

    Nodo_Cambio.leftnode = Nodo_act.leftnode #Asignamos hijos de Nodo actual al Nodo Cambio
    Nodo_Cambio.rightnode = Nodo_act.rightnode
    Nodo_Cambio.parent = Nodo_act.parent
    
    if Nodo_Cambio.leftnode != None: #Reasignamos los padres correspondientes a cada nodo hijo de padre reemplazado
      Nodo_Cambio.leftnode.parent = Nodo_Cambio
    if Nodo_Cambio.rightnode != None: 
      Nodo_Cambio.rightnode.parent = Nodo_Cambio 
     
    Nodo_Padre_act = Nodo_act.parent #  El padre de el Nodo actual apuntara al Nodo Cambio
    if Nodo_Padre_act ==  None:
      Arbol.root = Nodo_Cambio
    else:
      if Nodo_Padre_act.leftnode == Nodo_act:
        Nodo_Padre_act.leftnode = Nodo_Cambio
      else:
        Nodo_Padre_act.rightnode = Nodo_Cambio
    
    Nodo_act.parent = None #Limpiamos la referencia al Nodo actual
    Nodo_act.leftnode = None
    Nodo_act.rightnode = None

    return(Nodo_act) #Retornamos Nodo actual borrado del arbol

  else: #Buscamos el Nodo a eliminar
    if Nodo_act.key > key_borrar and Nodo_act.leftnode!= None : #Nos vamos a la derecha(menor)
      return( deleteKeyRecursivo(Arbol,Nodo_act.leftnode,key_borrar) )
    elif Nodo_act.rightnode!= None: #La key es mayor(izquierda)
      return( deleteKeyRecursivo(Arbol,Nodo_act.rightnode,key_borrar) )

def Nodo_de_Menor_key(Nodo): #Retorna el Nodo de menor valor de key
  if Nodo.leftnode == None:
    return(Nodo) #Retornamos el puntero
  return( Nodo_de_Menor_key(Nodo.leftnode) )

def Nodo_de_Mayor_key(Nodo): #Retorna el Nodo de mayor valor de key
  if Nodo.rightnode == None:
    return(Nodo) #Retornamos el puntero
  return( Nodo_de_Mayor_key(Nodo.rightnode) )

#---------------------------------------------------
def access(B,key):#Accede a un elemento mediante la Key
  if B.root!=None:
    return(access_Recursivo(B.root,key))
    
def access_Recursivo(nodo,key):    
  if node.key==key:
    return(node.value)
  else:
    Retorno = None
    if node.key > key and node.leftnode != None :
      Retorno = access_Recursivo(node.leftnode,key)
    elif node.key < key and node.rightnode!=None :
      Retorno = access_Recursivo(node.rightnode,key)
    return(Retorno)
  
#-------------------------------------------
def update(B,element,key):#Accede a un nodo mediante su key y cambia su valor
  if B.root!=None:
    return(UpdateBusqueda(B.root,element,key))
  return(False)
def UpdateBusqueda(node,element,key):
  if node.key == key:
    node.value = element
    return (True)
  else:
    if node.key>key and node.leftnode!=None:
      return( UpdateBusqueda(node.leftnode,element,key) )
    elif node.key<key and node.rightnode != None:
      return( UpdateBusqueda(node.rightnode,element,key) )
  return(False)

#-----------------------------------------------------------
def Lista_Padres(Arbol_B):
    #Retorna una lista en donde cada casillero corresponde a los nodos de un nivel del arbol
    #[ 1 ] [0 , 4] [ -1 , 2 , 5 ]
    lista = []
    if Arbol_B.root != None:
        Lista_Padres_Recursivo(Arbol_B.root,lista,0)    
    return (lista)

def Lista_Padres_Recursivo(Nodo,ListaPadres,contador):
    #El contador nos ayuda a ingresar al nivel indicado

    if ListaPadres == [] or len(ListaPadres) <= contador: #Puede que la lista ya este generada
      Lista = [] #Generamos una nueva lista que contendra a los nodos de el mismo nivel 
      ListaPadres.append(Lista)

    ListaPadres[contador].append(Nodo.value)
    if Nodo.leftnode != None:
        print(Nodo.leftnode.key)
        Lista_Padres_Recursivo(Nodo.leftnode,ListaPadres,contador+1)
    if Nodo.rightnode != None:
        print(Nodo.rightnode.key)
        Lista_Padres_Recursivo(Nodo.rightnode,ListaPadres,contador+1)
#-----------------------------------------------------------       
def Ver_Arbol(Arbol_B):
  print(Lista_Padres(Arbol_B))
#-----------------------------------------------------------

