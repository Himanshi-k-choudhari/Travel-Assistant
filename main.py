from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
print("Hello i am AMII your personal tracvel assistant !")
input1 = input("Ask me anything ....")
interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=input1
)
print(interaction.output_text)
print("thank you for using me!!")