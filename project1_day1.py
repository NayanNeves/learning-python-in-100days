# Day 01 — Variáveis, Input e f-strings

# Versão 1 — concatenação simples
Name = input("What is your name? ")
city = input("Where are you from? ")
length = str(len(Name))
print("Hello" + " " + Name)
print("You live in" + " " + city)
print("And your name has" + " " + length + " letters")

# Versão 2 — com f-string (modo moderno)
Name = input("What is your name? ")
city = input("Where are you from? ")
length = len(Name)
print(f"Hello, {Name}! You live in {city} and your name has {length} letters.")
