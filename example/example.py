#!/usr/bin/env python

import os
import yaml


class CustomYamlLoader(yaml.Loader):
    base_path = None

    def __init__(self, stream):
        self.base_path = os.path.split(stream.name)[0]
        super(CustomYamlLoader, self).__init__(stream)

    def include(self, node):
        try:
            p = os.path.join(self.base_path, node.value)
            with open(p, "r") as fin:
                node = yaml.load(fin, CustomYamlLoader)
        except Exception as e:
            print("YAML !include exception:", e)
            pass
        return node

CustomYamlLoader.add_constructor("!include", CustomYamlLoader.include)


with open("example/main.yaml", "r") as fin:
    doc = yaml.load(fin, CustomYamlLoader)
    print doc

    print "-"*80

    ygen = yaml.parse(fin, CustomYamlLoader)
    for item in ygen:
        if type(item) is yaml.events.StreamStartEvent:
            print "Stream started"
        elif type(item) is yaml.events.StreamEndEvent:
            print "Stream ended ..."
        else:
            print "Unhandled event type: %s" % (type(item))