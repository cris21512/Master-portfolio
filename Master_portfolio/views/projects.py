import reflex as rx
from Master_portfolio.components.link_project_01 import link_project_1


def projects() -> rx.Component:
    return rx.box(
        rx.vstack(
            link_project_1(),
        )
    ) 

