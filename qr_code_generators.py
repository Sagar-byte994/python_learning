# import qrcode
#
# from QR_code_generator import generate_trolley_id
#
#
#
# def make_qr_code(data, save_path, qr_foreground_colour, qr_background_colour ):
#
#     # Create a QR Code instance
#
#     qr = qrcode.QRCode(
#         version=1,  # controls the size of the QR code (1 to 40)
#         error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction level
#         box_size=10,  # size of each box in pixels
#         border=4,  # thickness of border (boxes)
#     )
#
#     # Add data to the QR code
#     qr.add_data(data)
#     qr.make(fit=True)
#
#     # Create an image from the QR Code instance
#     img = qr.make_image(fill_color=qr_foreground_colour, back_color=qr_background_colour)
#
#     # Save the image
#     img.save(save_path)
#
#     print("QR code saved as ")
#
#     # Data to encode
#     data = 123
#
#
# def generate_trolley_id():
#     n = 24
#     trolley_ids =("TSG000001AA", "TSG000002AA", "TSG000003AA", "TSG000004AA")
#     qr_background_colour = "white"
#     qr_foreground_colour = "black"
#     for data in trolley_ids:
#         save_path = "qr_code_xyz/abc" + data + ".png"
#         make_qr_code(data=data, save_path=save_path, qr_foreground_colour=qr_foreground_colour, qr_background_colour=qr_background_colour)
#
#
# def generate_trolley_position():
#     n = 24
#     qr_background_colour = "white"
#     qr_foreground_colour = "black"
#     for x in range (1, n + 1):
#         save_path = "qr_code_abc/abc" + str(x) + ".png"
#         make_qr_code(data=x, save_path=save_path, qr_foreground_colour=qr_foreground_colour, qr_background_colour=qr_background_colour)
#
#
# def main():
#     generate_trolley_id()
#     generate_trolley_position()
#
# if __name__=="__main__":
#     main()