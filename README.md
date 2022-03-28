# MixMatch
This is an unofficial PyTorch implementation of [MixMatch: A Holistic Approach to Semi-Supervised Learning](https://arxiv.org/abs/1905.02249). 
The official Tensorflow implementation is [here](https://github.com/google-research/mixmatch).


This repository carefully implemented important details of the official implementation to reproduce the results.


# Instructions to use on Custom dataset
1. Data should be kept inside custom_data folder.
2. In custom_data folder 2 folders named "labeled" and "unlabeled" to be there.
3. In "labeled" folder 2 folders named "train" and "test" will be there
4. In each "train" and "test" folders, there should be folders of different classes (can be any no.of classes)
4. In "unlabeled" folder all the unlabeled data to be there.


## Requirements
- Python 3.6+
- PyTorch 1.0
- **torchvision 0.2.2 (older versions are not compatible with this code)** 
- tensorboardX
- progress
- matplotlib
- numpy

## Usage
## My System commands
### Train
Train the model by 250 labeled data of CIFAR-10 dataset:
```
python3 train.py --gpu 0 --n-labeled 250 --train-iteration 10 --epochs 3 --out cifar10@250
```

```
python3 train.py --gpu 0 --n-labeled 250 --out cifar10@250
```

Train the model by 4000 labeled data of CIFAR-10 dataset:

```
python3 train.py --gpu 0 --n-labeled 4000 --out cifar10@4000
```

### Monitoring training progress
```
tensorboard --port 8008 --logdir cifar10@250### Train
```
## Default template commands
Train the model by 250 labeled data of CIFAR-10 dataset:

```
python3 train.py --gpu <gpu_id> --n-labeled 250 --out cifar10@250
```

Train the model by 4000 labeled data of CIFAR-10 dataset:

```
python3 train.py --gpu <gpu_id> --n-labeled 4000 --out cifar10@4000
```

### Monitoring training progress
```
tensorboard --port 6006 --logdir cifar10@250
```

## Results (Accuracy)
| #Labels | 250 | 500 | 1000 | 2000| 4000 |
|:---|:---:|:---:|:---:|:---:|:---:|
|Paper | 88.92 ± 0.87 | 90.35 ± 0.94 | 92.25 ± 0.32| 92.97 ± 0.15 |93.76 ± 0.06|
|This code | 88.71 | 88.96 | 90.52 | 92.23 | 93.52 |

(Results of this code were evaluated on 1 run. Results of 5 runs with different seeds will be updated later. )

## References
```
@article{berthelot2019mixmatch,
  title={MixMatch: A Holistic Approach to Semi-Supervised Learning},
  author={Berthelot, David and Carlini, Nicholas and Goodfellow, Ian and Papernot, Nicolas and Oliver, Avital and Raffel, Colin},
  journal={arXiv preprint arXiv:1905.02249},
  year={2019}
}
```
Forked from https://github.com/YU1ut/MixMatch-pytorch
