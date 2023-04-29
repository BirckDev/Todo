from model import TodoList
from view import TodoListView
from controller import TodoListController

model = TodoList()
view = TodoListView()
controller = TodoListController(model, view)

controller.run()
