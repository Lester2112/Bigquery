class Bq:
    def query():
        return BqQuery()
        

class BqQuery():
    def __init__(self):
        self.query = ""
    
    def select(self, columns):
        if isinstance(columns, BqQuery):
            self.query += f"SELECT ({columns})\n"
        self.query += f"SELECT {columns}\n"
        return self
    
    def fromTable(self, table):
        if isinstance(table, BqQuery):
            self.query += f"FROM ({table})\n"
        else:
            self.query += f"FROM {table}\n"
        return self
    def join(self, table,type,on):
        if isinstance(table, BqQuery):
            self.query += f"{type} JOIN ({table} ON {on})\n"
        else:
            self.query += f"{type} JOIN {table} ON {on}\n"
        return self
    
    def where(self,condition):
        if isinstance(condition, BqQuery):
            self.query += f"WHERE ({condition})\n"
        else:
            self.query += f"WHERE {condition}"
        return self
    def having(self,condition):
        if isinstance(condition, BqQuery):
            self.query += f"HAVING ({condition})\n"
        else:
            self.query += f"HAVING {condition}"
        return self
    def __str__(self):
        return self.query



# Chaining with a subquery in fromTable
result = Bq.query().select("A").fromTable(Bq.query().select("B").fromTable("C"))

print(result)