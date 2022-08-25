#FROM balenalib/raspberrypi4-64-alpine-node
FROM arm64v8/golang:1.18.4-bullseye

CMD mkdir -p /light_mapper

COPY . /light_mapper/

WORKDIR /light_mapper

ENTRYPOINT ["/light_mapper/light_mapper","-logtostderr=true"]
