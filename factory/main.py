from .factory import MySqlFactory

# a ideia foi retornar um obj ja estanciado la no mysqlfactory
usecase = MySqlFactory.create()
response = usecase.do_something(True)