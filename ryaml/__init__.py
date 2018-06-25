import os
import yaml


class IncludeLoader(yaml.Loader):
    """ Define a custom yaml.Loader which can understand the
        `!include` tag.
    """
    base_path = None

    def __init__(self, stream):
        self.base_path = os.path.split(stream.name)[0]
        super(IncludeLoader, self).__init__(stream)

    def include(self, node):
        try:
            p = os.path.join(self.base_path, node.value)
            with open(p, "r") as fin:
                node = yaml.load(fin, IncludeLoader)
        except Exception as e:
            pass
        return node

IncludeLoader.add_constructor("!include", IncludeLoader.include)
