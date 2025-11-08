import qrcode
from PIL import Image
import cv2
import os

def text_to_qr(text, output_file='qr_code.png'):
    """Converts a string of text into a QR code image."""
    length = len(text)
    box_size = min(20, max(5, length // 10))
    border = 4

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"[+] QR Code saved as '{output_file}' with size {img.size}")

def qr_to_text(image_path, output_file='qr_output.txt'):
    """Decodes a QR code image and saves the resulting text to a file."""
    img = cv2.imread(image_path)
    if img is None:
        print("[-] Failed to load image. Check the file path.")
        return

    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(img)

    if data:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"[+] Decoded text saved to '{output_file}'")
    else:
        print("[-] No QR code detected in the image.")

def main():
    """Main function for the QR Code Terminal App."""
    print("=== QR Code Terminal App ===")
    print("1. Convert Text/URL to QR Code")
    print("2. Decode QR Code Image to Text")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == '1':
        text_input = input("Enter text or path to a .txt file: ").strip()

        if text_input.endswith('.txt') and os.path.exists(text_input):
            try:
                with open(text_input, 'r', encoding='utf-8') as file:
                    text = file.read()
                print(f"[+] Loaded text from '{text_input}'")
            except Exception as e:
                print(f"[-] Error reading file: {e}")
                return
        else:
            text = text_input

        filename = input("Enter output image filename (default: qr_code.png): ").strip() or "qr_code.png"
        text_to_qr(text, filename)

    elif choice == '2':
        image_path = input("Enter the path to the QR code image: ").strip()
        output_file = input("Enter output text filename (default: qr_output.txt): ").strip() or "qr_output.txt"
        qr_to_text(image_path, output_file)

    else:
        print("[-] Invalid choice.")

if __name__ == '__main__':
    main()
