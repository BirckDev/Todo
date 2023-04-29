class TodoListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.show_list(self.model.items)
            command = self.view.get_input("Enter command (a to add, r to remove, c to mark complete, i to mark incomplete, q to quit): ")
            if command == "a":
                description = self.view.get_input("Enter description: ")
                self.model.add_item(description)
            elif command == "r":
                index = int(self.view.get_input("Enter index of item to remove: ")) - 1
                self.model.remove_item(index)
            elif command == "c":
                index = int(self.view.get_input("Enter index of item to mark complete: ")) - 1
                self.model.mark_complete(index)
            elif command == "i":
                index = int(self.view.get_input("Enter index of item to mark incomplete: ")) - 1
                self.model.mark_incomplete(index)
            elif command == "q":
                break
