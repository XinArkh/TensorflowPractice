from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# mnist = input_data.read_data_sets(
#     'E:\\Python\\Python3.5.4_64\\Lib\\site-packages\\tensorflow\\contrib\\learn\\python\\learn\\datasets\\MNIST_data\\',
#     one_hot=True)
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
# print('\n', mnist.train.images.shape, mnist.train.labels.shape)
# print('\n', mnist.test.images.shape, mnist.test.labels.shape)
# print('\n', mnist.validation.images.shape, mnist.validation.labels.shape)

# sess = tf.InteractiveSession()
sess = tf.Session()

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * \
                               tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# tf.global_variables_initializer().run()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    # train_step.run({x: batch_xs, y_: batch_ys})
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# print(accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))
print(
    sess.run(
        accuracy,
        feed_dict={
            x: mnist.test.images,
            y_: mnist.test.labels}))
# sess.close()
