import mysql.connector

midb = mysql.connector.connect( #Para acceder a la base de datos
    host='localhost',
    user='root',
    password='@Hello_world</',
    database='prueba'
)

cursor = midb.cursor() # Un cursor es un objeto que permite interactuar
                       # Con la base de datos mediante SQL

# cursor.execute('select * from usuario ') # Para llamar el metodo de execute

# sql = 'insert into usuario (email,username,edad) values (%s, %s,%s)'
# values = ('micorreo@correo.co.nz', 'nombreusuario',45)
# cursor.execute('show create table usuario') # ver definiciones de tablas

# resultado = cursor.fetchall()#Fetchall sirve para devolver todas las intancias 
                             # de los elemento que encontro en la base de datos 

                             # fetchone sirve para devolver solo el primer elemento que encuentre en la
                             #base de datos
# print(resultado)

# actulizar datos
# sql = 'update usuario set email = %s where id = %s'
# values = ('micorreo@correo.com', 8)

# cursor.execute(sql,values) # Para cuando se hace una consulta en sql y querer cambia

# midb.commit() # para poder comprometery guardar la consulta

#print(cursor.rowcount)

# Eliminar datos

# sql = 'delete from usuario where id = %s '
# values = (8, )
# cursor.execute(sql, values )

# midb.commit()


 #Para poder limitar los elementos
cursor.execute('select * from usuario limit 2')
resultado = cursor.fetchall()
print(resultado)