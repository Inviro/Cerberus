import numpy as np
import cv2
import time

import sys
import os

from google.cloud.automl_v1beta1.proto import service_pb2
from google.cloud import automl_v1beta1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (r"*******")

project_id = '******'
model_id = '*******'     # using Stances model

file_path = "stance-frame.jpg"     # name of frame saved 

source = 'jimmy-johns-robbery.mp4'

def get_prediction(content, project_id, model_id):
  prediction_client = automl_v1beta1.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

if __name__ == '__main__':

    cap = cv2.VideoCapture(source)

    font = cv2.FONT_HERSHEY_SIMPLEX

    count = 0

    while(cap.isOpened()):
        ret, frame = cap.read()

        height, width, channels = frame.shape
        
        count = count + 1
        
        # Checks agro every 30 frames
        if count > 30:
            cv2.imwrite(file_path, frame)     # save frame as JPEG file
            with open(file_path, 'rb') as ff:
                content = ff.read()

            # Gets prediction from model
            response = get_prediction(content, project_id,  model_id)
            
            for result in response.payload:
                print("Predicted class name: {}".format(result.display_name))
                print("Predicted class score: {}".format(result.classification.score))
                    
                if result.display_name == "AggroStance":
                    status = str(result.classification.score)

                else:
                    status = "No Threat"
            
            cv2.putText(frame, status, (50, (height - 50)), font, 3,(0, 0, 255),2,cv2.LINE_AA)
            small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
            cv2.imshow('checking', small)
            count = 0
            
        #cv2.imshow('frame', frame)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
