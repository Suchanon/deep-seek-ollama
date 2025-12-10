import ollama

MODEL = "deepseek-coder-v2"
messages = []

print(f"Chatting with {MODEL} (type 'quit' to exit)")
print("-" * 30)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['quit', 'exit']:
        break

    # Add user message to history
    messages.append({'role': 'user', 'content': user_input})

    print("DeepSeek:", end=" ", flush=True)
    
    # Stream response
    full_response = ""
    stream = ollama.chat(model=MODEL, messages=messages, stream=True)
    
    for chunk in stream:
        content = chunk['message']['content']
        print(content, end='', flush=True)
        full_response += content

    # Add assistant response to history so it "remembers"
    messages.append({'role': 'assistant', 'content': full_response})
    print()
