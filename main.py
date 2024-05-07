import flet as ft
import modules.update as upd

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
    
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Deploy"),
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
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )


ft.app(main)