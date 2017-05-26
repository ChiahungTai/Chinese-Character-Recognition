#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:37:26 2017

@author: ctai
"""

import os
import os.path
import tensorflow as tf
from tensorflow.python.platform import gfile

INCEPTION_LOG_DIR = './inception5h'

if not os.path.exists(INCEPTION_LOG_DIR):
    os.makedirs(INCEPTION_LOG_DIR)
with tf.Session() as sess:
    model_filename = './tensorflow_inception_graph.pb'
    with gfile.FastGFile(model_filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    writer = tf.summary.FileWriter(INCEPTION_LOG_DIR, graph_def)
    writer.close()