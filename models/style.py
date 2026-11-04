from dataclasses import dataclass


@dataclass
class Style:
    """
    Стиль намеренно является отдельным изменяемым объектом.

    Подумайте, какие последствия это имеет при копировании и при большом
    количестве фигур с одинаковым оформлением.
    """

    stroke: str = "black"
    fill: str = "transparent"
    stroke_width: float = 1.0
    font_family: str = "sans-serif"
