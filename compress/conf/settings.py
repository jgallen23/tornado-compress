#from django.core.exceptions import ImproperlyConfigured
#from django.conf import settings
from app import settings

def get(settings, var, default):
    return settings.get(var, default)
COMPRESS = get(settings, 'COMPRESS', not settings['debug'])
COMPRESS_AUTO = get(settings, 'COMPRESS_AUTO', True)
COMPRESS_VERSION = get(settings, 'COMPRESS_VERSION', False)
COMPRESS_VERSION_PLACEHOLDER = get(settings, 'COMPRESS_VERSION_PLACEHOLDER', '?')
COMPRESS_VERSION_DEFAULT = get(settings, 'COMPRESS_VERSION_DEFAULT', '0')
COMPRESS_VERSIONING = get(settings, 'COMPRESS_VERSIONING', 'compress.versioning.mtime.MTimeVersioning')

COMPRESS_CSS_FILTERS = get(settings, 'COMPRESS_CSS_FILTERS', ['compress.filters.csstidy.CSSTidyFilter'])
COMPRESS_JS_FILTERS = get(settings, 'COMPRESS_JS_FILTERS', ['compress.filters.jsmin.JSMinFilter'])
COMPRESS_CSS = get(settings, 'COMPRESS_CSS', {})
COMPRESS_JS = get(settings, 'COMPRESS_JS', {})

if COMPRESS_CSS_FILTERS is None:
    COMPRESS_CSS_FILTERS = []

if COMPRESS_JS_FILTERS is None:
    COMPRESS_JS_FILTERS = []


