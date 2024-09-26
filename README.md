# Implementing CNN to detect fog in images

In an independent study project in Fall 2023, I learned how to pre-process and classify fog photos by implementing an input pipeline and a Convolutional Neural Network using Tensorflow.

<img width="40%" alt="prediction" src="https://github.com/autumn-yng/cnn_fog/assets/92401509/574c2884-22bb-4e45-a199-fa60d9c3b36d">

<img width="38%" alt="prediction" src="https://github.com/autumn-yng/cnn_fog/assets/92401509/c57d253a-0dfe-4e85-9753-e5115e716873">

## Motivation
In the summer of 2023, I did research on [coastal fog](https://github.com/autumn-yng/summerfog/tree/main) at UW's Friday Harbor Labs. One part of our research was looking at fog frequency from field photos, which were taken every 30 minutes by the cameras that we set up around the island. The research team had been manually looking through the thousands of photos to record when there was fog when I decided that I wanted something more efficient. 

I trained a Support Vector Machine model to detect fog in the photos, which saved us a lot of manual work. It still took several hours to rescale the photos and train and validate the model; and it didn't reach 100% accuracy, which was fine for the summer research, but I kept thinking if I could find a better Machine Learning model for this. As I had seen Convolutional Neural Network (CNN) at a lot of places when reading about Computer Vision, after the summer, I proposed an independent study project at Mount Holyoke to self-learn CNN. 

## Results
After various Tensorflow tutorials and many struggles, I was able to design a Tensorflow input pipeline and a CNN model that does in **a few minutes** what the SVM did in hours. The CNN also reached **100% Precision**, **100% Recall**, totaling 100% accuracy. Aside from my own learning purpose, I hope the CNN I trained can be helpful in supporting coastal fog research 🌫🌊. I also created two tutorial videos and a Juptyter Notebook with detailed documentation! 

## Input pipeline, Model Training and Testing, Performance Visualization
All of these are explained in details in the ipynb file.

## My tutorial videos about CNN
### Image Convolution, Input and Output in CNN
I found it especially challenging to bridge the gap between understanding the basic concept of CNN and understanding the parameters of a real CNN model, even the most basic one. Even when I had understood what is a neural network, what is image convolution, and even when I knew the definitions of the parameters (like the first parameter is the number of kernels, the second is the shape of the kernel, etc.), I struggled to connect the dots and to understand the output of `model.summary()`. After many days digging into both the Computer Vision and Machine Learning concepts related to CNN, I have finally felt like I understood it well. I recorded this video, hoping that it would help future students like my past self have an easier time understanding this topic.

[<img width="50%" src="https://github.com/autumn-yng/cnn_fog/assets/92401509/f5642e9c-0ecc-4dac-8c5b-e8771ec46d9a">](https://youtu.be/XELqHT8wkvg?si=obOYN3964Z6IC4-e)

### Parameters in CNN
[<img width="50%" src="https://github.com/autumn-yng/cnn_fog/assets/92401509/64214071-5820-49f7-b324-bde00e32306f">](https://youtu.be/nHYKOQ9-YZI?si=5AGJocq47gZMWUCG)

## Acknowledgement
I am very thankful for
- Professor Alyx Burns, the mentor who had helped me reflect on my progress and given me advice on my plan during our consistent weekly meeting throughout the semester.
- Professor Melody Su, the professor who had taught me Computer Vision and spared time to discuss with me all questions I had about Machine Learning.

## Resources
These resources have been particularly helpful for me during the semester:
- Nicholas Rennotte's [CNN tutorial](https://youtu.be/jztwpsIzEGc?si=9XTNDnWZUwyz8kMa)
- Lawrence Moroney's [Machine Learning, Computer Vision, and CNN course](https://developers.google.com/codelabs/tensorflow-4-cnns#0)
