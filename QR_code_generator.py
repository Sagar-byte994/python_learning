from qrcode.main import QRCode
import qrcode



def generate_qrcode(data, save_path, qr_background_colour,  qr_forground_colour ):

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
    img = qr.make_image(fill_color=qr_forground_colour, back_color=qr_background_colour)

    # Save the image
    img.save(save_path)

    print("QR code saved as " + save_path)


def generate_trolley_id():
     n = 10
     trolley_id = ("TSG000001AA","TSG000002AA","TSG000003AA","TSG000004AA",)
     trolley_name = ("TSG000001AA", "TSG000002AA", "TSG000003AA", "TSG000004AA",)
     qr_background_colour = "white"
     qr_forground_colour = "black"
     for num in trolley_id:
         a = num
         b = "trolley_id/" + num + ".png"
         generate_qrcode(a, b, qr_background_colour, qr_forground_colour)


def generate_trolley_positions():
    n = 24
    qr_background_colour = "white"
    qr_forground_colour = "black"
    for i in range(1,n + 1):
        a = i
        b = "trolley_positions/trolley_position_" + str(i) + ".png"
        generate_qrcode(a, b, qr_background_colour, qr_forground_colour)

def main():
    pass
    generate_trolley_id()
    generate_trolley_positions()

if __name__=="__main__":
    main()
