
REPO_NAME := synfinmelab
IMAGE_NAME := py-dogs-histo
IMAGE_TAG := v0.2
IMAGE := "${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}"

_init	:
	echo "*** Use { build | push } ***"

build	:
	docker build -t ${IMAGE} .

push	: build
	docker push ${IMAGE}
