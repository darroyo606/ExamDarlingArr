# ExamDarlingArr
Examen Tratamiento de Datos
# Requirements.txt
En este archivo se coloca los plugins que utilizaremos

Ejecutamos el comando pip install -r requirements.txt
# Se ha seleccionado una página para Extraer datos
https://www.deprati.com.ec/es/stefano/c/021001741

Se analiza si contiene api, aqui en previsualización se va observando donde se encuentra el formato JSON
![image](https://github.com/darroyo606/ExamDarlingArr/assets/55005126/b8381c1b-b1bf-4cd6-854b-bd6c3001206f)

Una vez que entendemos el formato JSON, nos vamos a headers y obtenemos la URL
![image](https://github.com/darroyo606/ExamDarlingArr/assets/55005126/fde91fe6-ada1-4f86-b8fe-a77db58f5552)

Nuestro Main con estos datos da de resultado lo siguiente:
![image](https://github.com/darroyo606/ExamDarlingArr/assets/55005126/03c0b8b1-bb96-476f-87f8-121ddb0b4a56)


Una vez obtenida esta información he creado un nuevo archivo main2.py para poder continuar con la extracción de los datos de los productos
Con el formato JSON obtenido de la página sabemos como se llama cada una de las descripciones del productos que deseamos visualizar,
el resultado de esto es el siguiente:
![image](https://github.com/darroyo606/ExamDarlingArr/assets/55005126/20e44213-dc15-4b96-88ed-123f50acedad)

Para estos pasos es importante aclarar que nuestro Requirements.txt ya contiene lo siguiente:
requests==2.31.0

# Insert Base de datos se crea un archivo mongodb.py y un archivo .env
En el archivo .env se encuentra:


MONGO_USER=tu usuario
MONGO_PASSWORD=tu contraseña

La respuesta que tenemos si se conecta de forma adecuada es la siguiente:
![image](https://github.com/darroyo606/ExamDarlingArr/assets/55005126/b538b2cf-2120-4e1e-aaa8-c40b32b26913)


# Creamos un archivo deprati_data.py

Aqui realizaremos nuestro desarrollo para que los datos obtenidos se guarden en la base de datos llamada DarExam y en la tabla productos
![image](https://github.com/darroyo606/ExamDarlingArr/assets/55005126/78626430-a359-44a2-be01-52f2ca69e0c5)






