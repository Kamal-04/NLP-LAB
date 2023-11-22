
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

conversation = "Hello! How are you?\nI'm doing well,thanks! What about you?"

tokens=word_tokenize(conversation.lower())
stop_words=set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

from nltk.chat.util import Chat, reflections

pairs = [
    ('(hi|hello|hey)',['Hello!','Hi there!','Hey!']),
    ('how are you',['I am doing well, thank you. How about you?']),
    ('(.*)',['I am just a chatbot, not capable of understanding that.']),
]

chatbot = Chat(pairs,reflections)

user_message = "HI, What can you do?"
reponse = chatbot.respond(user_message)
print(reponse)