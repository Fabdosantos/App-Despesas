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

    def add_expense(e):
        expense = {
            "name": name.value,
            "type": dd.value,
            "installments": input.value,
            "price": price.value,
        }

        print(expense)
        pass

    name = ft.TextField(label='Nome da Despesa')
    price = ft.TextField(label='Valor', prefix_text='R$')
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
        name,
        dd,
        input,
        price,
        ft.ElevatedButton(text='Adicionar', on_click=add_expense),
    )
    pass


ft.app(target=main)
