import boto3

#Crear cliente para dynamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
tabla = dynamodb.Table('tabla-santiago-giraldo')

#Leer un elemento de la tabla
response = tabla.get_item(Key={'id': '2'})
print(response['Item'])

#Leer todos los elementos de la tabla
response = tabla.scan()
print(response['Items'])

#Insertar un registro en la tabla
item = {
    "id": "3",
    "nombre": "Maria",
    "telefono": "3002342100"
} 

response = tabla.put_item(Item=item)
response = tabla.get_item(Key={'id': '3'})
print(response['Item'])

#Crear un elemento (realizado por el profesor)
tabla.put_item(Item={
    "id": "4",
    "nombre": "Juan Esteban",
    "ciudad": "Medellin",
    "edad": 35
})

# Realizar la actualización(update)
response = tabla.update_item(
    Key={
        'id': '4'  
    },
    UpdateExpression='SET edad = :val1',  # Expresión de actualización
    ExpressionAttributeValues={
        ':val1': 30  # Nuevo valor para atributo2
    }
)

response = tabla.get_item(Key={'id': '4'})

# Imprimir la respuesta
print(response['Item'])