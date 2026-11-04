from models import Circle, Rectangle, TextLabel


def render_text(shapes: tuple[object, ...]) -> str:
    """
    Текущий renderer знает обо всех типах фигур.
    При добавлении нового типа его, вероятно, придётся изменять.
    """
    lines: list[str] = []

    for shape in shapes:
        if isinstance(shape, Circle):
            lines.append(
                f"Circle(center=({shape.center.x}, {shape.center.y}), "
                f"radius={shape.radius}, fill={shape.style.fill})"
            )
        elif isinstance(shape, Rectangle):
            lines.append(
                f"Rectangle(top_left=({shape.top_left.x}, {shape.top_left.y}), "
                f"size={shape.width}x{shape.height}, fill={shape.style.fill})"
            )
        elif isinstance(shape, TextLabel):
            lines.append(
                f"Text(position=({shape.position.x}, {shape.position.y}), "
                f"text={shape.text!r}, font={shape.style.font_family})"
            )
        else:
            raise TypeError(f"Unsupported shape: {type(shape).__name__}")

    return "\n".join(lines)
