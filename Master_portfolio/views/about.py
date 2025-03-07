import reflex as rx
import Master_portfolio.styles.styles as styles
from Master_portfolio.styles.styles import Size



def about() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Sobre mí",
            size=Size.BIG.value,
        ),
        rx.text(
            """ Soy un chico de 18 años, curioso y emocionado por aprender cada día más sobre el mundo de la programación. Trabajo principalmente en la parte Frontend, pero también tengo conocimientos en Backend. Soy autodidacta y actualmente estoy disponible para trabajar en cualquier modalidad, con el objetivo de ganar experiencia y seguir creciendo profesionalmente.""",
            style=styles.text_style
        )
    )
