import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = "My first app"
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value="Hello world", color=ft.Colors.RED)
    
    
    def text_name(_):
        #print(name_input.value)
        name = name_input.value.strip()

        if name:
          text_hello.color = None
          time = datetime.now()
          text_hello.value = f"{time.strftime("%d:%m:%y - %H:%M:%S")} - Привет {name}"
          name_input.value = None
        else:
           text_hello.value = "Enter name!"  
           text_hello.color = ft.Colors.RED_900
    
    name_input = ft.TextField(label="Enter ur name:", on_submit=text_name)
    
    def thememode(_):
       if page.theme_mode == ft.ThemeMode.DARK:
          page.theme_mode = ft.ThemeMode.LIGHT
       else: 
          page.theme_mode = ft.ThemeMode.DARK
    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

      

    elevated_button = ft.ElevatedButton("send", on_click=text_name, icon=ft.Icons.SEND)


    

    page.add(text_hello, name_input, elevated_button, thememode_button)


    

ft.app(target=main)