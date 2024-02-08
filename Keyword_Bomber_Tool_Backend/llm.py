import google.generativeai as genai



async def generate_response(user_prompt, model, open_ai_api_key):

    genai.configure(api_key=open_ai_api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    try:
        response = model.generate_content(user_prompt)

        response = response.text
        
        return response


    except Exception as e:

        print(f"Response generation exception after max retries: {e}")
        return None

