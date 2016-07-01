# random.png

Serves up a random image from a directory.

```
$ docker run -v path/to/images:/srv/images:ro -p 5000:5000 arecker/random.png:latest
```