FROM python:3

# Install nginx
RUN apt-get update && apt-get install -y --no-install-recommends nginx
COPY nginx.default /etc/nginx/sites-available/default
RUN    ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Copy files
RUN mkdir -p /opt/fudge
COPY requirements.txt start-server.sh /opt/fudge/
COPY fudge /opt/fudge/fudge/
RUN chown -R www-data:www-data /opt/fudge

# Install dependenices
WORKDIR /opt/fudge
RUN pip install --upgrade pip; pip install -r requirements.txt
EXPOSE 8000

# Start server
CMD [ "/opt/fudge/start-server.sh" ]

