import cairo

def sierpinski(ctx, level):
    surface = cairo.ImageSurface(cairo.Format.RGB24, 640, 480)
    width = surface.get_width()
    height = surface.get_height()
    size = min(width, height) * 0.8

    def draw_triangle(level, size):
        if level == 0:
            ctx.move_to(0, 0)
            ctx.line_to(size, 0)
            #"size * (3**0.5) / 2: This is the y-coordinate of the point. 
            # It's calculated using the properties of an equilateral triangle. 
            # The height of an equilateral triangle can be found using the formula: height = (side_length * sqrt(3)) / 2. 
            # In this case, size is the side length of the triangle, and (3**0.5) is the square root of 3."
            ctx.line_to(size / 2, size * (3**0.5) / 2)
            ctx.close_path()
            ctx.fill()
        else:
            draw_triangle(level - 1, size / 2)

            ctx.translate(size / 2, 0)
            draw_triangle(level - 1, size / 2)

            ctx.translate(-size / 4, size * (3**0.5) / 4)
            draw_triangle(level - 1, size / 2)

            ctx.translate(size / 4, -size * (3**0.5) / 4)
            ctx.translate(-size / 2, 0)

    draw_triangle(level, size)

def main():    
    surface = cairo.ImageSurface(cairo.Format.RGB24, 640, 480)
    
    ctx = cairo.Context(surface)
    
    ctx.set_source_rgb(1, 1, 1)
    
    ctx.paint()
    
    ctx.set_source_rgb(0, 0, 0)
    
    ctx.translate(20, 20)

    sierpinski(ctx, 4)
    
    surface.write_to_png("result3-4.png")

if __name__ == "__main__":
    main()
