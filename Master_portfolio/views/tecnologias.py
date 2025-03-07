import reflex as rx
from Master_portfolio.components.heading import heading
from Master_portfolio.styles.styles import Size
from Master_portfolio.components.technology_link import technology_link

def technologies() -> rx.Component:
    return rx.vstack(
        heading("Tecnologías y herramientas"),
        rx.flex(
            technology_link(
                "JavaScript",
                "icons/javascript.svg",
                "Basico"
            ),
            technology_link(
                "HTML",
                "icons/html.svg",
                "Intermedio"
            ),
            technology_link(
                "CSS",
                "icons/icons8-css.svg",
                "Intermedio"
            ),
            technology_link(
                "Python",
                "icons/piton.svg",
                "Intermedio"
            ),
            technology_link(
                "Docker",
                "icons/icon-docker.svg",
                "Basico"
            ),
            technology_link(
                "GitHub",
                "icons/icon-github.svg",
                "Basico"
            ),
            wrap="wrap",
            spacing="4",
            width="100%",
        ),
        spacing=Size.MEDIUM.value,
    )

