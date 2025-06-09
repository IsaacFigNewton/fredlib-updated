class TextPreprocessor:
    def __init__(self, text:str):
        self.text = text
        self.processed_text = None

    def preprocess_text(self):
        # Original text cleanup
        new_text = self.text.replace("-", " ")\
                    .replace("#", " ")\
                    .replace(chr(96), "'")

        # Dictionary of replacements
        replacements = {
            "'nt ": " not ",
            "'ve ": " have ",
            " what's ": " what is ",
            "What's ": "What is ",
            " where's ": " where is ",
            "Where's ": "Where is ",
            " how's ": " how is ",
            "How's ": "How is ",
            " he's ": " he is ",
            " she's ": " she is ",
            " it's ": " it is ",
            "He's ": "He is ",
            "She's ": "She is ",
            "It's ": "It is ",
            "'d ": " had ",
            "'ll ": " will ",
            "'m ": " am ",
            " ma'am ": " madam ",
            " o'clock ": " of the clock ",
            " 're ": " are ",
            " y'all ": " you all "
        }

        # Apply replacements
        for old, new in replacements.items():
            new_text = new_text.replace(old, new)

        new_text = new_text.strip()
        if new_text[len(new_text)-1]!='.':
            new_text = new_text + "."

        self.processed_text = new_text