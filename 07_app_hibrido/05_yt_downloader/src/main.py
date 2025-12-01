import flet as ft
from pytubefix import YouTube

import os
import threading

def main(page: ft.Page):
    page.title = 'Youtube Downloader'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = 'assets/youtube.png'
    page.window.resizable = False
    
    # cria as pastas caso não existam
    caminho_videos = 'videos'
    caminho_audios = 'audios'

    os.makedirs(caminho_videos, exist_ok = True)
    os.makedirs(caminho_audios, exist_ok = True)

    # Componentes da interface gráfica
    titulo = ft.Text("Use uma URL", color=ft.Colors.BLACK12,
                     size=20, weight=ft.FontWeight.BOLD)
    url = ft.TextField(
        label='Cole a URL do vídeo do Youtube aqui',
        width=400,
        border_radius=10
    )
    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets", "logo.png")
    logo_cabecalho = ft.Image(src=logo_path, width=300, height=200)

    # componente para mostrar informações do vídeo
    video_info = ft.Container(
        content=ft.Column([]),
        visible=False,
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        width=400
    )
    
    # barra de progresso
    progress_bar = ft.ProgressBar(
        visible=False,
        width=400,
        color=ft.Colors.BLUE_600,
        bgcolor=ft.Colors.BLUE_GREY_100
    )

    # texto de status
    status_text = ft.Text(
        "",
        color=ft.Colors.BLACK,
        size=14,
        text_align=ft.TextAlign.CENTER
    )

    # Mostra as informações de vídeo na interface
    def mostrar_info_videos(yt):
        try:
            # TODO construir mostrar_info_videos
            video_info.content.controls.extend(
                [
                    ft.Text(f"Título: {yt.title}", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Canal: {yt.author}", size=12),
                    ft.Text(f"Duração: {yt.length / 60}:{yt.length % 60}", size=12),
                    ft.Text(f"Visualização: {yt.views:,}", size=12),
                ]
            )
            video_info.visible = True
            page.update()

        except Exception as e:
            status_text.value = f"Erro ao obter informações: {str(e)}."
            status_text.color = ft.Colors.RED
            page.update()
    # função para baixar vídeo
    def baixar_video(e):
        if not url.value.strip():
            status_text.value = "Por favor, insira uma URL váida."
            status_text.color = ft.Colors.ORANGE_200
            page.update()
        # outra função com multithread para cuidar de outra função
        # uma função dentro da outra
        def download_thread():
            try:
                # mostra o progresso
                progress_bar.visible = True
                status_text.value = "Analisando vídeo..."
                status_text.color = ft.Colors.BLUE
                page.update()

                # cria o objeto do youtube
                yt = YouTube(url.value.strip())
                # mostra as informações do vídeo
                mostrar_info_videos(yt)
                # inicia o download
                status_text.value = f"Baixando vídeo: {yt.title}..."
                page.update()

                # pega a maior resolução possível
                stream = yt.streams.get_highest_resolution()

                # TODO: fazer o if else do stream
                # capturando as informações do vídeo
                mostrar_info_videos(yt)
            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro {str(e)}."
                status_text.color = ft.Colors.RED_300
                page.update()
        # função para executar em uma thread separada para não travar a interface
        threading.Thread(target=download_thread, daemon=True).start()
        # 
    page.add(
        ft.SafeArea(
            ft.Container(
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
