pip install torch
pip install tensorboardX
pip install progress
pip install torchvision
pip install cuda-python
cd MixMatch-pytorch
python3 train.py --gpu 0 --n-labeled 250 --train-iteration 10 --epochs 3 --out new_out
