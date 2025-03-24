from enum import Enum
import reflex as rx
from .colors import Colors,TexColor 

MAX_WIDTH = "800px"
IMAGE_HEIGHT = "200px"


class EmSize(Enum):
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Montserrat:wght@400;700&family=Raleway:ital,wght@1,500&display=swap"
    "https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;600&display=swap"
]

BASE_STYLE = {
    "background-image": "radial-gradient(circle, rgba(173,216,230,1) 2px, transparent 2px)",
    "background-size": "30px 30px",
    "background-color": "#CFC5B0",
    rx.heading:{
        "color":TexColor.TITLE.value,
        "font_family": "'Raleway', sans-serif",
        "font_weight": "600",
        "font_style": "italic",
    },
    rx.container: {
        "width": "100px",
        "height": "160px",
        "background": Colors.CARDS.value,
        "padding": "0.60em",
        "border-radius": "10px",
        "border": "1px solid rgba(0,0,0,0)",
        "cursor": "pointer",
        "transition": "transform 0.5s",
        "_hover": {
            "box-shadow": "inset 4px 4px 6px -1px rgba(0, 0, 0, 0.2), inset -4px -4px -6px -1px rgba(255, 255, 255, 0.7), -0.5px -0.5px 0px rgba(255,255,255,1), 0.5px 0.5px 0.5px 0px rgba(0,0,0,0.15), 0px 12px 10px -10px rgba(0,0,0,0.1)",
        "border": "1px solid rgba(0,0,0,0.1)",
        "transform": "translateY(0.5em)",
        },
        "image": {
            "transition": "transform 0.5s",
        },
        "_hover image": {
            "transform": "scale(0.9)",
            "fill": "#333333"
        },
    },
    rx.card:{
        "width": "100%",
        "background": TexColor.PROJECTS.value,
        "padding_y": "0.5rem",
        "border-radius": "0.60rem",
        "box-shadow": "0.4rem 0.4rem #19191a",
        "overflow": "hidden",
        "color": "black",
        "align-items": "center",
        "transition": "all 0.2s ease-in-out",
        "_hover": {
            "box-shadow": "0rem 0rem #05060f",
            "translate": "1.5px 1.5px",
        }
    },
    rx.button: {
        "padding": "10px 10px",
        "text-transform": "uppercase",
        "border-radius": "8px",
        "color": "#8c8c8c",
        "font-size": "12px",
        "font-weight": "500",
        "text-shadow": "none",
        "background": "transparent",
        "cursor": "pointer",
        "box-shadow": "transparent",
        "border": "1px solid #19191a",
        "transition": "0.5s ease",
        "user-select": "none",
        "_hover": {
                "color": "#ffffff",
                "background": "#008cff",
                "border": "1px solid #008cff",
                "text-shadow": "0 0 1px #ffffff, 0 0 1px #ffffff, 0 0 1px #ffffff",
                "box-shadow": """0 0 5px #008cff, 0 0 20px #008cff, 0 0 50px #008cff,
                0 0 10px #008cff""",
        }
    },
}

title_style = {
    "font_family": "'Raleway', sans-serif",
    "font_weight": "600",
    "font_style": "italic",
    "color": TexColor.TITLE.value,
}

sub_title_style = {
    "color": TexColor.SUBTITLE.value,
}

text_style = {
    "font-family": "Poppins",
    "color": TexColor.SECUNDARY.value,
    "font-size": "1em",
}

badge_style = {
    "background-color": "transparent",
    "border-radius": "50px",
    "padding": "5px 5px",
    "color": TexColor.TERCIARY.value,
    "box-shadow": "0px 0px 0px 3px rgba(1,1,0,0.1)",
}

technolgies_style = {
    "font-family": "cursive",
    "color": TexColor.SUBTITLE.value,
}

projects_text_style = {
    "color": TexColor.PROJECTS.value,
}


card_style = {
        "width": "100%",
        "background": Colors.CARDS.value,
        "padding_y": "0.5rem",
        "border-radius": "1rem",
        "border": "0.5vim solid #05060f",
        "box-shadow": "0.4rem 0.4rem #05060f",
        "overflow": "hidden",
        "color": "black",
        "align-items": "center",
        "transition": "all 0.2s ease-in-out",
        "_hover": {
            "box-shadow": "0rem 0rem #05060f",
            "translate": "1.5px 1.5px",
        }
    }