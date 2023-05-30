import tensorflow as tf

h = tf.constant("hello")
w = tf.constant("world")

hw = h + w

with tf.version() as sess:
    ans = sess.run(hw)

print(ans)

