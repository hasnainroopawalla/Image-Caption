# Image Captioning using Uni-Directional and Bi-Directional LSTM

Execute 'run.py' in the 'Flickr' directory

The parent folder of this repository should contain the trained caption_model weights.

The Image Captioning Model is deployed as a REST API i.e., the web-app as well as our Flutter Application makes API calls to the server by sending an image and the server responds with a caption

The Web-App displays the Bidirectional as well as Uni directional Approaches side-by-side and also a table for the accuracy of each predicted word

# Test Results:
![Football players](https://github.com/hasnainroopawalla/Image-Captioning-Scene-Descriptor/blob/master/images/Capture.JPG)
![Snowy Scene](https://github.com/hasnainroopawalla/Image-Captioning-Scene-Descriptor/blob/master/images/Capture1.JPG)
![Surfboarding](https://github.com/hasnainroopawalla/Image-Captioning-Scene-Descriptor/blob/master/images/Capture4.JPG)
![Jumping Dog](https://github.com/hasnainroopawalla/Image-Captioning-Scene-Descriptor/blob/master/images/Capture7.JPG)

The BLEU Metric has been used to evaluate the test images. A higher BLEU rating (closer to 1) corresponds to an accurate description
