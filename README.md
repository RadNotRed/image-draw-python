# image-draw-python
Turning images into mouse movement. Can be used for Cash App card designs! (Like what I used it for)

This program automates drawing by converting an image into mouse movements. You can partner it with **[Phone Link](https://apps.microsoft.com/detail/9NMPJ99VJBWV)** (Windows only) to draw directly on your phone using screen mirroring.

---

## 📌 Installation Instructions  

### **1. Clone the Repository**  
```sh
git clone https://github.com/RadNotRed/image-draw-python.git
cd image-draw-python
```

### **2. Set Up a Virtual Environment**  
Create and activate a virtual environment to manage dependencies:  

- **Windows (PowerShell):**  
  ```sh
  python -m venv .venv
  .\.venv\Scripts\activate
  ```

- **macOS/Linux:**  
  ```sh
  python -m venv .venv
  source .venv/bin/activate
  ```

### **3. Install Dependencies**  
Run the following command to install the required packages:  
```sh
pip install -r requirements.txt
```

---

## 🚀 Usage  

1. Place your image in the `images/` folder (e.g., `spiderweb.png`).
2. Run the script:  
   ```sh
   python main.py
   ```
3. The program will process the image and simulate mouse movements to "draw" it.

💡 **Tip:** If you're using **Phone Link**, enable screen mirroring to draw directly on your phone screen!

---

## 📦 Dependencies  
This program uses:
- `pyautogui` - Automates mouse movement and clicks  
- `pillow (PIL)` - Handles image processing  
- `tqdm` - Displays progress bars  
- `keyboard` - Detects key presses (used for ESC key to cancel drawing)  

Make sure they are installed via `requirements.txt`.

---

## 📜 License  
This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.  
See the [LICENSE](LICENSE) file for more details.

---
