## Streamlit app

Para contar con el chat embebido en el segundo Iframe, es necesario levantar la aplicación implementada con Streamlit.

* Instalar Python 3.10
* Instalar Virtual Environment
	* pip install virtualenv
* Ejecutar **streamlit_setup_venv.sh**
	* Este script se encarga de crear un Virtual Environment con las dependencias de la app
* Ejecutar **streamlit_run_app.sh**
	* Este script levanta la app y la deja disponible en http://localhost:8501

Una vez que la aplicación se encuentre levantada, también se podrá ver integrado en el Live Server donde corre la POC.

### Opcional: 
Ambas aplicaciónes se pueden correr dentro de un contenedor docker utilizando la extension *devcontainer* en vscode. Si se utiliza dentro de un contenedor no hace falta instalar Live Server ni Python ya que se instalaran automáticamente. 
* La POC se corre de la misma forma con la opción **"Open With Live Server"**
* La aplicacion Streamlit se corre con el comando sin necesidad de crear un Virtual Environment
	*	**python3  -m  streamlit  run  streamlit-app/streamlit_app.py**
