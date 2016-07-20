def get(url, handler, name=None):
    namedict = dict(name=name) if name is not None else dict()
    return (('GET', url, handler, ), namedict, )


def post(url, handler, name=None):
    namedict = dict(name=name) if name is not None else dict()
    return (('POST', url, handler, ), namedict, )
