FROM python:3.12.2-slim
WORKDIR /app/
ADD data/results_full.csv /app
ADD viz_config.json /app
ADD dashboard.py /app
ADD requirements.txt /tmp
RUN python -m pip install --no-cache-dir $(echo `cat /tmp/requirements.txt`)
ENTRYPOINT ["python"]
CMD ["dashboard.py"]