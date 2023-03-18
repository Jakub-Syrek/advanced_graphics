import cairo

def sierpinski(ctx, level, size):
    if level == 0:
        ctx.move_to(0, 0)
        ctx.line_to(size, 0)
        ctx.line_to(size / 2, size * (3**0.5) / 2)
        ctx.close_path()
        ctx.fill()
    else:
        sierpinski(ctx, level - 1, size / 2)

        ctx.translate(size / 2, 0)
        sierpinski(ctx, level - 1, size / 2)

        ctx.translate(-size / 4, size * (3**0.5) / 4)
        sierpinski(ctx, level - 1, size / 2)

        # Undo the translations
        ctx.translate(size / 4, -size * (3**0.5) / 4)
        ctx.translate(-size / 2, 0)

def main():
    # Create a 640x480 image surface in RGB24 format
    surface = cairo.ImageSurface(cairo.Format.RGB24, 640, 480)

    # Create a drawing context
    ctx = cairo.Context(surface)

    # Set the background color to white
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    # Set the drawing color to black
    ctx.set_source_rgb(0, 0, 0)

    # Draw the Sierpinski triangle
    ctx.translate(20, 20)
    sierpinski(ctx, 3, 400)  # The second parameter is the recursion level

    # Save the surface to a PNG file
    surface.write_to_png("result3.png")

if __name__ == "__main__":
    main()
