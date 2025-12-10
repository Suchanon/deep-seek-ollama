import ollama

# Initialize the model name
MODEL = "deepseek-coder-v2"

print(f"Connecting to {MODEL}...")

# Send a prompt to the model
response = ollama.chat(model=MODEL, messages=[
  {
    'role': 'user',
    'content': 'Write a Python function to calculate the Fibonacci sequence.',
  },
], stream=True)

print("\nDeepSeek Response:")
print("-" * 20)

# Process the streaming response
for chunk in response:
  print(chunk['message']['content'], end='', flush=True)

print("\n" + "-" * 20)
