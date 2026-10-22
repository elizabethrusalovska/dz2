import datetime
import random
import text_tools

texts = [
    "Я вивчаю прикладну лінгвістику.",
    "Програмування допомагає працювати з мовою.",
    "Python має багато корисних модулів.",
]

text = random.choice(texts)
today = datetime.date.today()

print("Дата:", today.strftime("%d.%m.%Y"))
print("Випадкове речення:", text)
print("Кількість слів:", text_tools.count_words(text))
print("Кількість голосних:", text_tools.count_vowels(text))