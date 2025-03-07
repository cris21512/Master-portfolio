import reflex as rx
from Master_portfolio.styles.styles import Size
import Master_portfolio.styles.styles as styles


def technology_link(nombre: str, image: str, nivel: str) -> rx.Component:
    return rx.hstack(
        rx.container(
            rx.vstack(
                rx.text(
                    nombre,
                    size=Size.SMALL.value,
                    style=styles.title_style,
                ),
                rx.image(
                    src=image,
                    width="70px",
                    height="70px",
                ),
                rx.text(
                    nivel,
                    size=Size.SMALL.value,
                    style=styles.text_style,
                ),
                align="center"
            )
        )
    )
