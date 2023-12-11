from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, query=All()):
        self._query=query

    
    def oneOf(self,m1,m2):
        return QueryBuilder(Or(m1,m2))
    

    def playsIn(self, team):
        return QueryBuilder(And(self._query,PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query,HasAtLeast(value,attr)))
    
    def hasFewerThan(self,value, attr):
        return QueryBuilder(And(self._query,HasFewerThan(value, attr)))
    
    def build(self):
        return self._query