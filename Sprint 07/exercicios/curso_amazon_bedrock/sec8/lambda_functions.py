import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('bedrock-runtime', region_name="us-east-1")
    model_id = "amazon.titan-embed-text-v2:0"
    input_text = "Hi! My name is Matheus. How are you?"

    native_request = {
        "inputText": input_text
    }
    request = json.dumps(native_request)

    response = client.invoke_model(
        modelId=model_id,
        body=request
    )

    model_response = json.loads(response["body"].read())

    embedding = model_response["embedding"]
    input_text_token_count = model_response["inputTextTokenCount"]

    print("\nInput:")
    print(input_text)
    print(f"\nNúmero de tokens do input: {input_text_token_count}")
    print(f"\nTamanho do embedding gerado: {len(embedding)}")
    print("Embedding: \n")
    print(embedding)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Sucesso')
    }
