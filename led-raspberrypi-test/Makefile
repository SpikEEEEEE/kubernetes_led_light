
# make led_light_mapper
.PHONY: default led_light_mapper
led_light_mapper:
	env GO111MODULE=on GOPROXY=https://goproxy.cn,direct /snap/bin/go build light_mapper.go
	docker build -t led-light-mapper:v1.1 .
