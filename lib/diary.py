class Diary():
    def __init__(self, entry):
        self.entry = entry
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)
        
    def count_words(self):
        length_of_diary = 0
        for char in self.entries:
            length_of_diary += char.count_words()
        return length_of_diary

    def reading_time(self, wpm):
        return len(self.entry.split()) / wpm
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_to_read = wpm * minutes
        for entry in self.entries:
            if entry.count_words() <= words_to_read:
                return self.entries
