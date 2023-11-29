FROM postgres:latest

# Determinar variáveis de ambiente
ARG POSTGRES_PASSWORD
ARG POSTGRES_USER
ARG POSTGRES_DB
ARG DB_HOST
ARG DB_PORT

# Definir variáveis de ambiente
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}

# Expor a porta padrão do Postgres
EXPOSE 5433

# Definir o comando padrão para executar o container
CMD ["postgres"]