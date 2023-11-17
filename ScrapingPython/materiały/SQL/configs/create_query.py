import json


def return_not_null(is_not_null):
    return "NOT NULL" if is_not_null else ""


def return_unique(is_unique):
    return "UNIQUE" if is_unique else ""


config = json.load( open( "configs/blogposts.json", "r" ) )

create_query = "CREATE TABLE blogposts ("

columns_definitions = []
for col in config["columns"]:
    single_column_definition = col["name"] + " " + col["type"] + " " + return_not_null(
        col.get( "not_null", 0 ) ) + " " + return_unique( col.get( "unique", 0 ) )
    columns_definitions.append( single_column_definition )

columns_definition = ','.join( columns_definitions )

create_query += columns_definition + ");"

print( create_query )