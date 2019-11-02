import tensorflow as tf


w1=tf.Variable([1.,2.],dtype=tf.float32,name='w1')
w2=tf.Variable([3.,2.],dtype=tf.float32,name='w2')
sess=tf.Session()
saves=tf.train.Saver()
sess.run(tf.global_variables_initializer())
saves.save(sess,'./data/my_weight',global_step=1000)