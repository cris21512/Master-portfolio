import reflex as rx



def link_boton(icon: str, url: str, text="") -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
        ),
        href=url,
        is_external=True,
    )
