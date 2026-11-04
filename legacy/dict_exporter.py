from models import Circle, Rectangle, TextLabel


def export_to_dict(shapes: tuple[object, ...]) -> list[dict[str, object]]:
    """
    Ещё одна операция, зависящая от конкретных типов фигур.
    """
    result: list[dict[str, object]] = []

    for shape in shapes:
        if isinstance(shape, Circle):
            result.append(
                {
                    "type": "circle",
                    "x": shape.center.x,
                    "y": shape.center.y,
                    "radius": shape.radius,
                }
            )
        elif isinstance(shape, Rectangle):
            result.append(
                {
                    "type": "rectangle",
                    "x": shape.top_left.x,
                    "y": shape.top_left.y,
                    "width": shape.width,
                    "height": shape.height,
                }
            )
        elif isinstance(shape, TextLabel):
            result.append(
                {
                    "type": "text",
                    "x": shape.position.x,
                    "y": shape.position.y,
                    "text": shape.text,
                }
            )
        else:
            raise TypeError(f"Unsupported shape: {type(shape).__name__}")

    return result
