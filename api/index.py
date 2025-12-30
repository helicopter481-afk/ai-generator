from app import app

# Vercel serverless handler
def handler(request):
    return app(request, lambda *args: None)

# Export untuk Vercel
handler.__name__ = 'handler'
