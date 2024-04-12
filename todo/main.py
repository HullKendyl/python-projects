enterTodoPrompt = "Enter a TODO: "
doneCreatingTodos = "Are you finished creating TODOs? "
userActionPrompt = "Type add, show, edit, or exit: "

todos = []

while True:

    user_action = input(userActionPrompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input(enterTodoPrompt)
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            print("Got it!")
        case 'exit':
            break
        case _:
            print("You entered an unknown command")

print('Bye!')