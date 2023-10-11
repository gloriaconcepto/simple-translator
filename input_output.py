from translate import Translator
try:
    translator=Translator(to_lang='French')
    # Open the existing file for reading
    with open('read.txt', 'r') as input_file:
        text = input_file.read()

    # Create a new file and write the text
    with open('output.txt', 'w') as output_file:
        translation = translator.translate(text)
        output_file.write(translation)

    print("File copied successfully.")

except FileNotFoundError:
    print("The input file was not found.")
except IOError as e:
    print(f"An error occurred while copying the file: {e}")