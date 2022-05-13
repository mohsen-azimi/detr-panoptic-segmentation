# PANOPTIC SEGMENTATION USING DETR

## Directions to try out Bounding Box Predictions
1. [Open this link which directs to the Colab file](https://colab.research.google.com/drive/15O413og2oirRTu2zIwqKYb0GeMhUo8BQ?usp=sharing) where you can try out predictions on your own images, or see the results of predictions done already.
2. Save a copy of this colab file and follow the below steps there.
    - `File` -> `Save a copy in Drive`
3. Download this [weights file and upload it in your drive](https://drive.google.com/file/d/1K_sIyMr-qzKgnBUSK4CV_2bhU0m5sBik/view?usp=sharing).
4. Once uploaded, [visit this cell in opened colab file](https://colab.research.google.com/drive/15O413og2oirRTu2zIwqKYb0GeMhUo8BQ?authuser=1#scrollTo=5NaMGhGfwg0C&line=1&uniqifier=1).
5. In that cell, in line number 3, change path to wherever you have uploaded the models file downloaded in step [3].
6. Once changed, open this [link](https://colab.research.google.com/drive/15O413og2oirRTu2zIwqKYb0GeMhUo8BQ?authuser=1#scrollTo=U_wDp99daNb1&line=21&uniqifier=1) and paste any image url in `line 1` for which you want to visualize the predictions.
7. Once done, go to `Runtime` -> `Run all`.
8. It will prompt to validate drive access after a while, to be able to access the specified models weights file.
9. The output of the final cell wil be the predictions of the image provided.
