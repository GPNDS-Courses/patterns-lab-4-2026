from legacy import export_to_dict, render_text
from models import Circle, Point


def test_legacy_renderer_and_exporter() -> None:
    circle = Circle(Point(1, 2), 3)

    rendered = render_text((circle,))
    exported = export_to_dict((circle,))

    assert "Circle" in rendered
    assert exported == [{"type": "circle", "x": 1, "y": 2, "radius": 3}]
