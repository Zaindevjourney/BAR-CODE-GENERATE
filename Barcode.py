                             # GENERATING BARCODE #

import barcode
from barcode.writer import ImageWriter
from PIL import Image as PILImage

def generate_barcode(data):
    code = barcode.get('code128', data, writer=ImageWriter())
    barcode_filename = code.save("barcode")
    print("Barcode generated.")

    # Open the barcode image using Pillow
    img = PILImage.open(f"{barcode_filename}.png")
    img.show()  # This will open the image using the default image viewer

data = "1234-5678-9058"
generate_barcode(data)