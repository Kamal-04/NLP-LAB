from langdetect import detect

sentence = "Hallo Deutschland! Willkommen bei NLP"
print(detect(sentence))

from langdetect import DetectorFactory
DetectorFactory.seed=0

from translate import Translator
translator = Translator(from_lang="en",to_lang="de")

translation = translator.translate("Hi Germany! Welcome to NLP")
print(translation)