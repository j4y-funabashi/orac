docker-build-dev:
	tar -czvf app.tar.gz app
	mv app.tar.gz resources/docker/app/
	docker-compose -f resources/docker/docker-compose-dev.yml build

run:
	docker-compose -f resources/docker/docker-compose-dev.yml up
