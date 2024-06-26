import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')  

#Eliminar la tabla
response = dynamodb.delete_table(
    TableName='tabla-santiago-giraldo-2'
)

# #Crear la tabla
# response = dynamodb.create_table(
#      TableName='tabla-santiago-giraldo-2',
#      KeySchema=[
#          {
#              'AttributeName': 'id',
#              'KeyType': 'HASH'  
#          }
#      ],
#      AttributeDefinitions=[
#          {
#              'AttributeName': 'id',
#              'AttributeType': 'S'  
#          }
#      ],
#      BillingMode='PAY_PER_REQUEST'  # Configurar capacidad bajo demanda
# )