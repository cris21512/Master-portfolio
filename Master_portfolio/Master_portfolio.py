import reflex as rx
from Master_portfolio.views.header import header
from Master_portfolio.views.about import about
from Master_portfolio.views.tecnologias import technologies
from Master_portfolio.views.projects import projects
from Master_portfolio.views.formacion import educacion
from Master_portfolio.views.extra import extras
from Master_portfolio.views.footer import footer
import Master_portfolio.styles.styles as styles
from Master_portfolio.styles.styles import Size,EmSize,MAX_WIDTH,STYLESHEETS




def index() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                header(),
                about(),
                rx.divider(color_scheme="tomato"),
                technologies(),
                projects(),
                educacion(),
                extras(),
                rx.divider(color_scheme="tomato"),
                footer(),
        spacing=Size.MEDIUM.value,
        padding_x=EmSize.MEDIUM.value,
        padding_y=EmSize.BIG.value,
        max_width=MAX_WIDTH,
        width="100%"
            )
        ),
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Portfolio de Master | Desarrollador web",
    description="Mi Portafolio como desarrollador web full-stack",
    image="/logo2.png",
)
