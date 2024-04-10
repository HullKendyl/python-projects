enterTodoPrompt = "Enter a TODO: "

todos = []

while True:
    todo = input(enterTodoPrompt)
    todos.append(todo)

print("Current TODOS - ", todos)


