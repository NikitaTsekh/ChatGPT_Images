import openai
from apikey import OPENAI_API_KEY 


#Image generation
openai.api_key = OPENAI_API_KEY



# response = openai.Image.create(
#   prompt="2 Dancing gorillas on the boat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']

# print(image_url)

#Image variations


response = openai.Image.create_variation(
  image=open("Me.png", "rb"),
  n=5,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(response['data'])


print(image_url)