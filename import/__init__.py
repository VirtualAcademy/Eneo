import os, sys
import django

sys.path.append(os.path.dirname(os.path.abspath("__file__"))) #here is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fmms.settings")
django.setup()