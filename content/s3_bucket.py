from manim import *
from assets.building_blocks import *


class S3Bucket(Scene):
    def construct(self):
        s3_bucket = create_service(service_name="S3", service_color=PURPLE)
        vpc = create_ensemble(ensemble_name="VPC", ensemble_color=BLUE)
        self.play(Create(s3_bucket))
        self.play(Create(vpc))
        self.wait(1)


with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = S3Bucket()
    scene.render()
