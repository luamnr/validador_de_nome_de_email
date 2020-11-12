import Levenshtein
import sys

email_examples = open("example.txt", "r")
valid_domains = open("dominio_validos.csv", "r")
valid_domains_set = set()
email_examples_set = set()
correct_email = str()
result = open("result.txt", "a")
# Setando o out do terminal para a var result, que é um arquivo com o parâmetro "append"
sys.stdout = result

# Caso trocar arquivo de emails inválidos ou domínios validos mudar os indexes
for word in valid_domains:
    valid_domains_set.add(word[:-1])

for word in email_examples:
    email_examples_set.add(word[4:-3])

for i in email_examples_set:
    if i.split("@")[1][0] == "g":
        correct_email = i.split("@")[0] + "@gmail.com"
        print(f"EMAIL ORIGINAL;{i};SUGESTÃO;{correct_email}")

    elif i.split("@")[1][0] == "y":
        correct_email = i.split("@")[0] + "@yahoo.com.br"
        print(f"EMAIL ORIGINAL;{i};SUGESTÃO;{correct_email}")

    elif i.split("@")[1][0] == "h":
        correct_email = i.split("@")[0] + "@hotmail.com"
        print(f"EMAIL ORIGINAL;{i};SUGESTÃO;{correct_email}")

    else:
        for k in valid_domains_set:

            if Levenshtein.distance(i.split("@")[1], k) < 3:
                correct_email = i.split("@")[0] + "@" + k
                print(f"EMAIL ORIGINAL;{i};SUGESTÃO;{correct_email}")
