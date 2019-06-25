import os
import numpy as np
import pandas as pd
import caffe
from PIL import Image
from tqdm import tqdm

mean_file = '../data/ilsvrc_2012_mean.npy'

net_full_conv = caffe.Net('../data/sentiment_fully_conv_deploy.prototxt', '../data/twitter_finetuned_test4_iter_180.caffemodel', caffe.TEST)

transformer = caffe.io.Transformer({'data': net_full_conv.blobs['data'].data.shape})
transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)

output = pd.DataFrame(columns=['neg', 'pos'])
metadata = pd.read_csv("../data/cleanImageIndex.csv", header=0)

for image in tqdm(list(metadata['name'])):
    im = caffe.io.load_image("../images/" + image + ".jpg")
    out = net_full_conv.forward_all(data=np.asarray([transformer.preprocess('data', im)]))
    df = pd.DataFrame(out['prob'][0].reshape(-1, len(out['prob'][0])), columns = ['neg', 'pos'])
    output.append(df)
    #im.flush()

output.save('../out/sentiment_output.csv', sep=",")
