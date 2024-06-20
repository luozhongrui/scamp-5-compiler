all: build
.PHONY: build

# Do not named user and group the same, this would cause error in entrypoint.sh
#	because we create the group before user exist which allowing name-crash in useradd command
CONTAINER_USERNAME ?= student
CONTAINER_GROUPNAME ?=studentg

CONTAINER_HOMEDIR ?= /home/student
IMAGE_NAME ?= scamp-5-env

build: Dockerfile
	docker build \
		--build-arg CONTAINER_USERNAME=${CONTAINER_USERNAME} \
		--build-arg CONTAINER_GROUPNAME=${CONTAINER_GROUPNAME} \
		--build-arg CONTAINER_HOMEDIR=${CONTAINER_HOMEDIR} \
		-t $(IMAGE_NAME) .
