# Agente IA Orquestador de Microagentes

## Descripción

Este proyecto es una aplicación modular en Python que implementa un agente de IA orquestador, especializado en IT y gestión de proyectos. El orquestador coordina microagentes expertos, cada uno con acceso a documentos PDF como fuente de conocimiento, para responder preguntas y resolver tareas específicas.

## Características

- **Arquitectura modular**: Separación clara entre orquestador, microagentes y utilidades.
- **Procesamiento de PDFs**: Los microagentes pueden extraer y citar información de documentos PDF.
- **Fácil integración**: Pensado para expandirse con nuevos agentes o herramientas.
- **Configuración segura**: Uso de variables de entorno para claves y configuraciones sensibles.

## Estructura del proyecto

```text
tu_proyecto/
├── agents/
│   ├── orchestrator.py
│   ├── document_qa_agent.py
│   └── project_mgmt_agent.py
├── tools/
│   ├── pdf_processor.py
│   └── utilities.py
├── data/
│   └── documents/
├── config.py
├── main.py
├── .env
├── .gitignore
└── LICENSE
```
