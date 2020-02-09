Answers to questions 
====================

Summary Table
-------------


|Item | Number|
|-----|-------|
|Total Images| 40 |
|Dog Images| 30 |
|Not-a-Dog Images| 10 |


|CNN Model Architecture | % Not-a-Dog Correct | % Dog Correct | % Breeds Correct | % Match Labels | Time taken |
|-----------------------|--------------------:|--------------:|-----------------:|--------------: |-----------:|
|AlexNet                |      100.00%        |     100.00%   |    80.00%        |     75.00%     |   0:0:3    |
|ResNet                 |       90.00%        |     100.00%   |    90.00%        |     82.50%     |   0:0:6    |
|VGG                    |      100.00%        |     100.00%   |    93.33%        |     87.50%     |   0:0:32   |



Objective 1: Identifying which pet images are of dogs and which pet images aren't of dogs
-----------------------------------------------------------------------------------------
AlexNet and VGG are on par regarding correctly idetifying which images are showing dogs or other pets: 100% accuracy.
ResNet only has a 90% accuracy for Not-A-Dog.



Objective 2: Classifying the breeds of dogs, for the images that are of dogs
-----------------------------------------------------------------------------
The best architecture at predicting dog breeds is VGG at 93.33%, vs 90% for ResNet and 80% for AlexNet.
It is worth noting that these extra 3.33% accuracy come at a heavy cost of 32 seconds of processing time, which ten times more than AlexNet.