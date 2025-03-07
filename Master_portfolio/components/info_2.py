import reflex as rx
from Master_portfolio.components.icon_badge import icon_badge
from Master_portfolio.styles.styles import Size,IMAGE_HEIGHT
import Master_portfolio.styles.styles as styles
from Master_portfolio.components.icon_tech import icon_techs
import Master_portfolio.constants.const as const


def info_2(
        icon: str,
        title: str, 
        subtitle: str, 
        description: str,
        image: str
    ) -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.badge(
                rx.icon(
                    icon,
                    size=35,
                    
                ),
                style={
                "background-color": "transparent",
                "border-radius": "50px",
                "border": "2px solid rgba(206,206,206)",
                "padding": "10px 10px",
                "transition": "0.3s",
                "_hover":{
                    "border": "2px solid #19191a",
                    "box-shadow": "inset 0 0 10px #97e9ff",
                }
            },
            ),
            rx.vstack(
                rx.heading(
                    title,
                    as_="h1"
                ),
                rx.text(
                    subtitle,
                    size="3",
                    style=styles.projects_text_style
                ),
                rx.text(
                    description,
                    size=Size.SMALL.value,
                    style=styles.text_style
                ),
                rx.flex(
                    icon_badge(
                        "icons/minipython.svg",
                        "Python"
                    ),
                    icon_badge(
                        "icons/cssmini.svg",
                        "CSS"
                    ),
                    icon_badge(
                        "icons/minipython.svg",
                        "Reflex"
                    ),
                    wrap="wrap",
                    flex_direction=["row", "row", "row"],
                    spacing=Size.DEFAULT.value,
                ),
                rx.hstack(
                    icon_techs(
                        "icons/minigithub.svg",
                        const.GITPROJECT2
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%",
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        rx.hstack(
        rx.card(
            rx.image(
                src=image,
                height=IMAGE_HEIGHT,
                width="auto",
                object_fit="cover",
                border_radius="0.60rem",
                ),
            ),
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%",
    )
