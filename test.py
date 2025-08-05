#JRDFheRffUgmLmv-DK-5-vmNLfDVg1XpOan8bIFpZgt0IyuPU499Cpjx0nmAOpNzRKdlRn7O30bqeiMZmQ1cbw==

import os
from dotenv import load_dotenv
from llama_index.llms.groq import Groq
from llama_index.core.base.llms.types import ChatMessage, MessageRole

# Load environment variables from .env file
load_dotenv()

def test_groq_llm():
    """Test the Groq LLM with a simple query"""
    
    # Get API key from environment
    groq_api_key = os.getenv("GROQ_API_KEY")
    
    if not groq_api_key:
        print("❌ Error: GROQ_API_KEY not found in environment variables")
        print("Make sure you have GROQ_API_KEY in your .env file")
        return
    
    try:
        # Initialize the LLM (same as in your main code)
        llm = Groq(
            model="moonshotai/kimi-k2-instruct",
            api_key=groq_api_key,
            temperature=0.4,
            max_tokens=1000
        )
        
        print("✅ LLM initialized successfully")
        
        # Test 1: Simple completion
        print("\n--- Test 1: Simple Completion ---")
        test_prompt = "What is the capital of France? Give a brief answer."
        response = llm.complete(test_prompt)
        print(f"Prompt: {test_prompt}")
        print(f"Response: {response.text}")
        
        # Test 2: Chat format
        print("\n--- Test 2: Chat Format ---")
        messages = [
            ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant."),
            ChatMessage(role=MessageRole.USER, content="Explain what Python is in one sentence.")
        ]
        chat_response = llm.chat(messages)
        print(f"Chat Response: {chat_response.message.content}")
        
        # Test 3: Streaming (optional)
        print("\n--- Test 3: Streaming Response ---")
        stream_prompt = "Count from 1 to 5 and explain each number briefly."
        print(f"Prompt: {stream_prompt}")
        print("Streaming Response: ", end="")
        
        streaming_response = llm.stream_complete(stream_prompt)
        for chunk in streaming_response:
            print(chunk.delta, end="", flush=True)
        print("\n")
        
        print("✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Error testing LLM: {e}")
        print("Check your API key and internet connection")

if __name__ == "__main__":
    test_groq_llm()