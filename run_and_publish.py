#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 Matt Martz
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys
import subprocess
from google.cloud import pubsub_v1
from google.auth import compute_engine

CREDENTIALS_FILE = "/home/pi/speedtest-cli/scgoc-construction-6497d1ff82b2.json"

output = subprocess.Popen(['./speedtest.py', '--simplejson'], stdout=subprocess.PIPE)
stdout = output.communicate()[0]
# print 'STDOUT:{}'.format(stdout)

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id='scgoc-construction',
    topic='speedtest_results',
)

# message = output.stdout.read()[0]
print("Message: {}".format(stdout))
if output.returncode != 1:
    publisher.publish(topic_name, stdout)

#
# if 'Invalid argument'.encode() not in stderr:
#     raise SystemExit(
#         '"Invalid argument" not found in stderr:\n%s' % stderr.decode()
#     )
