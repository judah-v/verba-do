import ast
from openai import OpenAI
from .models import Task

setup = {"role": "system", "content": "You are trained to condense the items given to you into a python list object of tasks to be done in order of priority without numbers. Don't use a variable."}

commands = {
            'complete': 
                ["cross off", "strike off", "mark completed", "mark done", "mark finished", "finish task", "complete task", "show completed"],
            'complete_all':
                ["complete all", "complete list"],
            'delete': 
                ["remove task", "delete task", "remove item", "delete item"],
            'clear': 
                ["clear list", "delete all", "clear all", "reset list", "new list"],
            'reopen': 
                ["reopen task", "reopen item"],
            'reopen_all':
                ["reopen all"],
            'create': 
                ["add task", "create task", "new task", "add item", "create item", "new item"],

        }

def update_tasklist(request):
    user_prompt = request.POST['prompt'].lower()

    if user_prompt.split()[0] != "action":
        client = OpenAI(
        api_key="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")
        response = client.chat.completions.create(
            messages = [setup, {"role": "user", "content": user_prompt}],
            model="gpt-3.5-turbo",
        )
        try:
            tasks = ast.literal_eval(response.choices[0].message.content)
        except Exception as e:
            tasks= ['Voice command failed. Error in next item:', response.choices[0].message.content.strip()]

        for task in tasks:
            if len(request.user.task_set.filter(title=task)) == 0:
                new_task = Task(title=task, complete=False, owner=request.user)
                new_task.save()
        return tasks
    
    else:
        
        user_prompt = user_prompt.replace('.', '')
        command = ' '.join(user_prompt.split()[1:3])
        task_name = ' '.join(user_prompt.split()[3:])
        tasks = request.user.task_set.all()
        target_task = None
        for task in tasks:
            if task.title.lower() == task_name:
                target_task = task
                break

        if target_task:
            if command in commands['complete']:
                target_task.complete = True
                target_task.save() 
            elif command in commands['delete']:
                target_task.delete()
            elif command in commands['reopen']:
                target_task.complete = False
                target_task.save()
        elif command in commands['complete_all']:
            for task in tasks:
                task.complete = True
                task.save()
        elif command in commands['reopen_all']:
            for task in tasks:
                task.complete = False
                task.save()
        elif command in commands['clear']:
                for task in tasks:
                    task.delete()
        else:
            print(f'\n\n\nInvalid command: {user_prompt}\n\n\n')