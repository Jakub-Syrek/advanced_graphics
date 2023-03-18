import cairo

def draw_tree(ctx):    
    ctx.set_source_rgb(0, 1, 0)    
    ctx.move_to(25, 80)
    ctx.line_to(5, 100)
    ctx.line_to(45, 100)
    ctx.close_path()
    ctx.fill()
    
    ctx.move_to(25, 60)
    ctx.line_to(5, 80)
    ctx.line_to(46, 80)
    ctx.close_path()
    ctx.fill()

    ctx.move_to(25, 40)
    ctx.line_to(5, 60)
    ctx.line_to(45, 60)
    ctx.close_path()
    ctx.fill()
    
    ctx.set_source_rgb(0.6, 0.3, 0.1)
    ctx.rectangle(20, 100, 10, 20)
    ctx.fill()

def main():
    # Create a 640x480 image surface in RGB24 format
    surface = cairo.ImageSurface(cairo.Format.RGB24, 640, 480)

    # Create a drawing context
    ctx = cairo.Context(surface)

    # Draw the tree
    draw_tree(ctx)

    # Save the surface to a PNG file
    surface.write_to_png("result1.png")

if __name__ == "__main__":
    main()