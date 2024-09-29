# Usar uma imagem base do Python
FROM python:3.11

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de requisitos e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que o servidor vai usar
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
