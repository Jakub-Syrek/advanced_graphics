import cairo

def draw_sierpinski(ctx, depth):
    # Set up initial triangle
    WIDTH, HEIGHT = ctx.get_target().get_width(), ctx.get_target().get_height()
    points = [(WIDTH / 2, 0), (0, HEIGHT), (WIDTH, HEIGHT)]

    # Define function to draw triangle
    def draw_triangle(p1, p2, p3):
        ctx.move_to(*p1)
        ctx.line_to(*p2)
        ctx.line_to(*p3)
        ctx.close_path()
        ctx.stroke()

    # Define function to recursively draw mesh
    def draw_mesh(points, depth):
        draw_triangle(*points)

        if depth > 0:
            p1, p2, p3 = points
            p4 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            p5 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
            p6 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)
            draw_mesh([p1, p4, p6], depth - 1)
            draw_mesh([p4, p2, p5], depth - 1)
            draw_mesh([p6, p5, p3], depth - 1)

    # Draw the mesh
    draw_mesh(points, depth)

# Set up the Cairo surface
WIDTH, HEIGHT = 2048 , 2048
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Draw the Sierpinski mesh
draw_sierpinski(ctx, depth=11)

# Save the image to a file
surface.write_to_png("D:/tmp/sierpinski.png")
