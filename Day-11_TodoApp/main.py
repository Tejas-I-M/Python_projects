import os
import json
class TaskManager:
    def __init__(self, file_name='task.json'):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(script_dir, file_name)
        self.tasks = self.load_tasks()
    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r") as f:
            return json.load(f)
    def save_tasks(self):
        with open(self.file_name,"w") as f:
            json.dump(self.tasks,f,indent=4)
    def add_task(self,title):
        task={  "id": len(self.tasks)+1,
                "title":title,
                "completed":False
                }
        self.tasks.append(task)
        self.save_tasks()
        print("task added")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks appended")
            return
        for task in self.tasks:
            status = '👍' if task['completed'] else '👎'
            print(f"{task['id']}. {task['title']} {status}")
    def mark_complete(self,task_id):
        for task in self.tasks:
            if task['id'] ==task_id:
                task['completed'] =True
                self.save_tasks()
                print("Task marked as complete")
                return
        print("task not found")
    def delete_task(self,task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("task deleted")
                return
        print("task not found!!")

tm = TaskManager()
while True:
    print("\n1.ADD 2.VIEW 3.COMPLETE 4.DELETE 5.EXIT")
    choice = input("enter the choice number: ")
    if choice == "1":
        name = input("enter the task name: ")
        tm.add_task(name)
    elif choice == "2":
        tm.view_tasks()
    elif choice  == "3":
        id = int(input("enter the task id: "))
        tm.mark_complete(id)
    elif choice =="4":
        id = int(input("enter the task id: "))
        tm.delete_task(id)
    elif choice == "5":
        break
    else:
        print("invalid option")



