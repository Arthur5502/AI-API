from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .api import router as api_router
from datetime import datetime
import pytz

app = FastAPI(
    title="API de Integração com LLM",
    description="Uma API profissional para interagir com o Google Gemini, desenvolvida como um projeto prático.",
    version="1.0.1",
    contact={
        "name": "Grupo 5",
        "url": "https://github.com/Arthur5502/AI-API.git",
    },
)

app.include_router(api_router, prefix="/api/v1", tags=["IA Chat"])

@app.get("/", tags=["Root"], response_class=HTMLResponse)
async def read_root():
    tz = pytz.timezone('America/Recife')
    current_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{app.title} - Status</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            }}
            .container {{
                text-align: center;
                background: rgba(255, 255, 255, 0.9);
                padding: 40px 50px;
                border-radius: 15px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(4px);
                -webkit-backdrop-filter: blur(4px);
                border: 1px solid rgba(255, 255, 255, 0.18);
                max-width: 600px;
                width: 90%;
            }}
            h1 {{
                font-weight: 600;
                color: #333;
                font-size: 2.5em;
                margin-bottom: 10px;
            }}
            .version-badge {{
                display: inline-block;
                background-color: #e8e8e8;
                color: #555;
                padding: 5px 15px;
                border-radius: 15px;
                font-size: 0.8em;
                font-weight: 600;
                margin-bottom: 20px;
            }}
            .status {{
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px 0;
                padding: 10px;
                background-color: #e6ffed;
                border-radius: 8px;
                border: 1px solid #b7e4c7;
            }}
            .status-indicator {{
                height: 12px;
                width: 12px;
                background-color: #28a745;
                border-radius: 50%;
                margin-right: 10px;
                animation: pulse 2s infinite;
            }}
            @keyframes pulse {{
                0% {{ box-shadow: 0 0 0 0 rgba(40, 167, 69, 0.7); }}
                70% {{ box-shadow: 0 0 0 10px rgba(40, 167, 69, 0); }}
                100% {{ box-shadow: 0 0 0 0 rgba(40, 167, 69, 0); }}
            }}
            .status-text {{
                color: #155724;
                font-weight: 600;
            }}
            .docs-links a {{
                display: inline-block;
                text-decoration: none;
                background-color: #007bff;
                color: white;
                padding: 12px 25px;
                border-radius: 8px;
                margin: 5px;
                font-weight: 400;
                transition: transform 0.2s, background-color 0.2s;
            }}
            .docs-links a:hover {{
                background-color: #0056b3;
                transform: translateY(-2px);
            }}
            .footer {{
                margin-top: 30px;
                font-size: 0.9em;
                color: #888;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{app.title}</h1>
            <span class="version-badge">Versão {app.version}</span>
            <p>{app.description}</p>
            
            <div class="status">
                <div class="status-indicator"></div>
                <span class="status-text">API Operacional</span>
            </div>

            <div class="docs-links">
                <a href="/docs" target="_blank">Documentação Interativa (Swagger)</a>
                <a href="/redoc" target="_blank">Documentação (ReDoc)</a>
            </div>

            <div class="footer">
                <p>Desenvolvido por: <a href="{app.contact['url']}" target="_blank">{app.contact['name']}</a></p>
                <p>Horário Local: {current_time}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)