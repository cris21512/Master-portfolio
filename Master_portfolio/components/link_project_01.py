import reflex as rx
from Master_portfolio.components.info_1 import info_1
from Master_portfolio.components.info_2 import info_2
from Master_portfolio.components.heading import heading




def link_project_1() -> rx.Component:
    return rx.vstack(
        heading("Proyectos"),
        info_1(
            "tv-minimal-play",
            "Pagina Web Oficial",
            "Web oficial de Chito y Cris",
            "Como creador de contenido, he creado mi propia web de links para mis redes sociales y contenido.",
            "/proyect_1.jpg"
        ),
        info_2(
            "plane",
            "Interphase",
            "Interfaz de viajes para vuelos y hoteles",
            "Viajar a tu lugar favorito nunca habia sido tan facil, con esta interfaz podras encontrar los mejores precios en vuelos y hoteles.",
            "/proyect_2.jpg"
        ),
        spacing="5"
    )
