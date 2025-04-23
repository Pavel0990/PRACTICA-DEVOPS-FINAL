# Usar la imagen oficial de Nginx
FROM nginx:latest

# Copiar la página HTML al contenedor
COPY nginx/index.html /usr/share/nginx/html/index.html

# Copiar la configuración de Nginx
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
