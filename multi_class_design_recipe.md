# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary -> Notebook | -> Diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries -> | -> DiaryEntry

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed | -> Diary

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary -> Notebook | -> TodoList

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries -> | -> DiaryEntry



## 2. Design the Class System

┌────────────────────────────┐
│ Diary                      │
│                            │
│                            │
│ - init(self)
- reading_time                   │
└───────────┬────────────────┘

┌────────────────────────────┐
│ DiaryEntry                      │
│                            │
│ - init(contents, numbers)                │
│ - add(diaryentry)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘

┌────────────────────────────┐
│ TodoList                     │
│                            │
│ - init(self)
    list                 │
│ - add(todo)               │
│          │
└───────────┬────────────────┘

```python
class Diary:
    # User-facing properties:
    #   entries: string representing the diary entry

    def __init__(self, entry):
        pass # No code here yet


    def reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm: integer
        #   minutes: integer
        # Returns:
        #   Diaries entires to read based on the time I have and my reading speed
        pass # No code here yet

class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, contents, phone_number):
        # Parameters:
        #   contents: string
        #   phone_number: integer
        # Side-effects:
        #   Sets the content and mobile number
        pass # No code here yet

    def add(self, entry):
        # Adds a an entry to the diary 
        # Returns:
        #   Nothing
        pass # No code here yet

    def show_diary_content(self)
        # Returns:
        #   A list of all content in the diary
    def show_numbers(self)
        # Returns:
        #   A list of all phone numbers in all diary entries

class TodoList():
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self):
        # Parameters:
        #   contents: string
        #   phone_number: integer
        # Side-effects:
        #   Sets the content and mobile number
        pass # No code here yet

    def add(self, task):
        # Adds a task to the todo list 
        # Returns:
        #   Nothing
        pass # No code here yet

## 3. Create Examples as Integration Tests

## 4. Create Examples as Unit Tests