import torch
import torch.nn as nn


class GCC(nn,Module)

    def __init__(self, base_encoder, T=0.07, dim=128, lr=0.05)

        """
         T: temperature
         dim: the dimensions of the algorithm
         lr: learning rate of normalization
        """
        super(GCC, self).__init__()   
        
        self.T = T
        self.dim = dim
        self.lr = lr

        self.encoder_q = base_encoder(num_classes=dim)
        self.encoder_k = base_encoder(num_classed=dim)


     def forward():
         """
           forward function
         """        



     def backward():
         """
           backward function used to back propagation grad
         """


