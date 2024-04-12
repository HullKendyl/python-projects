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
            print(todos)
            number = int(input("Enter the number of the todo to edit: "))
            # TODO - If a user enters something other than a number, share it is an unknown command and prompt again
            existing_todo = todos[number - 1]
            edited_todo = input("Enter the edit you'd like to make to [" + existing_todo + "]: ")
            todos[number - 1] = edited_todo
            print(f"You've successfully updated [{existing_todo}] to [{edited_todo}]")
            print(todos)
        case 'exit':
            break
        case _:
            print("You entered an unknown command")

print('Bye!')