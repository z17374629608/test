import tensorflow as tf
with tf.Session() as sess:
    new_saver=tf.train.import_meta_graph('.\data\my_weight-1000.meta')
    new_saver.restore(sess,tf.train.latest_checkpoint('.\data'))
    print(sess.run('w1:0'))
    print(sess.run('w2:0'))