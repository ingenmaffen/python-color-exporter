import png

def export(width, height, red, green, blue, filename):
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            row = row + (red, green, blue)
        img.append(row)
    with open(filename + '.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)
