# functions-from-zero-arm
live training


[![CI](https://github.com/ArmandoReyesRepo/functions-from-zero-arm/actions/workflows/main.yml/badge.svg)](https://github.com/ArmandoReyesRepo/functions-from-zero-arm/actions/workflows/main.yml)



### To cal Microservice

```bash
curl -X 'POST' \
  'https://fictional-fishstick-497657wq44qhqrq5-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
``````

### Build container
`docker build .`
`docker image ls`

### Run container

something like this
`docker run -p 127.0.0.1:8080:8080 c3481a6d88c7`

## Invoke POST request

run `invoke.sh`
