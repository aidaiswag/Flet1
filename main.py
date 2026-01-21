import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = "My first app"
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value="Hello world", color=ft.Colors.RED)
    
    greeting_history = []
    history_text = ft.Text("История пользователей: ")

    def text_name(_):
        #print(name_input.value)
        name = name_input.value.strip()

        if name:
          text_hello.color = None
          time = datetime.now()
          text_hello.value = f"{time.strftime("%d:%m:%y - %H:%M:%S")} - Привет {name}"
          name_input.value = None

          greeting_history.append(name)
          print(greeting_history)
          history_text.value = "История пользователей: \n" + "\n".join(greeting_history)

        else:
           text_hello.value = "Enter name!"  
           text_hello.color = ft.Colors.RED_900
    
    name_input = ft.TextField(label="Enter ur name:", on_submit=text_name, expand=True)
    
    def thememode(_):
       if page.theme_mode == ft.ThemeMode.DARK:
          page.theme_mode = ft.ThemeMode.LIGHT
       else: 
          page.theme_mode = ft.ThemeMode.DARK
    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

      

    elevated_button = ft.ElevatedButton("send", on_click=text_name, icon=ft.Icons.SEND)

    def clear_history(_):
       print(greeting_history)
       greeting_history.clear()
       print(greeting_history)
       history_text.value = "История приветствий: "
    def delete_last(_):
       if greeting_history:
          greeting_history.pop()
          history_text.value = "История пользователей:\n " + "\n".join(greeting_history)
       else:
          history_text.value = "История пользователей пуста!"     

    delete_last_button = ft.IconButton(icon=ft.Icons.REMOVE_CIRCLE_OUTLINE, on_click=delete_last)      
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    
    main_object = ft.Row([name_input, elevated_button, thememode_button, delete_last_button, clear_button])

    page.add(text_hello, main_object, history_text)


    

ft.app(target=main)