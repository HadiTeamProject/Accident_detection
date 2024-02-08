import numpy as np
import tensorflow as tf

class AccidentDetectionModel(object):
    class_nums = ['Accident', 'No Accident', 'Fire']

    def __init__(self, tflite_model_file):
        self.interpreter = tf.lite.Interpreter(model_path=tflite_model_file)
        self.interpreter.allocate_tensors()

    def predict_accident(self, img):
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()

        img = np.expand_dims(img, axis=0).astype(np.float32)
        self.interpreter.set_tensor(input_details[0]['index'], img)
        self.interpreter.invoke()
        preds = self.interpreter.get_tensor(output_details[0]['index'])

        return AccidentDetectionModel.class_nums[np.argmax(preds)], preds