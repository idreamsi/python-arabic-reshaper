from .arabic_reshaper import reshape, default_reshaper, ArabicReshaper

import os

exec(open(os.path.join(os.path.dirname(__file__), '__version__.py')).read())
