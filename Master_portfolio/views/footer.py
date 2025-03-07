import reflex as rx
from Master_portfolio.components.links import links
import Master_portfolio.styles.styles as styles
from Master_portfolio.styles.styles import Size
import Master_portfolio.constants.const as const



def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Interesado en contactarme?", style=styles.text_style),
        links(),
    )
