import requests
from bs4 import BeautifulSoup

# Definición de los colores
class Colores:
    VERDE = '\033[92m'
    ROJO = '\033[91m'
    AZUL = '\033[94m'
    AMARILLO = '\033[93m'
    RESET = '\033[0m'

# Arte ASCII
arte_ascii = f"""{Colores.AMARILLO}
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                 :::---::-===--:          
                                                              .-=----===+++*++=-+=.       
                                                            .==-=+*+=-:.    .:-+*+++      
                                                           :=-=*=:               .=**.    
                                                          -=-*=                    .**    
                                                         .+=#.                      .#=   
                                                         =:#:                        #*   
                                                         ==#   ................      %+   
                                                         -*#                        =@.   
                                                         .@%:                      =@=    
                                   .:-=========:          @%#:                   :#%=     
                            .-=+++**+=-------+-=*+:    :=+*=*#+:              .=#@*:      
                         .+*+-:-----+*****+==-----+*=-+++*#*#=+##*=-:....:-=*%@%+:        
                        =#--------------:-=*#+==-::--*#***#%.  .-=*%%%%@@@%#*=:           
                      -**+---:=+=---------=+=*#===-:==+%%*-          ....                 
                     ++---------=****==--==---=%*===#---*.                                
                    +*:--------------+**===----=@%#++*+-+-                                
                   -%----=------------:=#+==----*%#+##-:                                  
                  :#-:----**==--------==-#+=----=#+#-                                     
                 .%-:-----:=**+=======----#+=---+%+                                       
                 #=-----------=**+=====----#==+#@=                                        
               :*=---------------=**===----#+**%-                                         
        .=----:+*:----=-------------+*==--=#==*+                                          
       =+-....-#-:---:-++==----------=#+**+==*-                                           
      +=:....:%-:-------=##*+==--=--==*+===*+                                             
     +=:.....+*--------===-=+**#*===+*+==**:                                              
    +--.....:#=:---------------==+*++==*+:                                                
   --=......-%=:----------------=*==+*=.                                                  
   +.=......:#+----------------==%==:                                                     
   -=-......:=%==------------==+*:                                                        
    #:.......-+%+===------===+*-                                                          
    =-:.:#=..=*+##+=======+*#*.                                                           
    .+....-+*====+*##****###-                                                             
     =-=+*+==========++*#*-                                                               
     -=+**#***######*++-                                                                  
            ....                                                                          
{Colores.RESET}
"""

def buscar_en_duckduckgo(termino_busqueda, num_resultados):
    url = f"https://html.duckduckgo.com/html/?q={termino_busqueda}"
    
    # Añadiendo el encabezado User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    respuesta = requests.get(url, headers=headers)
    
    if respuesta.status_code != 200:
        print(f"{Colores.ROJO}[-] Error al realizar la búsqueda: {respuesta.status_code}{Colores.RESET}")
        return []

    soup = BeautifulSoup(respuesta.text, 'html.parser')
    resultados = []
    
    for enlace in soup.find_all('a', class_='result__a', limit=num_resultados):
        resultados.append(enlace['href'])
    
    return resultados

def main():
    print(arte_ascii)
    
    print(f"{Colores.AZUL}[-] Ingrese el término de búsqueda: {Colores.RESET}", end="")
    termino_busqueda = input().strip()
    
    print(f"{Colores.AZUL}[-] Ingrese el número de resultados a mostrar: {Colores.RESET}", end="")
    num_resultados = int(input().strip())
    
    print(f"{Colores.AZUL}[-] ¿Desea guardar los resultados en un archivo? (s/n): {Colores.RESET}", end="")
    guardar = input().strip().lower() == 's'

    print(f"\n{Colores.AZUL}[-] Realizando búsqueda para: {termino_busqueda}{Colores.RESET}")
    resultados = buscar_en_duckduckgo(termino_busqueda, num_resultados)
    
    if resultados:
        print(f"\n{Colores.AZUL}[-] Resultados encontrados para '{termino_busqueda}':{Colores.RESET}")
        for i, resultado in enumerate(resultados, 1):
            print(f"{Colores.VERDE}[{i}] {resultado}{Colores.RESET}")
        
        if guardar:
            with open('resultados_busqueda.txt', 'w') as f:
                for resultado in resultados:
                    f.write(f"{resultado}\n")
            print(f"{Colores.VERDE}[-] Resultados guardados en 'resultados_busqueda.txt'{Colores.RESET}")
    else:
        print(f"{Colores.ROJO}[-] No se encontraron resultados.{Colores.RESET}")

if __name__ == "__main__":
    main()
