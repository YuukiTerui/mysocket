import sys
import pickle

class _const:
    class ConstError(TypeError):
        pass
    MSGLEN = 2 ** 12
    MSGSTART = pickle.dumps('<<')
    MSGEND = pickle.dumps('>>')

    def __setattr__(self, name, value) -> None:
        if name in self.__dict__:
            raise self.ConstError
        self.__dict__[name] = value


sys.modules[__name__] = _const()