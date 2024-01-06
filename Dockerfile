FROM nginx:mainline

EXPOSE 8000

WORKDIR /tasktool

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gettext python3 python-is-python3 python3-pip

RUN useradd -ms /bin/bash tasktool
RUN mkdir /tasktool/static
RUN mkdir /tasktool/media
RUN pip install --break-system-packages --upgrade pip

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

RUN mkdir ./nginx-templates
RUN mkdir ./nginx-conf.d
ENV NGINX_ENVSUBST_TEMPLATE_DIR /tasktool/nginx-templates
ENV NGINX_ENVSUBST_OUTPUT_DIR /tasktool/nginx-conf.d

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./nginx.default.conf.template ./nginx-templates/default.conf.template

COPY requirements.txt .
RUN pip install --break-system-packages -r requirements.txt

COPY ./src ./src

RUN chown -R tasktool:tasktool /tasktool

USER tasktool

CMD ["/tasktool/entrypoint.sh"]

