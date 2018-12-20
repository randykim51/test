import tensorflow as tf

a = tf.constant("Hello, man")

with tf.Session() as sess:
    sess.run(a)

