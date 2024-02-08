from Keyword_Bomber_Tool_Backend import bomber
import asyncio
import os
from dotenv import load_dotenv


#Set Your inputs
# input_keyword = "Marketing Automation"
# input_country = "US"

#Set your Open AI API Key

def keyword_analysis_function(input_keyword,input_country):

    # Load environment variables from the .env file
    load_dotenv()
    # Access the environment variable
    API_KEY = os.getenv("OPENAI_API_KEY")
    
    print("started...")
    #run
    result =  asyncio.run(bomber.get_keyword_data(input_keyword,input_country,API_KEY))

    print('ended...')
    
    return result