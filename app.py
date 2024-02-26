import flet as ft

def main(page: ft.Page):
    page.title = 'App Despesas'

    def add_installments_input(e):
        if (dd.value == "Parcelada"):
            input.visible = True
            page.update()
            return
        input.visible = False
        page.update()

    input = ft.TextField(label="Quantidade de Parcelas", visible=False)
    dd = ft.Dropdown(
         label='Tipo',
         on_change=add_installments_input,
         options=[
            ft.dropdown.Option('Unica'),
            ft.dropdown.Option('Parcelada'),
        ])

    page.add(
        ft.Text('Adicione uma despesa', theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        ft.TextField(label='Nome da Despesa'),
        dd,
        input,
        ft.TextField(label='R$'),
    )
    pass


ft.app(target=main)
