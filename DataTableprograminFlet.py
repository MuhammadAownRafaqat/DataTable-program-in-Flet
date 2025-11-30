import flet as ft

def acoolfunction(page: ft.Page):
    page.window.width = 500
    page.window.height = 500
    firsttextfieldvalue = ""
    secondtextfieldvalue = ""

    
    greeting = ft.Row(
        controls=[
            ft.Text(value="Enter Username and Password")
        ]
    )
    page.add(greeting)

    
    firsttextfield = ft.TextField(label="Username", on_submit=lambda _: submitusername())
    page.add(firsttextfield)

    
    secondtextfield = ft.TextField(label="Password", on_submit=lambda _: submitpassword())
    page.add(secondtextfield)

    def submitusername():
        nonlocal firsttextfieldvalue
        firsttextfieldvalue = firsttextfield.value
        
        check_fields()

    def submitpassword():
        nonlocal secondtextfieldvalue
        secondtextfieldvalue = secondtextfield.value
        
        check_fields()

    def check_fields():
        
        if firsttextfieldvalue and secondtextfieldvalue:
            show_data_table()
        else:
            
            page.add(ft.SnackBar(content=ft.Text(value="Please enter both username and password")))
            page.update()

    def show_data_table():
        
        thetextfield = ft.TextField(label="Enter Name, Age and Profession", on_submit=lambda _: submitthedataforrow())
        page.add(thetextfield)

        
        thedatatable = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(value="Name")),
                ft.DataColumn(ft.Text(value="Age")),
                ft.DataColumn(ft.Text(value="Profession"))
            ],
            rows=[]
        )
        page.add(thedatatable)

        current_value = []
        step = 0

        def submitthedataforrow():
            nonlocal current_value, step
            if step == 0:
                current_value.append(thetextfield.value)  
                step = 1
            elif step == 1:
                current_value.append(thetextfield.value)  
                step = 2
            elif step == 2:
                current_value.append(thetextfield.value)  
                rowgoinginsidethecolumns = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=current_value[0])),
                        ft.DataCell(ft.Text(value=current_value[1])),
                        ft.DataCell(ft.Text(value=current_value[2]))
                    ]
                )
                thedatatable.rows.append(rowgoinginsidethecolumns)
                page.update()
                current_value = []
                step = 0

            thetextfield.value = ""
            page.update()

    
    

ft.app(acoolfunction)
