# AI-Youtube-Chrome-Extension
This is Chrome extension that leverage the power of AI to generate a summary of any YouTube Videos out there, giving people a clear and consise idea on what the video is about. User can simply input a YouTube URL and press generate. By utilising Langchain and the OpenAI API under the hood, GPT-4 is used to understand the context of the video and generate a summary of the video.
 
# Initializing the project
First, run ``` pip install -r requirements.txt ``` to install all the required dependencies. Second, enter your OpenAI API key into the OPENAI_API_KEY variable in an .env file. Third, load the folder into the chrome extension developer testing site. Lastly, run ``` flask run --port=8000 ``` to initialize the backend. Afterwards, you will be able to use the chrome extension.
