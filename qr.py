import qrcode

# Data to be encoded
data = "+251923036023"

# Create a QR code object
qr = qrcode.QRCode( # type: ignore
    version=1,  # Version of the QR code (size of the QR code)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level # type: ignore
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size in boxes
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
