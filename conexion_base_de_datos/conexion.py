import pyscopg2   #Librería para conectar a bases de datos PostgreSQL

def conectar():  #Define la función para conectar con la base de datos
    try:  #Intenta establecer la conexión
        conexion=pyscopg2.connect(
            host="localhost",
            database="empleados",   #Nombre de tu base de datos
            user="postgres",  #Usuario por defecto de PostgreSQL
            password="",  #Contaseña de tu base de datos
        )
        print("Conxeión correcta a la base de datos")
        return conexion    #Devuelve el objeto de conexión 
    except Exception as e:   #Captura cualquier error
        print("Error al conectar a la base de datos",)    #Muestra el error en la pantalla

if __name__=="__main__":  #Ejecuta esto solo si el archivo se ejecuta directamente
    conectar()    #Llama la función para probar la conexión


















