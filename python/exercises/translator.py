from googletrans import Translator

translator = Translator()

try:
    with open('./text.txt', 'r') as file:
        source = file.readlines()
except FileNotFoundError:
    print("The input file could not be found.")
    quit()

translation = translator.translate(source, dest='ja')

print("The input file says:")
print(translation[0].text)

try:
    with open('./text.txt', 'a') as file:
        file.write("\n" + translation[0].text)
except IOError:
    print("Could not write output to text.txt")
