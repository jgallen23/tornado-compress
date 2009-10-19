import os

from compress.conf import settings
from compress.utils import media_root, media_url, needs_update, filter_css, filter_js, get_output_filename, get_version, get_version_from_file


def render_common(template, obj, filename, version):
    if settings.COMPRESS:
        filename = get_output_filename(filename, version)

    context = obj.get('extra_context', {})
    prefix = context.get('prefix', None)
    if filename.startswith('http://'):
        context['url'] = filename
    else:
        context['url'] = media_url(filename, prefix)
        
    #return template.loader.render_to_string(template_name, context)
    return template.replace("{{ url }}", context['url'])

def render_css(css, filename, version=None):
    template = '<link rel="stylesheet" type="text/css" href="{{ url }}"/>' 
    return render_common(template, css, filename, version)

def render_js(js, filename, version=None):
    template = '<script type="text/javascript" src="{{ url }}"></script>'
    return render_common(template, js, filename, version)


def compressed_css(css_name):
    try:
        css = settings.COMPRESS_CSS[css_name]
    except KeyError:
        return '' # fail silently, do not return anything if an invalid group is specified

    if settings.COMPRESS:

        version = None

        if settings.COMPRESS_AUTO:
            u, version = needs_update(css['output_filename'], 
                css['source_filenames'])
            if u:
                filter_css(css)
        else:
            filename_base, filename = os.path.split(css['output_filename'])
            path_name = media_root(filename_base)
            version = get_version_from_file(path_name, filename)
            
        return render_css(css, css['output_filename'], version)
    else:
        # output source files
        r = ''
        for source_file in css['source_filenames']:
            r += render_css(css, source_file)

        return r


def compressed_js(js_name):

    try:
        js = settings.COMPRESS_JS[js_name]
    except KeyError:
        return '' # fail silently, do not return anything if an invalid group is specified
    
    if 'external_urls' in js:
        r = ''
        for url in js['external_urls']:
            r += render_js(js, url)
        return r
                
    if settings.COMPRESS:

        version = None

        if settings.COMPRESS_AUTO:
            u, version = needs_update(js['output_filename'], 
                js['source_filenames'])
            if u:
                filter_js(js)
        else: 
            filename_base, filename = os.path.split(js['output_filename'])
            path_name = media_root(filename_base)
            version = get_version_from_file(path_name, filename)

        return render_js(js, js['output_filename'], version)
    else:
        # output source files
        r = ''
        for source_file in js['source_filenames']:
            r += render_js(js, source_file)
        return r


