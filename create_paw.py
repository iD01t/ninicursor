from PIL import Image, ImageDraw

def create_paw_print(size=(200, 200), color=(255, 192, 203, 255)):
    """Creates a single paw print image with a transparent background."""
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Scale factor based on size
    scale = size[0] / 200.0

    # Main pad (kept the same)
    draw.ellipse([(50 * scale, 90 * scale), (150 * scale, 190 * scale)], fill=color)

    # Four Toes
    # I've adjusted the size and position of the toes to fit four in a nice arc.
    draw.ellipse([(40 * scale, 55 * scale), (70 * scale, 85 * scale)], fill=color) # Toe 1
    draw.ellipse([(70 * scale, 35 * scale), (100 * scale, 65 * scale)], fill=color) # Toe 2
    draw.ellipse([(100 * scale, 35 * scale), (130 * scale, 65 * scale)], fill=color) # Toe 3
    draw.ellipse([(130 * scale, 55 * scale), (160 * scale, 85 * scale)], fill=color) # Toe 4

    return image

if __name__ == "__main__":
    colors = {
        "pink": (255, 192, 203, 255),
        "lightblue": (173, 216, 230, 255),
        "yellow": (255, 255, 0, 255)
    }

    sizes = [100, 150]

    for name, color in colors.items():
        for size in sizes:
            paw_image = create_paw_print(size=(size, size), color=color)
            paw_image.save(f"paw_{name}_{size}.png")
