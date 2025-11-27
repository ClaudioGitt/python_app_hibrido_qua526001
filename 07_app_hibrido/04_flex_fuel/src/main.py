import flet as ft

def main(page: ft.Page):
      def calcular_combustivel(e):
            if not gasolina.value:
                  gasolina.error_text = "Campo não pode ficar vazio"
                  page.update()
            else:
                  gasolina.error_text = ""
                  page.update()
            if not etanol.value:
                  etanol.error_text = "Campo não pode ficar vazio"
                  page.update()
            else:
                  etanol.error_text = ""
                  gasolina.value = float(gasolina.value.replace(",","."))
                  etanol.value = float(etanol.value.replace(",","."))
                  resultado = "gasolina" if etanol.value >= gasolina.value * 0.7 else "etanol"
                  # resultado com caixa de diálogo
                  dlg_modal.content.value = resultado
                  gasolina.value = ""
                  etanol.value = ""
                  

                  page.open(dlg_modal)

                  page.update()
      page.title = "APP Flex Fuel"
      page.scroll = "adaptive"
      page.theme_mode = ft.ThemeMode.LIGHT

      gasolina = ft.TextField(label="Valor da gasolina",prefix_text="R$ ",keyboard_type=ft.KeyboardType.NUMBER,hover_color="#add8e6",bgcolor="white")

      etanol = ft.TextField(label="Valor da etanol",prefix_text="R$ ",keyboard_type=ft.KeyboardType.NUMBER,hover_color="#add8e6",bgcolor="white",on_submit=calcular_combustivel)

      dlg_modal = ft.AlertDialog(modal=True,
                              title=ft.Text("Melhor abastecer com: "),content=ft.Text(size=20,
                              width="bold"),
                              actions = [ft.TextButton("OK",
                              on_click=lambda e:page.close((dlg_modal)))],
                              actions_alignment = ft.MainAxisAlignment.END)


      page.add(
            ft.SafeArea(
                  ft.Container(
                        ft.Text("FLEX FUEL", size=25, weight="bold",color=""),
                        alignment=ft.alignment.center,
                        padding=100
                  ),
            ),
            ft.ResponsiveRow(
                  [ # dicionario, informando chaves e valores.
                        ft.Container(gasolina,col={"sm":6,"md":4,"xl":2}),
                        ft.Container(etanol,col={"sm":6,"md":4,"xl":2})
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                  [
                        ft.Container(
                              ft.ElevatedButton("Calcular",on_click=calcular_combustivel,icon=ft.Icons.CAR_CRASH_ROUNDED,width=150),
                              padding=30,
                              on_hover="#ADD8E6"
                        )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER 
            )
      )
ft.app(main)
