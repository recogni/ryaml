#!/usr/bin/env python

import os
import yaml
from ryaml import IncludeLoader

with open("example/main.yaml", "r") as fin:
    doc = yaml.load(fin, Loader=IncludeLoader)
    print doc

    print "-"*80

    for item in yaml.parse(fin, Loader=IncludeLoader):
        if type(item) is yaml.events.StreamStartEvent:
            print "Stream started"
        elif type(item) is yaml.events.StreamEndEvent:
            print "Stream ended ..."
        else:
            print "Unhandled event type: %s" % (type(item))