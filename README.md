# Emojifier - Emotion Recognition in Real-Time (no longer maintained)

***Project Structure***

	\
	|------ main_module.py
	|------ detect_face.py
	|------ image_enhance.py
	|------ prepare_model.py
	|------ process_dataset.py

 1. **detect_face.py** : Responsible for finding, detecting, cropping and normalizing input images.
 2. **process_dataset.py**: Responsible for harvesting the data set from the local computer and use _detect_face.py_ to normalize the images. Also organizes the raw data set.
 3. **image_enhance.py**: Responsible for image enhancement and color corrections.
 4. **prepare_module.py**: Responsible for getting the fisherface classifier and prepare the model. It uses _image_enhance.py_
 5. **main_module.py**: This is the main module of the projects which implements all the code, processing data, image enhancement, preparing and training model. It also maps an image (i.e represents the corresponding emotion which is predicted by the model ) to the mapped faced on the camera output.
## To run this project
1. This project is using CK+ image dataset [link](http://www.consortium.ri.cmu.edu/ckagree/)
2. Put CK emotions dataset inside /data/ folder following tips from  [Paul van Gent's blog post](http://www.paulvangent.com/2016/04/01/emotion-recognition-with-python-opencv-and-a-face-dataset/)
3.  Run process_dataset.py. It harvests dataset and puts neutral and emotions images into /data/sorted_set/, it also normalizes them
4.  Run prepare_model.py to teach a model using /data/sorted_set/ files. You can specify list emotions you want to use. It saves a teached model to /models/emotion_detection_model.xml
5.  Run main_module.py. It opens a webcam stream, detect emotions on faces (using /models/emotion_detection_model.xml) and changes them to specified emojis (/graphics/)

Here is the link to my research paper [link](https://github.com/Anandesh-Sharma/College/blob/master/Emojifier__Facial_Emotion_Recognition-2019-05-10-09-17.pdf)
