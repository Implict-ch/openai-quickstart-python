import os
import openai
def gpt35_get_response(content):
  openai.api_key = "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"
  # gpt-3.5-turbo
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=content,
    temperature=0.4,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response['choices'][0]['text']



f = open('./src/test.txt' , 'r' , encoding= "utf-8")
raw = f.read()
prompt = raw + ",\n请把上述python代码转换成java给我,注意保留代码内的注释"
result = gpt35_get_response(prompt)
print(result)

