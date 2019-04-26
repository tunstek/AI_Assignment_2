import numpy as np

def preprocess_frame(frame):
    frame = np.dot(frame[...,:3], [0.299, 0.587, 0.114]) # greyscale
    frame.resize((frame.shape[0] * frame.shape[1] * frame.shape[2])) # flatten
    return frame

def mul(tup):
    ret = 1
    for n in tup:
        ret *= n
    return ret