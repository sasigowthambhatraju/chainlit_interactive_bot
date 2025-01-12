Chainlit Interactive Bot

Hello There👋🏻. Welcome to Chainlit Interactive Bot application repo.

What is Chainlit Interactive Bot?
This is a Python-based Chat Code Interpreter application that uses OpenAI's GPT-3.5-turbo API and Chainlit for the UI. This application can interpret code from chat messages or prompt given in the UI as a regular gpt companion, answer basic and general questions related to any topic, and handle data analysis tasks such as tasks or questions related to the csv which got uploaded in the UI.

How it works?
To start the application and to see how it workd first fork/ clone this project/ repository or download using the download as a zip option into your local machine.
Then the next steps involves the developer to do the following
1. Create a new virtual environment for this specific project then install all the required libraries from requirements.txt in the directory you are currently working on
2. Get your own OpenAI API Key from https://platform.openai.com/api-keys and paste that inside api_key variable present inside the config.yaml file
3. Now the fun part begins, to start the application in your local use the following command in the Terminal -> chainlit run app.py
4. As the program starts exicuting you'll see localhost url click on that or chainlit will directly take you to that url in the default browser of your choice, now you can chit chat with the bot related to any topic or upload a csv and asks questions related to the uploaded file, which is nothing but handling data analytics queries/ tasks.
![Screenshot 2025-01-12 013807](https://github.com/user-attachments/assets/9aebb910-4ea2-49b1-ae3a-23c5466d822f)

Note:
1. Do not forget to get your own OpenAI API Key from your OpenAI account and paste that inside config.yaml file
2. Do not start the application without installing all the libraries from requirements.txt in your venv
3. If there are errors try to check the path or directory
4. Use Python 3.8+ version for this project.
