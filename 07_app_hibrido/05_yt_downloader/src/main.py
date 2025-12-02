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

                # fazer o if else do stream
                # capturando as informações do vídeo
                if stream:
                    # O que ira fazer? Fazer o download
                    # vai informar onde é o download
                    stream.download(caminho_videos)
                    # Se concluir o download, o progressbar some
                    # sucesso
                    progress_bar.visible = False
                    status_text.value = "Download concluído com sucesso."
                    status_text.color = ft.Colors.GREEN
                    page.update()
                else:
                    progress_bar.visible = False
                    status_text.value = "Não foi possível baixar o vídeo."
                    status_text.color = ft.Colors.RED
                    page.update()

            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro {str(e)}."
                status_text.color = ft.Colors.RED_300
                page.update()
        # função para executar em uma thread separada para não travar a interface
        threading.Thread(target=download_thread, daemon=True).start()
    # Extrair o áudio do vídeo
    def extrair_audio(e):
        if not url.value.strip():
            status_text.value = "Favor inserir uma URL"
            status_text.color = ft.Colors.ORANGE
            page.update()
        def download_thread():
            try:
                # Aqui o código para download com thread
                progress_bar.visible = True # já que o download tá sendo feito, o bar aparece
                status_text.value = "Analisando vídeo..."
                status_text.color = ft.Colors.BLUE
                page.update()

                # cria objeto Youtube
                yt = YouTube(url.value.strip())

                # mostra informações do vídeo
                # .strip para dar uma padronizada
                mostrar_info_videos(yt)

                # iniciar o download do áudio
                status_text = f"Extraindo o audio de {yt._title}..."
                page.update()

                stream = yt.streams.filter(only_audio=True).first()
                if stream:
                    audio_file = stream.download(caminho_audios)

                    # renomeia para mp3
                    base, extens = os.path.splitext(audio_file)
                    novo_audio = base + ".mp3"
                    os.rename(audio_file,novo_audio)

                    # Sucesso
                    progress_bar.visible = False
                    status_text.value = f"Áudio salvo como {os.path.basename(novo_audio)}"
                    status_text.color = ft.Colors.GREEN
                    page.update()
                else:
                    progress_bar.visible = False
                    status_text.value = "Não foi possível baixar o áudio."
                    status_text.color = ft.Colors.RED
                    page.update()
            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro: {str(e)}."
                status_text.color = ft.Colors.RED
                page.update()
        # executa em thread separada para não travar interface
        threading.Thread(target=download_thread, daemon=True).start()
    # limpa campos e reinicia a interface
    def limpar_campos(e):
        url.value = ""
        video_info.visible = False
        progress_bar.visible = False
        status_text.value = ""
        page.update()
    # interface
    video_btn = ft.ElevatedButton(
        text="Baixar vídeo",
        width=150,
        on_click=baixar_video,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            shadow_color=ft.Colors.BLACK,
            elevation=3,
            text_style=ft.TextStyle(size=18),
            visual_density=2,
            shape=ft.RoundedRectangleBorder
        )
    )
    audio_btn = ft.ElevatedButton(
        text = "Baixar áudio",
        width = 150,
        on_click = extrair_audio,
        style = ft.ButtonStyle(
            bgcolor = ft.Colors.BLUE,
            color = ft.Colors.WHITE,
            shadow_color = ft.Colors.BLACK,
            elevation = 3,
            text_style = ft.TextStyle(size=18),
            visual_density = 2,
            shape = ft.RoundedRectangleBorder
        )
    )
    clear_btn = ft.IconButton(
        on_click=limpar_campos,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREY,
            color=ft.Colors.WHITE,
            elevation=1
        )
    )
    # cria a linha para inserir a URL
    linha_url = ft.Row(
        [url, clear_btn],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    botoes = ft.Row(
        [video_btn,audio_btn],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
