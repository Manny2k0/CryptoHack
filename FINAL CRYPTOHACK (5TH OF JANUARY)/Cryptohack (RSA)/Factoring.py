from factordb.factordb import FactorDB

target_number = 510143758735509025530880200653196460532653147

factor_database = FactorDB(target_number)
factor_database.connect()

smallest_factor = None
for factor in factor_database.get_factor_list():
    if smallest_factor is None or factor < smallest_factor:
        smallest_factor = factor
print(smallest_factor)