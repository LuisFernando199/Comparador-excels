
```markdown
# Excel Comparator

Excel Comparator es una aplicación web creada con Flask que permite comparar dos archivos XLSX o CSV y reportar las diferencias. La aplicación soporta múltiples hojas en los archivos y muestra las diferencias en una interfaz atractiva y fácil de usar.

## Características

- Comparación de archivos Excel con múltiples hojas.
- Reporte de diferencias celda por celda.
- Interfaz web moderna y fácil de usar.

## Requisitos

- Python 3.7 o superior.
- pip (el instalador de paquetes de Python).

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/tu-usuario/excel-comparator.git
    cd excel-comparator
    ```

2. **Crea y activa un entorno virtual** (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

## Uso
1. **Crear una carpeta llamada uploads**

2. **Ejecuta la aplicación**:

    ```bash
    python app.py
    ```

2. **Abre tu navegador** y visita `http://127.0.0.1:5000/`.

3. **Sube dos archivos Excel** y presiona "Comparar". La aplicación mostrará las diferencias entre los archivos.

## Estructura del Proyecto

```
excel_comparator/
├── app.py
├── requirements.txt
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   └── result.html
└── uploads/
```

- `app.py`: Contiene la lógica principal de la aplicación Flask.
- `requirements.txt`: Lista de dependencias del proyecto.
- `static/styles.css`: Archivo CSS para los estilos de la aplicación.
- `templates/index.html`: Plantilla HTML para la página principal.
- `templates/result.html`: Plantilla HTML para mostrar los resultados de la comparación.
- `uploads/`: Carpeta para almacenar los archivos subidos temporalmente.

## Capturas de Pantalla

### Página Principal

![Página Principal](static/img/index.png)

### Resultados de la Comparación

![Resultados de la Comparación](static/img/result.png)

## Contribución

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y commitea (`git commit -am 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

```

### Notas

- **Capturas de Pantalla**: Si deseas incluir capturas de pantalla, asegúrate de tener las imágenes en la carpeta `static/img` y actualiza los nombres de los archivos en el README.
- **URL del Repositorio**: Reemplaza `https://github.com/tu-usuario/excel-comparator.git` con la URL de tu repositorio.
- **Requisitos Adicionales**: Si tienes requisitos adicionales, agrégalos en la sección de instalación.
- **Licencia**: Asegúrate de incluir un archivo `LICENSE` en tu repositorio si decides usar una licencia específica.

Este `README.md` debe proporcionar una guía clara y completa para cualquier usuario o desarrollador que quiera entender, instalar y contribuir a tu proyecto.
