all: project

.PHONY: restore project test clean autograde

IMAGE_NAME = scamp-5-env



# TODO: add a clean build opiton
project:
	make -C src/
project-clean:
	${MAKE} clean -C src/

test: project
	make -C test/
test-clean:
	${MAKE} clean -C test/

clean:	project-clean test-clean



# Docker
# ========================================================
# ██████╗  ██████╗  ██████╗██╗  ██╗███████╗██████╗
# ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
# ██║  ██║██║   ██║██║     █████╔╝ █████╗  ██████╔╝
# ██║  ██║██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
# ██████╔╝╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
# ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
# ========================================================


.PHONY: docker-build docker-push activate

# Do not named user and group the same, this would cause error in entrypoint.sh
#	because we create the group before user exist which allowing name-crash in useradd command
IMAGE_FULLNAME = scamp-5-env
CONTAINER_USERNAME = student
CONTAINER_GROUPNAME = studentg
HOST_NAME = SCAMP-5
HOMEDIR = /home/$(CONTAINER_USERNAME)

docker-build:
	${MAKE} \
		IMAGE_NAME=${IMAGE_NAME} \
		CONTAINER_USERNAME=${CONTAINER_USERNAME}\
		CONTAINER_GROUPNAME=${CONTAINER_GROUPNAME}\
		CONTAINER_HOMEDIR=${HOMEDIR}\
		HOMEDIR=${HOMEDIR} \
		-C docker

activate:
	python3 docker/activate_docker.py \
		--username ${CONTAINER_USERNAME} \
		--homedir ${HOMEDIR} \
		--imagename ${IMAGE_FULLNAME} \
		--hostname ${HOST_NAME} ${ARGS}
