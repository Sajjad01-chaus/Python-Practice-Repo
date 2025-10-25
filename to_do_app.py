import json
class ToDoApp:
    def __init__(self):
        self.tasks=[]
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks=json.load(file)
                print("These are the Tasks:")
                for i, task in enumerate(self.tasks,start=1):
                    status= "Done" if task['done'] else "Not Done"
                    print(f"{i}. {task['task']} - {status}\n")
                    print("--------------------------------")                             
        except FileNotFoundError:
            print("No tasks found")
            self.tasks=[]
    def add_task(self):
        task= input("Enter your task:")
        self.tasks.append({"task":task, "done":False})
        self.save_tasks()
        print("Task added successfully")

    def delete_ask(self):
        pass

    def update_task(self):
        pass

    def save_tasks(self):
        pass

    def tasks_list(self):
        while True:
            print("1. Add Task")
            print("2. Delete Task")
            print("3. Update Task")
            print("4. Save Tasks")
            print("5. Exit")
            choice= int(input("Enter your choice: "))
            if choice ==1:
                self.add_task()
            elif choice ==2:
                self.delete_task()
            elif choice ==3:
                self.update_task()
            elif choice ==4:
                self.save_tasks()
            elif choice ==5:
                break
            else:
                print("Invalid choice")

if __name__== "__main__":
    app= ToDoApp()
    app.tasks_list()




            

                    


        
