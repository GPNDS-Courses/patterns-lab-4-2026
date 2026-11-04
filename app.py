from document import DrawingDocument
from legacy import export_to_dict, render_text
from models import Circle, Point, Rectangle, Style, TextLabel


def build_demo_document() -> DrawingDocument:
    document = DrawingDocument()

    style_1 = Style(stroke="navy", fill="lightblue", stroke_width=2)
    style_2 = Style(stroke="navy", fill="lightblue", stroke_width=2)

    document.add(Circle(Point(10, 10), 5, style_1))
    document.add(Rectangle(Point(20, 15), 30, 10, style_2))
    document.add(TextLabel(Point(5, 40), "Design Patterns", Style(font_family="serif")))

    return document


def main() -> None:
    document = build_demo_document()

    print("TEXT RENDER")
    print(render_text(document.shapes()))
    print()
    print("DICT EXPORT")
    print(export_to_dict(document.shapes()))


if __name__ == "__main__":
    main()
