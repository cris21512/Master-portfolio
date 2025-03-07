import reflex as rx
from Master_portfolio.components.link_button import link_boton
from Master_portfolio.styles.styles import Size
import Master_portfolio.constants.const as const


def links() -> rx.Component:
    return rx.flex(
        link_boton(
            "mail",
            const.GMAIL,
            "master.email94@gmail.com"
        ),
        rx.hstack(
            link_boton(
                "file-text",
                const.CV
            ),
            link_boton(
                "github",
                const.GITHUB
            ),
            link_boton(
                "linkedin",
                const.LINKEDIN
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"],
    )
