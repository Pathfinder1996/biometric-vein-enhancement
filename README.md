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
[1] S.-J. Horng, D.-T.Vu, T.-V. Nguyen,W. Zhou, and C.-T. Lin, ‘‘Recognizing
palm vein in smartphones using RGB images,’’ *IEEE Trans. Ind. Informat.*,
vol. 18, no. 9, pp. 5992–6002, Sep. 2022, doi: 10.1109/TII.2021.3134016.
