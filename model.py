class TodoItem:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        return f"{self.description} ({'complete' if self.completed else 'incomplete'})"

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, description):
        self.items.append(TodoItem(description))

    def remove_item(self, index):
        del self.items[index]

    def mark_complete(self, index):
        self.items[index].completed = True

    def mark_incomplete(self, index):
        self.items[index].completed = False
