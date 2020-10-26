import PySimpleGUI as Sg

Sg.theme("Material1")
font_name = 'Courier'
font_size = 14


def add_task(value):
    task = value['task_name']
    if task != "":
        if values[0]:
            todolist.insert(0, task+" -Top")
        elif values[1]:
            todolist.insert(len(todolist), task+" -Low")

    print(values[0])
    window.FindElement('task_name').Update(value="")
    window.FindElement('todolist').Update(values=todolist)
    window.FindElement('add_save').Update('Add')


def edit_tasks(value):
    try:
        edit_val = value['todolist'][0]
        window.FindElement('task_name').Update(value=edit_val)
        todolist.remove(edit_val)
        window.FindElement('add_save').Update('Save')
    except:
        pass


def delete_tasks(value):
    try:
        delete_val = value['todolist'][0]
        todolist.remove(delete_val)
        window.FindElement('todolist').Update(values=todolist)
    except:
        pass


radio_choices = ["Top", "Normal", "Low"]
radio = [[Sg.Radio(text, 1), ] for text in radio_choices]

layout = [
    [
        Sg.Text("Enter the task", font=(font_name, font_size)),
        Sg.InputText("", font=(font_name, font_size), size=(20, 1), border_width=0, key="task_name"),
    ],

    [
        Sg.Text("Priority      ", font=(font_name, font_size)),
        Sg.Radio("Top", 1),
        Sg.Radio("Low", 1, default=True)
    ],

    [
        Sg.Button("Add", font=(font_name, font_size), border_width=0, key="add_save"),
        Sg.Button("Edit", font=(font_name, font_size), border_width=0),
        Sg.Button("Delete", font=(font_name, font_size), border_width=0),
    ],

    [
        Sg.Listbox(values=[], size=(40, 10), font=(font_name, font_size), key='todolist')
    ]

]

todolist = []
radio_choices = ["Top", "Normal", "Low"]

window = Sg.Window("Week1", layout)

while True:
    event, values = window.Read()
    if event == 'add_save':
        add_task(values)
    elif event == 'Edit':
        edit_tasks(values)
    elif event == 'Delete':
        delete_tasks(values)
    else:
        break

window.Close()
