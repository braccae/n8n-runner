FROM docker.io/n8nio/runners:next

USER root

# WORKDIR /opt/runners/task-runner-javascript

# RUN rm -f node_modules/.modules.yaml
# RUN mv package.json package.json.bak
# COPY package.json /app/task-runner-javascript/package.json
# RUN pnpm install --prod --no-lockfile --silent
# RUN mv package.json extras.json
# RUN mv package.json.bak package.json

WORKDIR /opt/runners/task-runner-python

COPY extras.txt /app/task-runner-python/extras.txt
RUN uv pip install -r /app/task-runner-python/extras.txt

COPY --chown=root:root task-runners.json /etc/n8n-task-runners.json

USER runner