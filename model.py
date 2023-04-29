class TodoItem:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        return f"{self.description} ({'complete' if self.completed else 'incomplete'})"
