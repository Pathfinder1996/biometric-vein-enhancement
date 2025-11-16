## Vein Feature Enhancement Algorithm

This repository provides a Python implementation of the vein enhancement method proposed by Hong et al [1].

## Contents
- `vein_enhance.py` - Main implementation of the enhancement algorithm.
- `requirements.txt` - Python 3.9.2 dependency list.

## Example Results (Click the thumbnails to enlarge)

| Input Image | Enhanced Result |
|-------------|-----------------|
| ![Input](image/input.png) | ![Enhanced](image/enhanced.png) |

## How to Use
Install the required Python packages:
```
pip install -r .\requirements.txt
```
Set the variable `image_path` inside `vein_enhance.py` to your test image, then run:
```
python .\vein_enhance.py 
```
The enhanced image will be saved to the output path defined in the script.

## Reference
[1] IEEE Transactions on Industrial Informatics: [Recognizing Palm Vein in Smartphones Using RGB Images](https://ieeexplore.ieee.org/document/9648012)
