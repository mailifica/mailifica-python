import mailifica

# Definir API Key globalmente ou via MAILIFICA_API_KEY no ambiente
mailifica.api_key = "ma_live_123456789"

params: mailifica.Emails.SendParams = {
    "from": "onboarding@suaempresa.ao",
    "to": ["cliente@gmail.com"],
    "subject": "Boas-vindas ao Mailifica!",
    "html": "<h1>Olá!</h1><p>Seu e-mail transacional foi entregue com sucesso.</p>",
}

try:
    response = mailifica.Emails.send(params)
    print("E-mail enviado com sucesso. ID:", response.get("id"))
except mailifica.MailificaError as e:
    print(f"Erro ({e.status_code}): {e.message}")
