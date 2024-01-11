from SublimeLinter.lint import Linter, util


class BeanCheck(Linter):
    cmd = ('bean-check',)
    print('test')
    regex = r'^\S.*:(?P<line>[0-9]+):\s*(?P<message>.*)$'
    multiline = False
    error_stream = util.STREAM_STDERR

    tempfile_suffix = '.beancount'
    defaults = {
        'selector': 'source.beancount'
    }
