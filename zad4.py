import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk, Gtk
gi.require_foreign("cairo")


class Okno(Gtk.Window):
    def __init__(self):
        super(Okno, self).__init__()

        self.lines = []

        self.set_title("Okno GTK")
        self.set_default_size(400, 300)
        self.connect("destroy", Gtk.main_quit)
        da = Gtk.DrawingArea()
        da.set_size_request(200, 200)
        da.connect("draw", self.on_draw)
        da.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        da.connect("button-press-event", self.on_button_press)
        self.add(da)
        self.show_all()

    def on_draw(self, widget, ctx):
        for line in self.lines:
            x1, y1, x2, y2 = line
            ctx.move_to(x1, y1)
            ctx.line_to(x2, y2)
            ctx.stroke()

    def on_button_press(self, widget, event):
        if event.button != 1:
            return False

        if len(self.lines) == 0 or len(self.lines[-1]) == 4:
            self.lines.append([event.x, event.y])
        else:
            self.lines[-1].extend([event.x, event.y])

        widget.queue_draw()
        return True

o = Okno()
Gtk.main()
