# example http server

based on: https://github.com/mongoose-os-apps/empty

added libs: mongoose-os-libs/wifi, mongoose-os-libs/http-server

## Behaviour
When we build this app with mongoose-os v2.3 versus mongoose-os v1.26 the heap available
to us AFTER connecting to the http server is around 1.3kB less. (we just use a different mos tool (mos update 2.0/1.26) to build)

v1.26:
======
mgos_http_ev         0x3fff0d34 HTTP connection from 192.168.4.2:54413
endpoint_handler     available heap: 45268

v2.3
======
mgos_http_ev         0x3fff0ed4 HTTP connection from 192.168.4.2:54710<\n>
endpoint_handler     available heap: 43948

please see folder "logs" for detailled logs! The heap increase happens when switching from v1.26 to 2.0!
