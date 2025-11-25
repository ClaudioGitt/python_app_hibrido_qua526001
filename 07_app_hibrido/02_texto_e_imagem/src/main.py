import flet as ft


def main(page: ft.Page):
    
    page.add(
        ft.SafeArea( # safearea é para cabeçalhos por exemplo
            ft.Container(
                # ft.Text é o mesmo que print em python
                ft.Text(f"Chrono cross",color="light-blue",size=30,weight="bold"),
                alignment=ft.alignment.center
            )
        ),
        ft.Container(
            ft.Image(
            src="maxresdefault.jpg",
            fit=ft.ImageFit.CONTAIN,
            width=800,
            height=600,
            opacity=0.6,
            error_content=ft.Text("Não foi possível carregar a imagem")
        ),
        alignment=ft.alignment.center
        )
    )
ft.app(main)
