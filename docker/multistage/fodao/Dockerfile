FROM golang AS buildando 

ADD . /app

WORKDIR /app

RUN go build -o goapp

FROM alpine:3.1 
WORKDIR /app
COPY --from=buildando /app/goapp /app

ENTRYPOINT ./goapp


