import qrcode
from PIL import Image
from pyfiglet import figlet_format
from colored import fore, style

def generate_qr(url, filename="qrcode.png"):
    """
    Generates a QR code from the given URL and saves it as an image file.

    Parameters:
    url (str): The URL to encode in the QR code.
    filename (str): The name of the file to save the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

    # Display the QR Code
    img.show()

def rgb_to_ansi256(r, g, b):
    return 16 + 36 * (r // 51) + 6 * (g // 51) + (b // 51)

def get_gradient_color(start_color, end_color, steps, step):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    r = int(r1 + (r2 - r1) * step / steps)
    g = int(g1 + (g2 - g1) * step / steps)
    b = int(b1 + (b2 - b1) * step / steps)
    return (r, g, b)

def gradient_text(text, start_color, end_color, steps):
    gradient_text = ""
    for i in range(steps):
        color = get_gradient_color(start_color, end_color, steps, i)
        ansi_color = rgb_to_ansi256(color[0], color[1], color[2])
        gradient_text += f"{fore(ansi_color)}{text[i % len(text)]}{style('reset')}"
    return gradient_text

def display_fontbees_name():
    """
    Displays the company name "FontBees" in a gradient color with a stylized format.
    """
    text = figlet_format("FontBees", font="slant")
    start_color = (0, 255, 0)  # Green
    end_color = (0, 0, 255)    # Blue
    steps = len(text)
    gradient_text_output = gradient_text(text, start_color, end_color, steps)
    print(gradient_text_output)

def main():
    """
    Main function that runs the QR code generator tool.
    """
    display_fontbees_name()  # Display "FontBees" with gradient effect

    # Always ask for the URL
    url = input("Enter the URL to generate QR Code: ")

    generate_qr(url)

if __name__ == "__main__":
    main()
