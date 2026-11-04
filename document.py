from __future__ import annotations

from typing import Any


class DrawingDocument:
    def __init__(self) -> None:
        self._shapes: list[Any] = []

    def add(self, shape: Any) -> None:
        self._shapes.append(shape)

    def remove(self, shape: Any) -> None:
        self._shapes.remove(shape)

    def shapes(self) -> tuple[Any, ...]:
        return tuple(self._shapes)

    def move_all(self, dx: float, dy: float) -> None:
        for shape in self._shapes:
            shape.move(dx, dy)
