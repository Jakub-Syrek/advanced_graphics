import cairo

def sierpinski(ctx, level):
    surface = cairo.ImageSurface(cairo.Format.RGB24, 640, 480)
    width = surface.get_width()
    height = surface.get_height()
    scale_factor = min(width, height) * 0.8

    def draw_triangle(level):
        if level == 0:
            ctx.move_to(0, 0)
            ctx.line_to(1, 0)
            ctx.line_to(0.5, (3**0.5) / 2)
            ctx.close_path()
            ctx.fill()
        else:
            draw_triangle(level - 1)

            ctx.translate(0.5, 0)
            draw_triangle(level - 1)

            ctx.translate(-0.25, (3**0.5) / 4)
            draw_triangle(level - 1)

            ctx.translate(0.25, -(3**0.5) / 4)
            ctx.translate(-0.5, 0)

    ctx.scale(scale_factor, scale_factor)
    draw_triangle(level)

def main():    
    surface = cairo.ImageSurface(cairo.Format.RGB24, 640, 480)
    
    ctx = cairo.Context(surface)
    
    ctx.set_source_rgb(1, 1, 1)
    
    ctx.paint()
    
    ctx.set_source_rgb(0, 0, 0)
    
    scale_factor = 400

    ctx.translate(20 / scale_factor, 20 / scale_factor)

    sierpinski(ctx, 4)
    
    surface.write_to_png("result3-4.png")

if __name__ == "__main__":
    main()
