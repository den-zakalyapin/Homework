import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = r"[,.=\!\?;:\s-]+"

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    text = f.read().lower()
                    text = re.sub(punctuation, " ", text)
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"File not found: {file_name}")
                all_words[file_name] = []
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
                all_words[file_name] = []

        return all_words

    def find(self, word):
        found_positions = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            try:
                first_index = words.index(word.lower())
                found_positions[file_name] = first_index + 1
            except ValueError:
                pass

        return found_positions

    def count(self, word):
        word_counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0: # Only add if exists
                word_counts[file_name] = count
        return word_counts

#Example usage
with open("test_file.txt", "w", encoding="utf-8") as f:
  f.write("It's a TEXT for task, найти везде! Используйте - его для самопроверки. Успехов в решении задачи! TEXT text tEXT")
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))