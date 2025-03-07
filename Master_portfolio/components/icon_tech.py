import reflex as rx
from Master_portfolio.styles.colors import Colors



def icon_techs(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.image(
                src=image,
                width="20px",
                height="20px",
            ),
            style={
                "width": "100%",
                "background": Colors.CARDS,
                "padding_y": "0.5rem",
                "border-radius": "1rem",
                "border": "0.5vim solid #05060f",
                "box-shadow": "3px 3px #05060f",
                "overflow": "hidden",
                "color": "black",
                "align-items": "center",
                "transition": "all 0.2s ease-in-out",
                "_hover": {
                    "box-shadow": "0rem 0rem #05060f",
                    "translate": "1.5px 1.5px",
                }
            }
        ),
        href=url,
        is_external=True
    ) 
