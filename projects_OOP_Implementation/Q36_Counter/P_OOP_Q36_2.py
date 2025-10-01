class WordCounter:

    def __init__(self, text=None):

        self.result=""
        
        if text is None:

            text = input("Enter words: \n")

        self.words= [w for w in text.split(" ")]

    def Check(self):

        checked = []

        for word in self.words:

            if word not in checked:

                count = 0
                    
                for w in self.words:

                    if w== word:

                        count += 1

                if count > 1:

                    self.result += f"\n{word} appears {count} times\n"

                checked.append(word)

        if self.result == "":
            self.result = "No words are repeating"

    def __str__(self):
        self.Check()
        return self.result







