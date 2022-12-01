import pickle
import os
import numpy as np

print(pickle.format_version)
img = load_img('./IMG_1306.jpg', target_size=(100, 100))
x = img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
model = pickle.load(open('history.pkl', 'rb'))
print(model.predict(images, batch_size=10))