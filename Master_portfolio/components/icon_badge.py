import reflex as rx
import Master_portfolio.styles.styles as styles
from Master_portfolio.styles.styles import Size

def icon_badge(image: str, name: str) -> rx.Component:
    return rx.badge(
        rx.image(
            src=image,
            width="20px",
            height="20px",
        ),
        rx.text(
            name,
            size=Size.SMALL.value,
        ),
        style=styles.badge_style
    )
