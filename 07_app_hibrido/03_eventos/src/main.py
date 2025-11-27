import flet as ft


def main(page: ft.Page):
    # Criando funções de evento.
    def exibir_nome(e): # o e no parametro, é um evento
        nome_saida.value=nome.value
        nome_saida.update()
    # Alterando as propriedades da página
    page.title = "App de manipulação de eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    # declaração de variáveis
    # captura de inputs
    nome =ft.TextField(label="Informe seu nome: ".strip().title(),border=20,bgcolor="green",on_submit=exibir_nome)
    # no caso do flet, precisa armazenar duas vezes
    nome_saida = ft.Text()
    page.add(
        # safe area, é a área que fica no topo
        ft.SafeArea( # um safearea por projeto.
            ft.Container(
                ft.Text("Trabalhando com eventos",size=30,weight="bold"),
                alignment=ft.alignment.center
            ),
            expand=True,
        ),
        nome,
        ft.ElevatedButton("Inserir",on_click = exibir_nome),
        nome_saida        
        )


ft.app(main)
""" etanol o valor precisa ser no maximo 70% do valor da gasolina, se for menos que 70% é gasolina"""
