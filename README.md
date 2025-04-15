# Agente IA Orquestador de Microagentes

## Descripción

Este proyecto es una aplicación modular en Python que implementa un agente de IA orquestador, especializado en IT y gestión de proyectos. El orquestador coordina microagentes expertos, cada uno con acceso a documentos PDF como fuente de conocimiento, para responder preguntas y resolver tareas específicas.

## Características

- **Arquitectura modular**: Separación clara entre orquestador, microagentes y utilidades.
- **Procesamiento de PDFs**: Los microagentes pueden extraer y citar información de documentos PDF.
- **Fácil integración**: Pensado para expandirse con nuevos agentes o herramientas.
- **Configuración segura**: Uso de variables de entorno para claves y configuraciones sensibles.

## Estructura del proyecto

tu_proyecto/
├── agents/
│ ├── orchestrator.py
│ ├── document_qa_agent.py
│ └── project_mgmt_agent.py
├── tools/
│ ├── pdf_processor.py
│ └── utilities.py
├── data/
│ └── documents/
├── config.py
├── main.py
├── .env
├── .gitignore
└── LICENSE

Instalación
Clona el repositorio:

git clone https://github.com/tu_usuario/tu_repositorio.git

cd tu_repositorio

Crea y activa un entorno virtual (opcional pero recomendado):

bash
python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate
Instala las dependencias:

bash
pip install -r requirements.txt
Configura las variables de entorno:

Crea un archivo .env en la raíz del proyecto con tu clave de API:

text
LLM_API_KEY=tu_api_key
Uso
Coloca tus documentos PDF en la carpeta data/documents/.

Ejecuta la aplicación principal:

bash
python main.py
Interactúa con el agente orquestador y sus microagentes según las instrucciones en pantalla.

Licencia
Este proyecto está licenciado bajo la MIT License.

Contribuciones
¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para sugerencias, mejoras o correcciones.

Contacto
Para dudas o soporte, contacta a [xavi.saavedra.alois@gmail.com.
