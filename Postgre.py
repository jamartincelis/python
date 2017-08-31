import psycopg2

try:
	# Conexion a la base de datos
    conn = psycopg2.connect("dbname='ejemplo' user='admin' host='localhost' password='j18129576'")
    print "Me conecto a la base de datos"
    
    # Se abre cursor para hacer operaciones en la BD
    cur = conn.cursor()
    print "Se abre cursor para hacer operaciones en la BD"
    
    # Ejecuto un comando: crear una tabla
    #cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    #print "Se crea la tabla"
    
    # Se inserta valores en la tabla
    # Se maneja el SQL injection!
    #cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
    #print "Se insertan datos en la tabla"
    
    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM test;")
    print cur.fetchone()
    
    # Make the changes to the database persistent
    conn.commit()
    
    # Close communication with the database
    cur.close()
    conn.close()
except:
    print "I am unable to connect to the database"