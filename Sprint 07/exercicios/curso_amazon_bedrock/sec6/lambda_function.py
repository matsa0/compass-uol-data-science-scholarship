import json
import boto3

bedrock_client = boto3.client('bedrock-runtime')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    prompt = event['prompt']
    print(prompt)
    
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    body_claude =  { 
        "anthropic_version": "bedrock-2023-05-31",
        "messages": messages,
        "temperature": 0.9,
        "top_p": 0.9,
        "top_k": 250,
        "max_tokens": 100,
    }

    response = bedrock_client.invoke_model(
        contentType='application/json',
        accept='application/json',
        modelId='anthropic.claude-3-haiku-20240307-v1:0',
        body = json.dumps(body_claude)
    )
    #print(response)


    response_body = json.loads(response['body'].read())
    print(response_body)

    text = response_body['content'][0]['text']

    return {
        'statusCode': 200,
        'body': json.dumps(text) 
    }
