FROM python:alpine
WORKDIR /geekrobot
ADD . .
RUN pip install -U wxpy
RUN apk add build-base jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install pillow
CMD ["python", "main.py"]
