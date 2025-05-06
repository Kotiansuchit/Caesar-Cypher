from PIL import Image

def encrypt_image(image_path, output_path, method="invert"):
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size

    if method == "invert":
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (255 - r, 255 - g, 255 - b)

    elif method == "swap":
        for y in range(height):
            for x in range(width // 2):
                left = pixels[x, y]
                right = pixels[width - x - 1, y]
                pixels[x, y] = right
                pixels[width - x - 1, y] = left

    image.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    print("Simple Image Encryption Tool")
    img_path = input("Enter path to input image: ").strip()
    out_path = input("Enter path to save encrypted image: ").strip()
    method = input("Enter encryption method ('invert' or 'swap'): ").strip().lower()

    if method not in ["invert", "swap"]:
        print("Invalid method. Use 'invert' or 'swap'.")
        return

    encrypt_image(img_path, out_path, method)

if __name__ == "__main__":
    main()
