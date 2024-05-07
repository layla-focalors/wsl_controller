import flet as ft
import modules.update as upd

# VM Delete 등의 작업 후에는 반드시 page.refresh()
# settings 창을 vm 관리탭에 다시 만들고 그걸 클릭 시 ram 등을 제어


def deploy_page():
    return ft.Text("Deploy Page")

def environment_page():
    vm_list = upd.get_vm_list()
    tabs = []
    
    if len(vm_list) != 0:
        return ft.Column([
            ft.Text("No WSL found!"),
            ft.Text("Please Deploy any WSL first!, and then reload this page!")
        ])
    
    for i, vm in enumerate(vm_list):
        tab = ft.Tab(
            text=f"{vm[3]}",
            content=ft.Column([
                ft.Text(
                    f"{vm[3]}",
                    color='white',
                    size=20
                )   
            ])
        )
        tabs.append(tab)

    env_page = ft.Column([
        ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=tabs,
            expand=1,
        ),
        ft.Text("Environment Page"),
        ft.Text("Environment Page"),
    ])
    return env_page

def functions_page():
    return ft.Text("Functions Page")

def storages_page():
    return ft.Text("Storages Page")

def settings_page():
    return ft.Text("Settings Page")

def main(page: ft.Page):
    page.window_width = 1280
    page.window_height = 720
    page.window_resizable = False
    page.title = f"{upd.get_version()} - WSL Controller by layla-focalors"
    
    lang = upd.get_language()
    
    if lang == 'korean':
        pass
    else:
        pass
    
    body = ft.Column([ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True)
    
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Deploy", on_click=lambda e: update_body(-1, body)),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.AIRPLAY, selected_icon=ft.icons.AIRPLAY_OUTLINED, label="Environment"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Functions",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Storages"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.STORAGE_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.STORAGE),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: update_body(e.control.selected_index, body),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                body,
            ],
            expand=True,
        )
    )

    def update_body(index, body):
        body.controls.clear()
        if index == -1:
            body.controls.append(deploy_page())
        elif index == 0:
            body.controls.append(environment_page())
        elif index == 1:
            body.controls.append(functions_page())
        elif index == 2:
            body.controls.append(storages_page())
        elif index == 3:
            body.controls.append(settings_page())
        page.update()

    update_body(0, body)

    page.update()

ft.app(main)
