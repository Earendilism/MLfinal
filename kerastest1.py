import tensorflow as tf
#import matplotlib.pyplot as plt

fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
(x_train_full, y_train_full), (x_test, y_test) = fashion_mnist
x_train, y_train = x_train_full[:-5000], y_train_full[:-5000]
x_valid, y_valid = x_train_full[-5000:], y_train_full[-5000:]
# fig, axes = plt.subplots(10, 10, gridspec_kw={'wspace': 0, 'hspace': .5})
dict_name = {0: 'T-shirt/top', 1: 'Trouser', 2: 'Pullover', 3: 'Dress',
             4: 'Coat', 5: 'Sandal', 6: 'Shirt', 7: 'Sneaker', 8: 'Bag',
             9: 'Ankle boot'}
tf.random.set_seed(42)
model = tf.keras.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=[28, 28]))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(300, activation="relu"))
model.add(tf.keras.layers.Dense(100, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))
model.compile(
    loss="sparse_categorical_crossentropy", optimizer="sgd",
    metrics=["accuracy"])
model.fit(x_train, y_train, epochs=30, validation_data=(x_valid, y_valid))
