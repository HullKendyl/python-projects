enterTodoPrompt = "Enter a TODO: "
doneCreatingTodos = "Are you finished creating TODOs? "
userActionPrompt = "Type add, show, or exit: "

todos = []

while True:
    user_action = input(userActionPrompt)

    match user_action:
        case 'add':
            todo = input(enterTodoPrompt)
            todos.append(todo)
        case 'show':
            print("Current TODOS - ", todos)
        case 'exit':
            break

print('Bye!')