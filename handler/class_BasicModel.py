# fit() is for training the model with the given inputs (and corresponding training labels).
# evaluate() is for evaluating the already trained model using the validation (or test) data and the corresponding labels. Returns the loss value and metrics values for the model.
# predict() is for the actual prediction. It generates output predictions for the input samples.

class BasicModel (object):
    ################
    ## constructor
    ################
    def __init__(self):
        self.model = None
        self.name = type(self).__name__
        self.loadPath = ''
        self.savePath = ''

        self.loopEpochs = 10
        self.loopStatus = 0 
        self.loopLimit = 1000

        self.tp = 0
        self.tn = 0
        self.fp = 0
        self.fn = 0
        self.cm = []
        
        self.allAcc = []
        self.allLoss = []
        self.loss = 0
        self.acc = 0

        self.accuracy = 0
        self.precision = 0
        self.recall = 0
        self.f1 = 0

        print(">>> " + self.name + " model intiated ...")

    ################
    ## destructor
    ################
    def __del__(self):
        print("xxx deleted, model " + self.name)

    ################
    ## model retreival
    ################
    def build (self):
        print('>>> bulding ' + self.name + ' model ...')

    def load_model(self , path = None):
        print('>>> loading ' + self.name + ' model ...')
        if path:
            self.loadPath = path
        self.model = tf.keras.models.load_model(self.loadPath)

    def load_weights(self , path = None):
        print('>>> loading ' + self.name + ' weights ...')
        if path:
            self.loadPath = path
        self.model.load_weights(self.loadPath)

    ################
    ## model operations
    ################

    def program_0(self,ep = 5):
        self.train(ep)
        self.test()

    def program_1(self):
        self.predict()

    def loop_train(self):
        # 0 - load previous session weights , values
        for i in self.loopLimit - self.loopLimit:
            dataset.load_new_batch(i) # todo: implement
            self.train(self.loopEpochs)
            if (i % 2):
                pass
            else:
                pass
            # 3- save weights , values

    # verbose=0 will show you nothing (silent)
    # verbose=1 will show you an animated progress
    # verbose=2 will just mention the number of epoch 
    def train (self , epochs = 5):
        print('>>> training ' + self.name + ' model ...')
        self.model.fit(handler.train_x, handler.train_y, epochs , verbose=1)

    def test (self):
        print('>>> testing ' + self.name + ' model ...')
        self.loss, self.acc = self.model.evaluate(handler.test_x, handler.test_y, verbose=2)
        print('>>> Restored model, accuracy: {:5.2f}%'.format(100 * self.acc))

    def predict (self , smpl = None):
        print('>>> Predicting with ' + self.name + ' model ...')
        dataset.read_predict()
        if smpl:
            handler.predict_x = smpl
        handler.predict_y = self.model.predict(handler.predict_x)
        print('>>> predict_y:' , handler.predict_y)

    def inf_predict (self):
        while True :
            self.predict()

    def random_predict (self):
        print('>>> Random predict with ' + self.name + ' model ...')
        dataset.read_random()
        handler.predict_y = self.model.predict(handler.predict_x)
        print('>>> predict_y:' , handler.predict_y)

    ################
    ## saving model
    ################
    def save_weights(self, path = None): # saves the current weights
        if path:
            self.savePath = path
        if self.model == None:
            print("xxx No modle found for " + self.name)
        else:
            print('>>> saving ' + self.name + ' weights ...')
            self.model.save_weights(self.savePath) # saving weights only

    def save_model(self, path = None):
        if path :
            self.savePath = path
        if self.model == None:
            print("xxx No modle found for " + self.name)
        else:
            print('>>> saving ' + self.name + ' model ...')
            self.model.save(self.savePath) # saving the entire model

    def checkpoint(self, checkpoint_path = "cp.ckpt"): # saves the best weights
        if self.model == None:
            print("xxx No modle found for " + self.name)
            return -1
        else:
            return tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

    ################
    ## model detials
    ################
    
    def summery_plot(self , details = True, plotted = True):
        if self.model == None:
            print("xxx No modle found for " + self.name)
            return -1
        else:
            try:
                if(details):
                    self.summery()
                if(plotted):
                    self.plot()
            except Exception as e:
                print("xxx Error in summery_plot model")
            
    def plot(self):
        print('>>> plotting model: ' + self.name)
        tf.keras.utils.plot_model(self.model, to_file=self.name + '.png', show_shapes=True)

    def summery(self):
        print('>>> showing ' + self.name + ' summery ...')
        self.model.summary()

    ################
    ## accuracy
    ################

    def calculate_cm(self, y_actu , y_pred):
        self.cm = confusion_matrix(y_actu, y_pred)

    def calculate_results(self):
        [self.accuracy , self.precision , self.recall , self.f1] = results.get_results(self.tp , self.tn , self.fp , self.fn )

    def show_results(self):
        results.print_results(self.tp , self.tn , self.fp , self.fn )

    def show_graphs(self):
        graphs.plot_array(self.allAcc)
        graphs.plot_array(self.allLoss)