import os
from django.conf import settings

class Helpers:

    def _read_build_env(self):
        result = {}
        with open(os.path.join(os.getcwd(), settings.BUILD_ENVS)) as f:
            for l in f:
                tokens = l.split('=') # pragma: no cover
                result[tokens[0]] = tokens[1].rstrip() # pragma: no cover
        return result