class TodoListView:
    def show_list(self, items):
        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")

    def get_input(self, prompt):
        return input(prompt)
