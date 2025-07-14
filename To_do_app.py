class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append({'task':task,'completed':False})

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = 'completed' if task ['completed'] else 'not completed'
            print(f'{i+1}. {task["task"]} - {status}')

    def mark_completed (self,task_number):
        try:
            task_number =int(task_number)-1
            if task_number >= 0 and task_number < len(self.tasks):
                self.tasks[task_number]['completed']= True
            else:
                print('invalid task number')

        except ValueError:
            print('invalid input')

    def delete_task(self,task_number):
        try:
            task_number = int(task_number)-1
            if task_number >= 0 and task_number < len(self.tasks):
                del self.tasks[task_number]

            else:
                print('invalid task number')

        except ValueError:
            print('invalid input.')

def main():
        app = ToDoApp()
        while True:
            print('1. Add task')
            print('2.View tasks')
            print('3. mark task as completed')
            print('4.delete task')
            print('5.quit')
            choice = input('choose an option: ')
            if choice =='1':
                task = input('Enter task')
                app.add_task(task)

            elif choice == '2':
                app.view_tasks()

            elif choice == '3':
                task_number = input('Enter task number: ')
                app.mark_completed(task_number)
            
            elif choice == '4':
                task_number=input('enter task number: ')
                app.delete_task(task_number)

            elif choice == '5':
                break

            else:
                print('Invalid option.')

if __name__ =='__main__':
    main()