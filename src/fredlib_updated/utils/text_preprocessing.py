class TextPreprocessor:
    def __init__(self, text=None):
        self.text = self.preprocessText(text)

    def preprocessText(self, text):
        # Original text cleanup
        nt = text.replace("-", " ")\
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
            nt = nt.replace(old, new)

        nt = nt.strip()
        if nt[len(nt)-1]!='.':
            nt = nt + "."

        return nt