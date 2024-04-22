
import time
import random



#PREGUNTAS
#ADSO

q1 = "Cuanto tiempo (meses) dura nuestro programa academico ADSO? "

q2 = "Cuando dura la etapa lectiva?"

q3 = "Debo asistir a la empresa durante mi etapa lectiva asi tenga un patrocinio?\n(verdadero o falso)"

q4 = "Existen otras alternativas   parte del contrato de aprendizaje para mi etapa productiva? \n(verdadero o falso)"

#Matematicas

q5 = "Los años luz son unidad de tiempo o de distancia?: \n(verdadero o falso)"

q6 = "Toda funcion derivable en un intervalo cerrado es continua?: \n(verdadero o falso)"

q7 = "Sea f una funcion continua e inyectiva, entonces tiene algun punto de inflexion ?: \n(verdadero o falso)"

q8 = "sea F(a) un punto de una funcion continua y suave, es F''(a) la pendiente de la recta tangente de la derivada de F(a)?: \n(verdadero o falso)"

#SENA

q9 = "Con que cantfidad de dinero soy apoyado si me postulo al centro de desarrollo empresarial con el fondo emprender?"

q10 = "Que significa SENNOVA?"

q11 = "Puede cualquier persona puede acceder a la agencia publica de emples del sena?: \n(verdadero o falso)"

q12 = "Cuantos cursos de ingles se ofrecen en el sena?: "

#APO

q13 = "Es Python un lenguaje compilado o interpretado?: "

q14 = "Puede una funcion en python retornar un valor que no sea numerico?: \n(verdadero o falso)"

q15 = "Cuantos caracteres diferentes se pueden hacer con 8 bits?: "

q16 = "El nombre " "juan", "cuantos bits podemos decir que pesa en programacion?: "

#rESPUESTAS

r1 = "27 meses"
r2 = "falso"
r3 = "falso"
r4 = "verdadero"

r5 = "distancia"
r6 = "verdadero"
r7 = "verdadero"
r8 = "verdadero"

r9 = "100 millones"
r10 = "sistema de investigacion desarrollo tecnologico e innovacion"
r11 = "verdadero"
r12 = "13"

r13 = "interpretado"
r14 = "verdadero"
r15 = "256"
r16 =  "32"

#COLORES
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
NEGRILLA = '\033[1m'
END = '\033[0m'

print(CYAN+"■"*40+NEGRILLA+(BLUE+" BIENVENIDOS AL  ")+CYAN+"■"*40)
print(CYAN+"■"*35+NEGRILLA+(BLUE+" PIEDRA, PAPEL Y TIJERA   ")+CYAN+"■"*36)
print(CYAN+"■"*41+NEGRILLA+(BLUE+" DE LA INDUCCION   ")+CYAN+"■"*41)

print(END)

#Catálogo
A = "ADSO"
F = "Matematicas"
C = "SENA"
P = "Programacion"
a = "ADSO"
f = "Matematicas"
c = "SENA"
p = "Programacion"

print(GREEN + NEGRILLA)
print(f"a = ADSO\nf = Matematicas\nc = SENA\np = Programacion\n\n\t")
print(END)
print("\t"+(" ▄")+("■"*55)+("▄"))
print("\t"+NEGRILLA+"█   Presione la inicial del tema que desea repasar  █")
print("\t"+(" ▀")+("■"*55)+("▀")+"\n")

print(END)
 
#cantidad de materias
kMaterias = int(input("Cuantos temas le gustaria estudiar: "))
while   kMaterias >5 or 1 > kMaterias:
  print(f".")
  time.sleep(1)
  print(f".")
  time.sleep(1)
  print(f".")
  time.sleep(1)
  print("Valor invalido, DIGITE NUEVAMENTE\n")
  time.sleep(1)
  kMaterias = int(input("Cuantos temas le gustaria estudiar: "))
else:
  print("\n")  

acum = ""
for i in range(kMaterias):
  m = input(f"Escriba  el tema {i+1} que desea estudiar: ")
  acum = acum + m


print("\n\t\t\tJUEGO\n\n\n")

#El JUEGO (explicacion)

print("NOTA:\nUsted jugara contra la maquina"+ NEGRILLA+(" 3 ")+END+"rounds de"+ NEGRILLA+(" piedra, papel o tijera ")+END)
time.sleep(2)
print("debera ganar  "+ NEGRILLA+("3 veces ")+END+"para ganar completamente el juego")
time.sleep(2)
print("Para ello contara con "+ NEGRILLA+("1 vida ")+END+"la cual aparecera en la parte superior de esta manera: "+ NEGRILLA+ RED+("♥")+END)
time.sleep(2)
print("Si gana el round: "+ NEGRILLA+BLUE+("ENHORABUENA!!! ")+END+"el juego continua, hasta terminarlo, de lo contrario...")
time.sleep(2)
print("TRANQUILO! "+ NEGRILLA+("NO ")+END+"perdera su vida, pero si  tendra que jugarsela "+ NEGRILLA+ RED+("♥ ")+END+" en ")
time.sleep(2)
print(NEGRILLA+RED+"EL GULAG  "+ END)
time.sleep(2)
print("Responde correctamente y el juego continuara, falla "+ NEGRILLA+("1 vez "+RED+" ♥ ")+END+"y estaras fuera\n")
time.sleep(2)



O = "piedra"
D = "papel"
X = "tijera"
print(NEGRILLA+ RED+("♥")+END)
print("\tO = Piedra\tD = Papel\tX = Tijera\n")
print(BLUE)

#Seleccion de materia

jugada_U = ""

def THEGAME(J):
  jugada_U = input("cual sera su jugada: \n\n\n")
    #1_sola_Materias 

  if acum =="a" :
    pregunta = random.randint(1,4)
  elif acum =="f" :
    pregunta = random.randint(5,8)
  elif acum =="c" :
    pregunta = random.randint(9,12)
  elif acum =="p" :
    pregunta = random.randint(13,16)

  #2_Materias 


  elif acum =="ac" or acum =="ca" :
    pregunta = random.randint(1,8)
  elif acum =="af" or acum =="fa" :
    pregunta = random.randint(random.randint(1,4),random.randint(9,12))
  elif acum =="ap" or acum =="pa" :
    pregunta = random.randint(random.randint(1,4),random.randint(13,16))
  elif acum =="cf" or acum =="fc" :
    pregunta = random.randint(5,12)
  elif acum =="cp" or acum =="pc" :
    pregunta = random.randint(random.randint(5,8),random.randint(13,16))
  elif acum =="fp" or acum =="pf" :
    pregunta = random.randint(9,16)


  #3_Materias

  elif acum =="acf" or acum =="afc" or acum =="caf" or acum =="cfa" or acum =="fac" or acum =="fca":
    pregunta = random.randint(1,12)
  elif acum =="acp" or acum =="apc" or acum =="cap" or acum =="cpa" or acum =="pac" or acum =="pca":
    pregunta = random.randint(random.randint(1,8),random.randint(13,16))
  elif acum =="cfp" or acum =="cpf" or acum =="fcp" or acum =="fpc" or acum =="pcf" or acum =="pfc":
    pregunta = random.randint(5,16)
  elif acum =="afp" or acum =="apf" or acum =="fap" or acum =="fpa" or acum =="paf" or acum =="pfa":
    pregunta = random.randint(random.randint(1,4),random.randint(9,16))

  #todas

  else:
    pregunta = random.randint(1,16)

  #Turno del jugador

  print(BLUE)
  
  if jugada_U == "O" or jugada_U == "o":
    vU = 1
    print("               ⢀⣾⣿⣦⠀⢀                     ")
    print("              ⠼⠿⠿⠃⠼⠿⣿⠀⣀⣀⠀               ")
    print("          ⢀⣶⣶⣶⣶⣶⣶⣶⠂⠎⣰⣿⣿⡇              ")
    print("        ⢀⣾⣿⣿⣿⡟⠛⣋⣡⡞⣰⣿⣿⡟                 ")
    print("        ⣾⣿⣿⣿⡟⢰⣿⣿⡟⢠⣿⣿⡟⢠⣿⣿⡆             ")
    print("       ⢸⣿⣿⣿⣿⣦⣤⣉⠛⢀⣿⣿⡿⢁⣿⣿⣿⡇            ")
    print("       ⠈⠻⣿⣿⣿⣿⣿⣿⣷⡄⠙⠛⠁⣾⣿⢁⣾⡇            ")
    print("          ⠙⣿⣿⣿⣿⣿⣿⣿⢸⣿⣧⣌⣡⣾⣿⡇            ")
    print("           ⠈⢻⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⠁            ")
    print("             ⢹⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⠃              ")
    print("             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃                ")
    print("             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿                 ")
    print("             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿                 ")
    print("             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿                ")

  elif jugada_U == "D" or jugada_U == "d" :
    vU = 2
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣦⢸⣿⣿⣿⢀⣶⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣷⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣾⣿⣿⣿⣾⣿⣿⣿⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣴⣿⣷⡄⠀⠀⠀⠀ ⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀ ⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")


  elif jugada_U == "X" or jugada_U == "x" :
    vU = 3
    print("⠀⠀⠀      ⠀⠀⣀⣀⣤⣴⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣶⣦⠀⠀     ")
    print("⠀      ⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠀⠀    ")
    print("      ⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢹⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀     ")
    print("      ⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⢹⣿⣿⣿⡆⠸⣟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ")
    print("      ⣿⣿⣿⣿⣿⣿⣿⠶⠃⡀⠘⣿⣿⣿⣇⠀⣿⣿⣿⣿⣿⣶⣶⣶⣶⣤⣤⣤⣤⡀    ")
    print("      ⣿⣿⣿⣿⡋⠉⣁⣤⣾⣷⠀⢿⣿⣿⣿⠀⣀⣀⣀⣀⣀⠈⢻⣿⣿⣿⣿⣿⣿⣿    ")
    print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠛⠛⠋⣠⣿⣿⣿⣿⣿⡇⠀⠈⠉⠉⠉⠉⠉⠁    ")
    print("      ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⢀⣉⣉⣉⣉⣉⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")
    print("      ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")
    print("⠀      ⠈⠙⠿⠿⠿⡿⢿⠿⠿⡿⢷⠄⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")

  else:
    while   jugada_U != "O" or jugada_U != "o" or jugada_U != "D" or jugada_U != "d" or jugada_U != "X" or jugada_U != "x" :
      jugada_i = input("Jugada invalida intente nuevamente: \n\n\n")
      THEGAME(jugada_i)
    else :
      jugada_U = jugada_U  

  print(END)
  print(MAGENTA+NEGRILLA+"\t\t       VS"+END)
  print(RED)
  time.sleep(1)

  #Turno del la maquina

  jugada_M = random.randint(1,3)
  if jugada_M == 1:
    vM = 1

    print("               ⢀⣾⣿⣦⠀⢀                     ")
    print("              ⠼⠿⠿⠃⠼⠿⣿⠀⣀⣀⠀               ")
    print("          ⢀⣶⣶⣶⣶⣶⣶⣶⠂⠎⣰⣿⣿⡇              ")
    print("        ⢀⣾⣿⣿⣿⡟⠛⣋⣡⡞⣰⣿⣿⡟                 ")
    print("        ⣾⣿⣿⣿⡟⢰⣿⣿⡟⢠⣿⣿⡟⢠⣿⣿⡆             ")
    print("       ⢸⣿⣿⣿⣿⣦⣤⣉⠛⢀⣿⣿⡿⢁⣿⣿⣿⡇            ")
    print("       ⠈⠻⣿⣿⣿⣿⣿⣿⣷⡄⠙⠛⠁⣾⣿⢁⣾⡇            ")
    print("          ⠙⣿⣿⣿⣿⣿⣿⣿⢸⣿⣧⣌⣡⣾⣿⡇            ")
    print("           ⠈⢻⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⠁            ")
    print("             ⢹⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⠃              ")
    print("             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃                ")
    print("             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿                 ")
    print("             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿                 ")
    print("             ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿                ")
  elif  jugada_M == 2:
    vM = 2
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣦⢸⣿⣿⣿⢀⣶⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣷⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣾⣿⣿⣿⣾⣿⣿⣿⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣴⣿⣷⡄⠀⠀⠀⠀ ⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀ ⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")  
  else:
    vM = 3
    print("⠀⠀⠀      ⠀⠀⣀⣀⣤⣴⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣶⣦⠀⠀     ")
    print("⠀      ⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠀⠀    ")
    print("      ⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢹⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀     ")
    print("      ⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⢹⣿⣿⣿⡆⠸⣟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ")
    print("      ⣿⣿⣿⣿⣿⣿⣿⠶⠃⡀⠘⣿⣿⣿⣇⠀⣿⣿⣿⣿⣿⣶⣶⣶⣶⣤⣤⣤⣤⡀    ")
    print("      ⣿⣿⣿⣿⡋⠉⣁⣤⣾⣷⠀⢿⣿⣿⣿⠀⣀⣀⣀⣀⣀⠈⢻⣿⣿⣿⣿⣿⣿⣿    ")
    print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠛⠛⠋⣠⣿⣿⣿⣿⣿⡇⠀⠈⠉⠉⠉⠉⠉⠁    ")
    print("      ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⢀⣉⣉⣉⣉⣉⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")
    print("      ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")
    print("⠀      ⠈⠙⠿⠿⠿⡿⢿⠿⠿⡿⢷⠄⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")   
  
    print(END)

  #Victoria
  win = vU - vM
  victoria =0

   
  if win==1 or win==-2 :
    print("Usted"+GREEN+ NEGRILLA+" GANA "+END+"\nLa maquina"+RED+ NEGRILLA+" PIERDE "+END)
    print("Continua JUGANDO")
    victoria=1+victoria
    print(f"{victoria}")
    THEGAME(jugada_U)
    if victoria ==3:
      print("GANASTE!!!!") 



  #Derrota

  elif win==-1 or win==2 :
    print("Usted "+RED+NEGRILLA+ " PIERDE"+END+"\nLa maquina"+GREEN+NEGRILLA +" GANA\n\n "+END)
    print(NEGRILLA+RED+" \t\t\t\tBIENVENIDO AL GULAG "+ END)
    print("\n")
    
  
    if pregunta == 1 :
      s = input(f"{q1}")
      if s == r1:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36) 
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN) 
        print(END) 
    elif pregunta == 2 :  
      s = input(f"{q2}")
      if s == r2:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36) 
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN) 
        print(END)  
    elif pregunta == 3 :  
      s = input(f"{q3}")
      if s == r3:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 4 :  
      s = input(f"{q4}")
      if s == r4:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 5 :  
      s = input(f"{q5}")
      if s == r5:
        r = print("correcto, vuelves al juego")
        THEGAME(input("cual sera su jugada: \n\n\n"))
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 6 :  
      s = input(f"{q6}")
      if s == r6:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 7 :  
      s = input(f"{q7}")
      if s == r7:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 8 :  
      s = input(f"{q8}")
      if s == r8:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 9 :  
      s = input(f"{q9}")
      if s == r9:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 10 :  
      s = input(f"{q10}")
      if s == r10:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END)  
    elif pregunta == 11 :  
      s = input(f"{q11}")
      if s == r11:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 12 :  
      s = input(f"{q12}")
      if s == r12:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END)  
    elif pregunta == 13 :  
      s = input(f"{q13}")
      if s == r13:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END)  
    elif pregunta == 14 :  
      s = input(f"{q14}")
      if s == r14:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 15 :  
      s = input(f"{q15}")
      if s == r15:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    elif pregunta == 16 :  
      s = input(f"{q16}")
      if s == r16:
        r = print("correcto, vuelves al juego")
        THEGAME(jugada_U)
      else:
        print(CYAN+"■"*35+NEGRILLA+(RED+" GAME OVER ")+CYAN+"■"*36)
        print(NEGRILLA+(RED+" debes estudiar mas esa(s) materia ")+CYAN)  
        print(END) 
    
  #Empate
    
  else: 
    print(NEGRILLA+ "hay EMPATE, se repite el match")  
    THEGAME(jugada_U)

THEGAME(jugada_U)