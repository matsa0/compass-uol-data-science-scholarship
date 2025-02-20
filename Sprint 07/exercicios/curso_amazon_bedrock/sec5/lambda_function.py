import json
import boto3
import base64
import datetime

print(boto3.__version__)

# criando uma conexão com o bedrock e o s3
bedrock_client = boto3.client('bedrock-runtime')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    # armazenando o prompt
    prompt = event['prompt']
    print(prompt)

    # corpo da requisição
    body = json.dumps({
        "textToImageParams": {
            "text": prompt
        },
        "taskType": "TEXT_IMAGE",
        "imageGenerationConfig": {
            "cfgScale": 8,
            "seed": 42,
            "quality": "standard",
            "width": 512,
            "height": 512,
            "numberOfImages": 1
        }
    })

    # criando uma requisição para acessar o Bedrock
    response_bedrock = bedrock_client.invoke_model(
        contentType='application/json',
        accept='application/json',
        modelId='amazon.titan-image-generator-v2:0',
        body = body
    )
    #print(response_bedrock)


    # Processando ao corpo resposta (StreamingBody)
    response_body = json.loads(response_bedrock['body'].read())
    #print(response_body)

    # extraindo a imagem codificada em base64
    base64_image = response_body['images'][0]
    response_bedrock_image = base64.b64decode(base64_image)
    #print(response_bedrock_image)    

    # armazenando a imagem no s3
    image_name = 'imageName' + datetime.datetime.today().strftime('%Y-%M-%D-%M-%S')

    response = s3_client.put_object(
        Bucket='movieposterdesign-bckt',
        Body=response_bedrock_image,
        Key=image_name,
    )

    # gerando pre-signed URL
    generate_presign_url = s3_client.generate_presigned_url(
        'get_object',
        Params = {
            'Bucket': 'movieposterdesign',
            'Key': image_name
        },
        ExpiresIn=3600
    )
    print(generate_presign_url)

    return {
        'statusCode': 200,
        'body': generate_presign_url
    }
    

