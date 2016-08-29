# random.png

Serve random images form a directory.  You can run the docker
container with a command resembling this one:

	docker run \
		-v ~/Pictures:/app/images:ro \
		-p 5000:5000 \
		--restart always
	arecker/random.png:latest
