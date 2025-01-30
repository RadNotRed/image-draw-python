import pyautogui
import time
import os
import keyboard
from PIL import Image
from tqdm import tqdm

pos1 = None
pos2 = None

# Coordinate setting
def set_coordinates():
    global pos1, pos2
    print("Hover over the first position and press 'Enter' to set it.")
    while pos1 is None:
        if pyautogui.confirm("Focus the popup and press 'Enter' while hovering the first position to set pos1", buttons=['OK']):
            pos1 = pyautogui.position()
            print(f"Set pos1: {pos1}")
            break

    print("Hover over the second position and press 'Enter' to set it.")
    while pos2 is None:
        if pyautogui.confirm("Focus the popup and press 'Enter' while hovering the second position to set pos2", buttons=['OK']):
            pos2 = pyautogui.position()
            print(f"Set pos2: {pos2}")
            break

# Select an image from the 'images' folder
def select_image():
    image_folder = "./images"
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not images:
        print("No images found in the 'images' folder. Please add images and try again.")
        exit()

    print("\nSelect an image to draw:")
    for idx, image in enumerate(images):
        print(f"{idx + 1}. {image}")

    while True:
        try:
            choice = int(input("\nEnter the number of the image you want to draw: ")) - 1
            if 0 <= choice < len(images):
                selected_image = os.path.join(image_folder, images[choice])
                print(f"Selected image: {selected_image}")
                return selected_image
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Rasterize image
def rasterize_image(image_path, downsample_factor=2):
    global pos1, pos2
    if not pos1 or not pos2:
        print("Coordinates not set. Please set pos1 and pos2 first.")
        return []

    # Downsample
    image = Image.open(image_path).convert("RGBA")  # Transparency handling
    width = abs(pos2.x - pos1.x) // downsample_factor
    height = abs(pos2.y - pos1.y) // downsample_factor
    image = image.resize((width, height))

    plan = []
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = image.getpixel((x, y))
            if a > 128 and (r + g + b) / 3 < 64:  # Opaque and very dark pixels
                plan.append((x * downsample_factor + pos1.x, y * downsample_factor + pos1.y))
    print(f"Generated drawing plan with {len(plan)} points after rasterizing.")
    return plan

def draw_plan(plan):
    print("Drawing on the screen. Please switch to the target application.")
    time.sleep(5)

    with tqdm(total=len(plan), desc="Drawing Progress", unit="point") as pbar:
        for point in plan:
            if keyboard.is_pressed("esc"):  # Check if ESC is pressed to cancel job
                print("\nDrawing canceled by user.")
                return
            pyautogui.moveTo(point[0], point[1])
            pyautogui.click()
            pbar.update(1)

def main():
    print("Step 1: Select an image to draw.")
    image_path = select_image()

    print("Step 2: Set coordinates (pos1 and pos2).")
    set_coordinates()

    print("Step 3: Rasterize the image.")
    rasterized_plan = rasterize_image(image_path, downsample_factor=2)

    print("Step 4: Start drawing on the target app. (Press ESC to cancel)")
    draw_plan(rasterized_plan)

if __name__ == "__main__":
    main()
