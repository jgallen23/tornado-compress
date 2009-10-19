

def run(settings):
    force = False
    verbosity = 1

    from utils import needs_update, filter_css, filter_js

    for name, css in settings['COMPRESS_CSS'].items():
        u, version = needs_update(css['output_filename'],
            css['source_filenames'])

        if (force or u) or verbosity >= 2:
            msg = 'CSS Group \'%s\'' % name
            print msg
            print len(msg) * '-'
            print "Version: %s" % version

        if force or u:
            filter_css(css, verbosity)

        if (force or u) or verbosity >= 2:
            print

    for name, js in settings['COMPRESS_JS'].items():
        u, version = needs_update(js['output_filename'],
            js['source_filenames'])

        if (force or u) or verbosity >= 2:
            msg = 'JavaScript Group \'%s\'' % name
            print msg
            print len(msg) * '-'
            print "Version: %s" % version

        if force or u:
            filter_js(js, verbosity)

        if (force or u) or verbosity >= 2:
            print

def compressed(self, type, name):
    from compress import uimodules
    if type == 'css':
        return uimodules.compressed_css(name)
    elif type == 'js':
        return uimodules.compressed_js(name)
