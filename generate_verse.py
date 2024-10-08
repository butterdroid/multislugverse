from PIL.ImageFile import ImageFile
from generativepy.drawing import make_image, setup
from generativepy.geometry import Polygon
from generativepy.color import Color
from scipy.spatial import Voronoi
import random
from PIL import Image


def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return [r, g, b]


SIZE = 500
POINTS = 20

maxsize = [0, 0]

colour = False
random_color_gen = random_color_generator()


# Create a list of random points

def random_points():
    random.seed()
    global points
    points = [[random.randrange(SIZE), random.randrange(SIZE)]
              for i in range(POINTS)]


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))
    voronoi = Voronoi(points)

    voronoi_vertices = voronoi.vertices

    for region in voronoi.regions:
        if -1 not in region:

            # Random Colour for Polygon
            if colour:
                random_color_gen = random_color_generator()
            else:
                random_color_gen = [0, 0, 0]

            polygon = []

            for p in region:

                vertice1 = voronoi_vertices[p][0]
                vertice2 = voronoi_vertices[p][1]

                if vertice1 > SIZE * 2:
                    vertice1 = SIZE - 1
                if vertice1 < 0:
                    vertice1 = 10
                if vertice2 > SIZE * 2:
                    vertice2 = SIZE - 1
                if vertice2 < 0:
                    vertice2 = 10

                polygon.append((vertice1, vertice2))

                # Determine if new max size
                if vertice1 > maxsize[0]:
                    maxsize[0] = vertice1 + 10
                if vertice2 > maxsize[1]:
                    maxsize[1] = vertice2 + 10

            Polygon(ctx).of_points(polygon).stroke(
                Color(random_color_gen.pop() / 255, random_color_gen.pop() / 255, random_color_gen.pop() / 255),
                line_width=4)


def generate_main(colour_input=False, size=500):
    global colour, SIZE
    colour = colour_input
    SIZE = size
    random_points()

    make_image("voronoi-lines.png", draw, SIZE * 2, SIZE * 2)
    image: ImageFile = Image.open("voronoi-lines.png").crop((0, 0, maxsize[0], maxsize[1]))
    image.save("multislugverse.jpg")