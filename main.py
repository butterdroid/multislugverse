from generativepy.drawing import make_image, setup
from generativepy.geometry import Circle, Polygon
from generativepy.color import Color
from scipy.spatial import Voronoi
import random
import colornames


def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return [r, g, b]


random_color = random_color_generator()

SIZE = 1000
POINTS = 20

# Create a list of random points
random.seed()
points = [[random.randrange(SIZE), random.randrange(SIZE)]
          for i in range(POINTS)]


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))
    voronoi = Voronoi(points)

    voronoi_vertices = voronoi.vertices

    for region in voronoi.regions:
        if -1 not in region:
            random_color_gen = random_color_generator()


            polygon = []

            for p in region:

                vertice1 = voronoi_vertices[p][0]
                vertice2 = voronoi_vertices[p][1]

                if vertice1 > SIZE*2:
                    vertice1 = SIZE-1
                if vertice1 < 0:
                    vertice1 = 1
                if vertice2 > SIZE*2:
                    vertice2 = SIZE-1
                if vertice2 < 0:
                    vertice2 = 1

                polygon.append((vertice1,vertice2))

            Polygon(ctx).of_points(polygon).stroke(
                Color(random_color_gen.pop() / 255, random_color_gen.pop() / 255, random_color_gen.pop() / 255), line_width=4)


make_image("voronoi-lines.png", draw, SIZE * 2, SIZE * 2)
