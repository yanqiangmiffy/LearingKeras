#序贯模型
from keras.models import Sequential
from keras.layers import Dense,Activation
#创建一个Sequential模型
model=Sequential([
    Dense(32,units=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax')
])