import cv2
import numpy as np

# Global variables
biasX = 0
biasY = 0
scaleFactor = 2.0
gammaValue = 1.0
laplacianDelta = 0.0
roiMargin = 0.1
guideCircleRadiusFactor = 0.3
lineThickness = 2
circleRadian = 6
lineColor = (120, 120, 120)
circleColor = (100, 100, 100)
whiteArea_threshold = 0.75
roiShape_threshold = 0.7

# Automatic Gamma Correction
def AGC(src, gamma, isAutoMode=True):

    if src is None:
        return src

    c = 1.0
    d = 1.0 / 255.0

    if isAutoMode:
        mean_val = np.mean(src) / 255.0
        if mean_val > 0:
            c = np.log10(0.5) / np.log10(mean_val)
        else:
            c = 1.0

    gamma *= c

    # Build LUT
    lut = np.zeros((256,), dtype=np.uint8)
    for i in range(256):
        v = (i * d) ** gamma * 255.0
        v = np.clip(v, 0.0, 255.0)
        lut[i] = int(v)

    return cv2.LUT(src, lut)

# Vein enhancement
def enhanceVein(src):

    if src is None or src.size == 0:
        print("[ERROR] enhanceVein(): Null image")
        return src

    # 1. Gamma correction (AGC)
    src = AGC(src, gammaValue, True)

    # 2. CLAHE (clipLimit=2, tileGrid=4x4)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    src = clahe.apply(src)

    # 3. Convert to float64
    src = src.astype(np.float64) / 255.0

    # 4. GaussianBlur sigma=3
    src = cv2.GaussianBlur(src, (0, 0), sigmaX=3)

    # 5. Laplacian (same parameters)
    src = cv2.Laplacian(src, cv2.CV_64F, ksize=1, scale=1, delta=laplacianDelta)

    # 6. Clamp negative to 0
    src = np.maximum(src, 0.0)

    # 7. Normalize using max(-min, max)
    lap_min = src.min()
    lap_max = src.max()
    denom = max(-lap_min, lap_max)
    scale = 255.0 / denom if denom != 0 else 1.0

    src *= scale

    # 8. Convert to 8-bit
    src = np.clip(src, 0, 255).astype(np.uint8)

    return src

if __name__ == "__main__":

    image_path = "0.png"
    output_path = "0_enhanced.png"

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"[ERROR] Cannot load image: {image_path}")
    else:

        img = cv2.resize(img, (64, 64))

        result = enhanceVein(img)

        ok = cv2.imwrite(output_path, result)
        if ok:
            print(f"[INFO] Saved enhanced image to {output_path}")
        else:
            print(f"[ERROR] Failed to save {output_path}")
