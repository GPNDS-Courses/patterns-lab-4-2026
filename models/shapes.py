from dataclasses import dataclass, field

from .geometry import Point
from .style import Style


@dataclass
class Circle:
    center: Point
    radius: float
    style: Style = field(default_factory=Style)

    def move(self, dx: float, dy: float) -> None:
        self.center = Point(self.center.x + dx, self.center.y + dy)


@dataclass
class Rectangle:
    top_left: Point
    width: float
    height: float
    style: Style = field(default_factory=Style)

    def move(self, dx: float, dy: float) -> None:
        self.top_left = Point(self.top_left.x + dx, self.top_left.y + dy)


@dataclass
class TextLabel:
    position: Point
    text: str
    style: Style = field(default_factory=Style)

    def move(self, dx: float, dy: float) -> None:
        self.position = Point(self.position.x + dx, self.position.y + dy)
