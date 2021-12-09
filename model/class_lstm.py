class Lstm(BasicModel): 

    def build (self):
        super().build()
        sequenceLength = 5 
        self.nClasses = 1
        self.model = Sequential()
        temp = tf.keras.layers.LSTM(
            units = self.nClasses,
            input_shape=(sequenceLength , 1 ),
            activation="tanh",
            recurrent_activation="sigmoid",
            use_bias=True,
            kernel_initializer="glorot_uniform",
            recurrent_initializer="orthogonal",
            bias_initializer="zeros",
            unit_forget_bias=True,
            kernel_regularizer=None,
            recurrent_regularizer=None,
            bias_regularizer=None,
            activity_regularizer=None,
            kernel_constraint=None,
            recurrent_constraint=None,
            bias_constraint=None,
            dropout=0.0,
            recurrent_dropout=0.0,
            return_sequences=True,
            return_state=False,
            go_backwards=False,
            stateful=False,
            time_major=False,
            unroll=False )

        self.model.add(temp)
        self.model.add(Dense(self.nClasses))
        self.model.add(Activation('softmax'))
        
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        handler.train_x = [ 11 , 52 , 66 , 88 , 91 , 100 , 1.1 , 11 , 52 , 66 , 88 , 91 , 100 , 1.1 ]
        handler.train_y = [ 1 , 2  ,  1 , 2  , 1 ,  1  , 2 , 1 , 2  ,  1 , 2  , 1 ,  1  , 2]

        handler.test_x = [ 11 , 52 , 66 , 88 , 91 , 100 , 1.1 , 11 , 52 , 66 , 88 , 91 , 100 , 1.1 ]
        handler.test_y = [ 1 , 2  ,  1 , 2  , 1 ,  1  , 2 , 1 , 2  ,  1 , 2  , 1 ,  1  , 2]

        self.batchize_data(sequenceLength)
