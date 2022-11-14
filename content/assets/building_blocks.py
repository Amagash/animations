from manim import *
from manim.utils.unit import Pixels


def create_service(service_name, service_color):
    result = VGroup()  # create a VGroup
    poly = RegularPolygon(n=6, start_angle=30*DEGREES, color=service_color)
    text = Text(service_name).move_to(poly.get_center())  # create text
    result.add(poly, text)  # add both objects to the VGroup
    return result


def create_ensemble(ensemble_name, ensemble_color):
    result = VGroup()  # create a VGroup
    rec = Rectangle(color=ensemble_color)
    text=Text(ensemble_name, font_size=20).align_to(rec, UL).shift(10 * Pixels * DR)

    result.add(rec, text)  # add both objects to the VGroup
    return result
