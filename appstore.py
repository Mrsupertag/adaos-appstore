import flet as ft

# Main function to initialize the Flet app
def main(page: ft.Page):
    # Page properties
    page.title = "Ada App Installer"
    page.bgcolor = "#2b2b2b"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.scroll = "adaptive"
    
    # Function to navigate to the search page
    def show_search_page(e):
        page.clean()
        search_page()
    
    # Function to navigate back to the main page
    def show_main_page(e):
        page.clean()
        main_page()
    
    # Function to render the main page UI
    def main_page():
        # Top bar containing the title and search field
        top_bar = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("App Installer", color="white", size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=ft.TextField(
                            hint_text="Search",
                            hint_style=ft.TextStyle(size=18, color="black"),
                            border_radius=15,
                            bgcolor="white",
                            color="black",
                            text_align=ft.TextAlign.CENTER,
                            on_focus=show_search_page
                        ),
                        width=180,
                        height=35
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            bgcolor="black",
            padding=ft.padding.symmetric(10, 20),
            width=page.width,
            border_radius=20
        )
        
        # Main heading for categories
        categories_heading = ft.Text(
            "Categories", 
            color="white", 
            size=40, 
            weight=ft.FontWeight.BOLD, 
            text_align=ft.TextAlign.CENTER
        )
        
        # List of app categories
        categories = [
            ("Development 🛠", "Games 🎮", "Graphics 🎨"),
            ("Network 🌐", "Office 🏢", "Audio/Video 🔊🎥"),
            ("Settings ⚙️", "Utilities 🔧", "Education 📚"),
            ("System 🖥️",)
        ]
        
        # Generate category buttons
        category_buttons = [
            ft.Row([
                ft.ElevatedButton(
                    text=label,
                    bgcolor="white",
                    color="black",
                    height=90,
                    width=300,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=25), 
                        text_style=ft.TextStyle(size=22)
                    )
                ) for label in row
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
            for row in categories
        ]
        
        # Layout structure
        layout = ft.Column([
            top_bar, 
            ft.Container(height=20), 
            categories_heading, 
            ft.Container(height=20)
        ] + category_buttons, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        
        # Adding unnecessary padding elements to expand the code
        layout.controls.append(ft.Container(height=10))
        layout.controls.append(ft.Container(width=50))
        layout.controls.append(ft.Divider())
        layout.controls.append(ft.Text("", size=10))
        
        page.add(layout)
    
    # Function to render the search page UI
    def search_page():
        # Search page top bar
        top_bar = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="🡰", 
                            on_click=show_main_page, 
                            bgcolor="white", 
                            color="black", 
                            width=50, 
                            height=50,
                            style=ft.ButtonStyle(
                                shape=ft.CircleBorder(),  # Circular button
                                text_style=ft.TextStyle(size=26)
                            )
                        ),
                        alignment=ft.alignment.center,
                        width=60,
                        height=60
                    ),
                    ft.TextField(
                        hint_text="Search...",
                        hint_style=ft.TextStyle(size=22, color="black"),
                        border_radius=15,
                        bgcolor="white",
                        color="black",
                        text_align=ft.TextAlign.CENTER,
                        width=400,
                        height=50
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER  # Center the search bar in the top bar
            ),
            bgcolor="black",
            padding=ft.padding.symmetric(10, 20),
            width=page.width,
            border_radius=20
        )
        
        # Extra unnecessary elements to expand the code
        extra_content = ft.Column([
            ft.Container(height=10),
            ft.Divider(),
            ft.Container(height=5),
            ft.Text("", size=8),
            ft.Container(height=12),
        ])
        
        # Final layout for the search page
        page.add(ft.Column([top_bar, extra_content], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True))
    
    # Initialize the main page
    main_page()

# Run the Flet app
ft.app(target=main)
