from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .api import router as api_router
from datetime import datetime

app = FastAPI(
    title="API de Integração com LLM",
    description="Uma API para interagir com o Google Gemini.",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1", tags=["IA Chat"])

@app.get("/", tags=["Root"], response_class=HTMLResponse)
def read_root():
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{app.title}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                margin: 40px;
                background-color: #f7f7f7;
                color: #333;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 20px 40px;
                border-radius: 10px;
                box-shadow: 0 2px 15px rgba(0,0,0,0.1);
            }}
            h1 {{ color: #005fcc; }}
            a {{ color: #007bff; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            code {{
                background-color: #eee;
                padding: 2px 6px;
                border-radius: 4px;
                font-family: "Courier New", Courier, monospace;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 0.9em;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{app.title}</h1>
            <p><strong>Versão:</strong> {app.version}</p>
            <p>{app.description}</p>
            <p>
                A API está operacional. Para interagir e ver todos os endpoints disponíveis, acesse a documentação:
            </p>
            <ul>
                <li><a href="/docs"><strong>Documentação Interativa (Swagger UI)</strong></a></li>
                <li><a href="/redoc"><strong>Documentação Alternativa (ReDoc)</strong></a></li>
            </ul>
            <div class="footer">
                <p>Status: Ativo</p>
                <p>Horário do Servidor: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC</p>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)