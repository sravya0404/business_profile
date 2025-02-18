import qrcode

# Replace this URL with your GitHub Pages URL
profile_url = "https://sravya0404.github.io/business_profile/"  # Replace with your actual URL

# Generate the QR code
qr = qrcode.make(profile_url)

# Save the QR code image
qr.save("business_qr_code.png")

print("QR Code saved as business_qr_code.png")