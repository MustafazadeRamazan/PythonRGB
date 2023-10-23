import sys
import stdio

#sys.argv listesinin dördüncü numaranın varlığını kontrol ediyor
if sys.argv[4:]:
    stdio.writeln("Usage: python ders.py <red> <green> <blue>")
    sys.exit(1)


r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])

if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
    stdio.writeln("Invalid input. RGB values must be integers in the range 0-255.")
    sys.exit(1)

c = m = y = 0.0
k = 1.0

if r != 0 or g != 0 or b != 0:
    r, g, b = r / 255, g / 255, b / 255
    w = max(r, g, b)
    c = (w - r) / w
    m = (w - g) / w
    y = (w - b) / w
    k = 1 - w

stdio.writeln("cyan    = " + str(c))
stdio.writeln("magenta = " + str(m))
stdio.writeln("yellow  = " + str(y))
stdio.writeln("black   = " + str(k))