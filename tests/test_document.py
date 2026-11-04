from document import DrawingDocument
from models import Circle, Point, Rectangle


def test_document_adds_and_moves_shapes() -> None:
    document = DrawingDocument()
    circle = Circle(Point(1, 2), 3)
    rectangle = Rectangle(Point(10, 20), 5, 6)

    document.add(circle)
    document.add(rectangle)
    document.move_all(2, -1)

    assert circle.center == Point(3, 1)
    assert rectangle.top_left == Point(12, 19)
    assert document.shapes() == (circle, rectangle)
