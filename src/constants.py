class Constants:
    SYSTEM_MESSAGE_CSV = "You are an assistant that answers questions based on user input. you should answer to general questions even if the data is not related to the csv data."
    SYSTEM_MESSAGE_GENERAL = "You are an assistant that answers questions based on user input."
    USER_MESSAGE_CSV = "Answer the following question based on this csv data:\n\n{data_json}\n\nQuestion: {user_message}"
    WELCOME_MESSAGE = "Hello there, Welcome to My App Upload a csv and ask any questions related to the data"
    SYS_MSG = "Please upload a csv file to begin!"