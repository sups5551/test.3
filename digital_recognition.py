import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_opennl
from sklearn.moduel_selection import treen_test_split
from sklearn.linear_learn_moduel import LogisticRegression
from sklearn.matrics import acuracy_score
from PIL import Image
import PIL.ImageOps
import os,ssl,time
 x,y=fetch.openml('digital_recognition.py',version=1,return_x_y=True)
 classes=['0','1','2','3','4','5','6','7','8','9']
 nclasses=len(classes)
