from manim import *


def create_service(service_name, service_color):
    result = VGroup()  # create a VGroup
    poly = RegularPolygon(n=6, start_angle=30*DEGREES, color=service_color)
    text = Text(service_name).move_to(poly.get_center())  # create text
    result.add(poly, text)  # add both objects to the VGroup
    return result


def create_ensemble(ensemble_name, ensemble_color):
    result = VGroup()  # create a VGroup
    rect = Rectangle(color=ensemble_color)
    text = Text(ensemble_name).move_to(rect.get_corner(np.array((-1.0, 1.0, 0.0))))  # create text
    result.add(rect, text)  # add both objects to the VGroup
    return result
