from manim import *

def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=2, width=3, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result


class TextBox(Scene):  
    def construct(self):

        # create text box
        textbox = create_textbox(color=BLUE, string="Hello world")
        self.add(textbox)

        # move text box around
        self.play(textbox.animate.shift(2*RIGHT), run_time=3)
        self.play(textbox.animate.shift(2*UP), run_time=3)
        self.wait()

with tempconfig({"quality": "low_quality", "preview": True}):
    scene = TextBox()
    scene.render()