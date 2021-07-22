import sys
import pickle

class _const:
    class ConstError(TypeError):
        pass
    PICKLE_PROTOCOL = 3

    MSGLEN = 2 ** 12
    MSGSTART = pickle.dumps('<<', protocol=PICKLE_PROTOCOL)
    MSGEND = pickle.dumps('>>', protocol=PICKLE_PROTOCOL)

    def __setattr__(self, name, value) -> None:
        if name in self.__dict__:
            raise self.ConstError
        self.__dict__[name] = value


sys.modules[__name__] = _const()