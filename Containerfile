FROM docker.io/n8nio/runners:1.121.0
USER root
RUN cd /opt/runners/task-runner-javascript && CI=true pnpm install && pnpm add moment uuid @xivapi/nodestone
RUN cd /opt/runners/task-runner-python && uv pip install numpy pandas polars beautifulsoup4 lxml pydantic selectolax python-dateutil
COPY n8n-task-runners.json /etc/n8n-task-runners.json

COPY enable_stdlib.py /tmp/enable_stdlib.py
RUN  cd /etc && python3 /tmp/enable_stdlib.py

USER runner