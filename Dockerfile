FROM python:3.6.9

ARG BUILD_GIT_BRANCH
ARG BUILD_GIT_COMMIT
ARG BUILD_GIT_AUTHOR
ARG BUILD_GIT_AUTHOR_NAME
ARG BUILD_GIT_REPO_LINK
ARG BUILD_CREATED
ARG BUILD_NUMBER

ADD requirements.txt /src/
RUN pip install -r /src/requirements.txt

ADD . /src
WORKDIR /src/

# Store all build args env variables into a file for later use
RUN env | grep BUILD_ > /src/build_envs.txt; exit 0
CMD ["server"]
ENTRYPOINT ["/src/boot.sh"]
