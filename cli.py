from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It's is {now}")


while True:
    user_action = input("Type add, show, edit, delete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            # item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Enter a todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print('Your command is not valid.')

    elif user_action.startswith('delete'):
        number = int(input("Number of the todo to delete?: "))
        number -= 1

        todos = get_todos()

        todo_to_remove = todos[number].strip('\n')
        todos.pop(number)

        write_todos(todos)

        print(f"Todo-{todo_to_remove} was removed from the list.")

    elif user_action.startswith('exit'):
        break
    else:
        print("Are you kidding?")

print("See you!")
