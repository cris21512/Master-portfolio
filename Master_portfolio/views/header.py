import reflex as rx
from Master_portfolio.components.heading import heading
from Master_portfolio.styles.styles import Size
import Master_portfolio.styles.styles as styles
from Master_portfolio.components.links import links


def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src="/avatar.jpg",
            radius="full",
            size=Size.BIG.value,
        ),
        rx.vstack(
            heading(
                "Soy Cristopher Fuentes",
            ),
            rx.text(
                "Y soy un:", rx.text.strong("Desarrollador Web Full-Stack junior", style=styles.projects_text_style),
                size=Size.DEFAULT.value,
                style=styles.title_style,
            ),
            rx.text(
                rx.icon("map-pin"),
                "Guatemala, Guatemala",
                display="inherit",
                style=styles.text_style,
            ),
            links(),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )
