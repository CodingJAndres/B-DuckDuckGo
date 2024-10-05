# Buscador de DuckDuckGo

Este script permite realizar búsquedas en DuckDuckGo y mostrar los resultados en la terminal. Además, puedes guardar los resultados en un archivo de texto.

## Características

- **Búsqueda simple**: Permite ingresar un término de búsqueda.
- **Número de resultados**: Especifica cuántos resultados deseas mostrar.
- **Guardar resultados**: Opción para guardar los resultados en un archivo.
- **Arte ASCII**: Presenta un arte ASCII al inicio de la ejecución.
- **Colores**: Resultados y mensajes en color para una mejor visualización.

## Requisitos

- Python 3
- Bibliotecas: `requests`, `beautifulsoup4`

## Instalación

1. Clona el repositorio o descarga el archivo `buscador.py`.
2. Asegúrate de tener Python 3 instalado en tu sistema.
3. Instala las bibliotecas requeridas:

   ```bash
   pip install requests beautifulsoup4
   ```

## Uso

1. Ejecuta el script:

   ```bash
   python3 duckfinder.py
   ```

2. Ingresa el término de búsqueda.
3. Especifica el número de resultados que deseas mostrar.
4. Elige si deseas guardar los resultados en un archivo de texto (s/n).
5. Los resultados se mostrarán en la terminal.

## Ejemplo

```
[-] Ingrese el término de búsqueda: los simpson
[-] Ingrese el número de resultados a mostrar: 5
[-] ¿Desea guardar los resultados en un archivo? (s/n): n
[-] Realizando búsqueda para: los simpson
[-] Resultados encontrados para 'los simpson':
[1] https://ejemplo.com/result1
[2] https://ejemplo.com/result2
[3] https://ejemplo.com/result3
[4] https://ejemplo.com/result4
[5] https://ejemplo.com/result5
```

## Notas

- Si la búsqueda devuelve un error, revisa que el término de búsqueda sea válido.
- Asegúrate de tener conexión a internet al ejecutar el script.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
