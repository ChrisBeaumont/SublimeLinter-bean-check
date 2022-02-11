from SublimeLinter.lint import Linter, util


class BeanCheck(Linter):
    cmd = ('bean-check',)
    regex = r'^\S.*:(?P<line>[0-9]+):    (?P<message>.*)$'
    multiline = False
    error_stream = util.STREAM_STDERR

    tempfile_suffix = '.beancount'
    defaults = {
        'selector': 'source.beancount'
    }
