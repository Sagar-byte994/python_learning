import qrcode

from qr_code_generators import generate_trolley_id


def generate_qr_code(data, xyz_path, qr_foreground_colour, qr_background_colour):

    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction level
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of border (boxes)
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color=qr_foreground_colour, back_color=qr_background_colour)

    # Save the image
    img.save(xyz_path)

    print("QR code saved as qr_code.png")


def generate_trolley_id():
    n = 5
    trolley_ids = ("aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee")
    qr_background_colour = "white"
    qr_foreground_colour = "black"
    for data in trolley_ids:
        xyz_path = "qr_code_bbb/abc" + data + ".png"
        generate_qr_code(data, xyz_path, qr_foreground_colour, qr_background_colour)

def generate_trolley_position():
    n = 5
    qr_background_colour = "white"
    qr_foreground_colour = "black"
    for i in range(1, n + 1):
       xyz_path = "qr_code_aaa/qr_code"+ str(i) +".png"
       generate_qr_code (i, xyz_path, qr_foreground_colour, qr_background_colour)

def main():
    generate_trolley_position()
    generate_trolley_id()


if __name__=="__main__":
    main()