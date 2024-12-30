from googletrans import Translator

def translate_text(text, src='auto', dest='fr'):
    try:
        # Validate input
        if not text or text.strip() == "":
            raise ValueError("Input text cannot be None or empty.")
        
        #Else If User entered any text for translation
        translator = Translator()

        # Translate text
        result = translator.translate(text, src=src, dest=dest)

        print(f"Translated Text: {result.text}")
        #return result.text
        return result.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
#text_to_translate = input("Enter text to translate: ").strip()
#translate_text(text_to_translate, src="en", dest="fr")  # Translate from English to French
