import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy

def main():
	model = load_model("saved_models/best_model.keras")
	test_ds = tf.data.Dataset.load('data/test_data')

	pre = Precision()       # What proportion of fog predictions was actually real fog? (TP/ TP + FP)
	re = Recall()           # What proportion of actual fog was corrected identified? (TP / TP + FN)
	acc = BinaryAccuracy()  # Accuracy for binary classification

	for batch in test_ds.as_numpy_iterator():
		X, y = batch
		yhat = model.predict(X)

		predicted = []
		predicted = yhat>0.5
		print("True labels: ", y)
		print("Predicted labels: ", predicted.flatten())

		pre.update_state(y, yhat)
		re.update_state(y, yhat)
		acc.update_state(y, yhat)

	return (pre.result().numpy(), re.result().numpy(), acc.result().numpy())

if __name__ == "__main__":
	results = main()
	print(f"Precision: {results[0]:.2f}, Recall: {results[1]:.2f}, Accuracy: {results[2]:.2f}")
	