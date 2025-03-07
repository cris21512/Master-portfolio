import reflex as rx
from Master_portfolio.styles.styles import Size
import Master_portfolio.styles.styles as styles


def heading(text: str) -> rx.Component:
    return rx.heading(
        text,
        size=Size.BIG.value,
        style=styles.title_style,
    )
