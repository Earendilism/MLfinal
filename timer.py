from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color



filename = "timer_python.gif"
bg_color = "white"
seconds = 1 * 60

# Generate time labels
def nice_time(seconds):
    m, s = divmod(seconds, 60)
    # m can be subdivided to hours if needed:
    # h, m = divmod(m, 60)
    return("{0:02d}:{1:02d}".format(m, s))

# from datetime import timedelta
# lambda x: str(timedelta(seconds=x)) works great, but it doesn't let you
# format the string however you want

labels = list(map(nice_time, reversed(range(seconds + 1))))

with Image() as gif:
    for label in labels:
        with Drawing() as draw:
            draw.font = "SourceSansPro-Light.otf"
            draw.font_size = 140
            draw.text_alignment = "center"
            draw.text_antialias = True

            with Image(width=600, height=400, background=Color(bg_color)) as img:
                x = int(img.width / 2)
                y = int(img.height / 2)
                draw.text(x, y, label)
                draw.draw(img)
                gif.sequence.append(img)

    for frame in gif.sequence:
        with frame:
            frame.delay = 100  # Centiseconds

    gif.save(filename=filename)