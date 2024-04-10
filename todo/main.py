enterTodoPrompt = "Enter a TODO: "
doneCreatingTodos = "Are you finished creating TODOs? "

todos = []

isDone = "No"

while isDone != "Yes":
    todo = input(enterTodoPrompt)
    todos.append(todo)
    print("Current TODOS - ", todos)
    isDone = input(doneCreatingTodos)
    isDone = isDone.capitalize()

