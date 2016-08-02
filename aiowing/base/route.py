def __namedict(name):
    return dict(name=name) if name is not None else dict()


def get(url, handler, name=None):
    return (('GET', url, handler), __namedict(name))


def post(url, handler, name=None):
    return (('POST', url, handler), __namedict(name))
