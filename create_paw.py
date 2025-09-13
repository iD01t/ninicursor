from PIL import Image, ImageDraw

def create_paw_print(size=(200, 200), color=(255, 192, 203, 255)):
    """Creates a single paw print image with a transparent background."""
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Scale factor based on size
    scale = size[0] / 200.0

    # Main pad
    draw.ellipse([(50 * scale, 90 * scale), (150 * scale, 190 * scale)], fill=color)

    # Toes
    draw.ellipse([(40 * scale, 40 * scale), (80 * scale, 80 * scale)], fill=color)
    draw.ellipse([(80 * scale, 20 * scale), (120 * scale, 60 * scale)], fill=color)
    draw.ellipse([(120 * scale, 40 * scale), (160 * scale, 80 * scale)], fill=color)

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
