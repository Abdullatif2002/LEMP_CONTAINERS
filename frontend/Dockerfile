# syntax=docker/dockerfile:1
FROM nginx:1.27-alpine

# Copy configuration and HTML file (no 'frontend/' prefix)
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
