enterTodoPrompt = "Enter a TODO: "
doneCreatingTodos = "Are you finished creating TODOs? "
userActionPrompt = "Type add, show, edit, complete, or exit: "

todos = []

while True:

    user_action = input(userActionPrompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input(enterTodoPrompt)
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                item = item.title()
                index = index + 1
                print(index, "-", item)
        case 'edit':
            print(todos)
            number = int(input("Enter the number of the todo to edit: "))
            # TODO - If a user enters something other than a number, share it is an unknown command and prompt again
            existing_todo = todos[number - 1]
            edited_todo = input("Enter the edit you'd like to make to [" + existing_todo + "]: ")
            todos[number - 1] = edited_todo
            print("You've successfully updated [{existing_todo}] to [{edited_todo}]")
            print(todos)
        case 'complete':
            completed_todo = int(input("Enter the number of todo you'd like to complete"))
            todos.pop(completed_todo - 1)
        case 'exit':
            break
        case _:
            print("You entered an unknown command")

print('Bye!')