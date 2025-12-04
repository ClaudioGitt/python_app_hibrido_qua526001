import flet as ft

class Task(ft.Column):
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Edit TO-DO",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            tooltip="Delete TO-DO",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Update TO-DO", # tooltip sempre é stringzinha.
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view,self.edit_view]

    def edit_clicked(self,e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self,e):
        self.display_task = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)

class TodoApp(ft.Column):
    # herança do ft.Colunm
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="O que precisa ser feito?", expand=True)
        self.tasks = ft.Column()
        self.width = 300
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked),
                ],
            ),
            self.tasks,
        ]

    def add_clicked(self,e):
        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

def main(page: ft.Page):
    page.title = "TO-DO APP"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    todo = TodoApp()
    titulo = ft.Text("Use uma URL", color=ft.Colors.ON_SURFACE,
                     size=20, weight=ft.FontWeight.BOLD)

    page.add(
        titulo,
        todo
    )
ft.app(main)