import webvtt
from googletrans import Translator

# Define the input and output file paths
input_file_path = input('Enter the name and address of your file along with its extension(.vtt): ')
output_file_path = input('Choose a name for the output file along with its extension(.vtt): ')

# Load the input webvtt file
captions = webvtt.read(input_file_path)

# Create a translator object
translator = Translator()

# Loop through each caption in the input file and translate its text
for caption in captions:
    original_text = caption.text
    translated_text = translator.translate(original_text, dest='fa').text
    caption.text = translated_text

# Save the translated captions to the output file
captions.save(output_file_path)
