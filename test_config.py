from config import Config

try:
    Config.validate_config()
    print(f"API_KEY cargada correctamente: {Config.OPENAI_API_KEY}")
    print(f"Directorio de PDFs: {Config.PDF_DIR}")
except ValueError as e:
    print(f"Error en la configuración: {e}")
