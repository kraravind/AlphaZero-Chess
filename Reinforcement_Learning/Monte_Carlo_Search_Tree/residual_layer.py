from Reinforcement_Learning.Monte_Carlo_Search_Tree.convolutional_layer import convolution
import torch
import torch.nn as nn
'''
This is the residual layer to the NN, the structure is:

Input -> 256 convolutional filters (3x3) -> Batch Normalization -> Rectifier non-linearity ->
256 convolutional filters (3x3) -> Batch Normalization -> Skip Connection -> Rectifier non-linearity
'''

class residual():


    def main(self, residu):
        self.resid = residu
        self.skip = self.resid

        self.convo = convolution()

        self.resid = self.convo.main(self.resid)

        self.resid = self.convo.layer_convolutional(self.resid)
        self.resid = self.convo.batch_normalization(self.resid)

        self.resid += self.skip

        self.resid = self.convo.rectifier_non_linearity(self.resid)

        return self.resid