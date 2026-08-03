import pymysql

pymysql.install_as_MySQLdb()

# Python 3.14 Compatibility Patch for Django Template Context copy
try:
    from django.template import context
    def _patched_base_context_copy(self):
        obj = self.__class__.__new__(self.__class__)
        obj.__dict__.update(self.__dict__)
        obj.dicts = [d.copy() for d in self.dicts]
        return obj

    context.BaseContext.__copy__ = _patched_base_context_copy
    context.Context.__copy__ = _patched_base_context_copy
    context.RequestContext.__copy__ = _patched_base_context_copy
except Exception:
    pass

