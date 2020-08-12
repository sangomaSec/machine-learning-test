#!/usr/bin/env python
import argsparse




import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets


“”“
  rbr: return back rate in random walk with restart
”“”

parser = argparse.ArgumentParser(description='GCC traning net')

def main():
    args = parser.parse_args()
    main_worker(args)


def main_worker(args):
    """
    load datasets
    define model 
    compute loss loss.backward
    donnot forget the steps : random walk with restart, subgraph induction and anonymization
    """
    

def load_dataset():
    


def compute_loss(output, target):
    """
      compute loss by using CrossEntropyLoss
    """
    criterion = nn.CrossEntropyLoss.cuda()
    loss = criterion(output, target)
    return loss
