/*
 * Copyright (c) 2014-2018 Cesanta Software Limited
 * All rights reserved
 *
 * Licensed under the Apache License, Version 2.0 (the ""License"");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an ""AS IS"" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "mgos.h"
#include "mgos_http_server.h"

#define MAX_REPLY_LENGTH 100

static void endpoint_handler(struct mg_connection *nc, int ev, void *ev_data, void *user_data);

enum mgos_app_init_result mgos_app_init(void) {

  mgos_register_http_endpoint("/getheap", endpoint_handler, NULL);

  LOG(LL_INFO, ("Hi there"));
  return MGOS_APP_INIT_SUCCESS;
}

static void endpoint_handler(struct mg_connection *nc, int ev, void *ev_data, void *user_data) {
  (void)ev;
  (void)ev_data;
  (void)user_data;

  LOG(LL_INFO, ("available heap: %u",mgos_get_free_heap_size()));

  char reply[MAX_REPLY_LENGTH];
  snprintf(reply,MAX_REPLY_LENGTH,"available heap: %u",mgos_get_free_heap_size());
  mg_printf(nc,
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Connection: close\r\n\r\n"
            "Heap: %u\r\n",mgos_get_free_heap_size());
  nc->flags |= MG_F_SEND_AND_CLOSE;
  mg_send(nc, reply, strlen(reply));
}
