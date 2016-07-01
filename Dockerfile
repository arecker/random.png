FROM golang
MAINTAINER Alex Recker <alex@reckerfamily.com>

WORKDIR /srv
COPY ./randomImages.go ./
RUN go build randomImages.go
RUN rm randomImages.go
EXPOSE 5000

CMD ["./randomImages"]
