import reflex as rx
from Master_portfolio.components.heading import heading
import Master_portfolio.styles.styles as styles
from Master_portfolio.styles.styles import Size


def extras() -> rx.Component:
    return rx.vstack(
        heading("Habilidades blandas"),
        rx.unordered_list(
            rx.list_item("Trabajo en equipo"),
            rx.list_item("Comunicación efectiva"),
            rx.list_item("Adaptabilidad"),
            rx.list_item("Respeto"),
            rx.list_item("Aprendizaje rapido"),
            style=styles.text_style,
        ),
        spacing=Size.SMALL.value,
    )

