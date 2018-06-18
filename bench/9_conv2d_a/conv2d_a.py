#-----------------------------------------------------------------------------
#Copyright (c) 2018 Daniel Holanda Noronha, Bahar Salehpour, Steve Wilton
#{danielhn,bahars,stevew}@ece.ubc.ca
#Permission to use, copy, and modify this software and its documentation is
#hereby granted only under the following terms and conditions. Both the
#above copyright notice and this permission notice must appear in all copies
#of the software, derivative works or modified versions, and any portions
#thereof, and both notices must appear in supporting documentation.
#This software may be distributed (but not offered for sale or transferred
#for compensation) to third parties, provided such third parties agree to
#abide by the terms and conditions of this notice.
#THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHORS, AS
#WELL AS THE UNIVERSITY OF BRITISH COLUMBIA DISCLAIM ALL
#WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
#AUTHORS OR THE UNIVERSITY OF BRITISH COLUMBIA OR THE
#UNIVERSITY OF SYDNEY BE LIABLE FOR ANY SPECIAL, DIRECT,
#INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
#PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
#OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
#WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#---------------------------------------------------------------------------


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import string

size = 8
outputs = 2

weights_tensor=tf.Variable(tf.random_normal([3,3,1,outputs]))
X = tf.placeholder(tf.float32, [1, size,size,1])

original_image=np.random.rand(1,size,size,1)


with tf.Session() as sess:
    with tf.device("device:XLA_CPU:0"):
        y = tf.nn.conv2d(X, weights_tensor, strides=[1, 1, 1, 1], padding='SAME')
    sess.run(tf.global_variables_initializer())
    result = sess.run(y,{X: original_image})
    print(result)











