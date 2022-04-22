from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os


class GarbagePredictor:
    def __init__(self):
        ENDPOINT = os.environ.get('GARBAGE_ENDPOINT')
        predictionKey = os.environ.get('GARBAGE_PREDICTION_KEY')
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": predictionKey})
        self.project_id = os.environ.get('GARBAGE_PROJECT_ID')
        self.published_name = os.environ.get('GARBAGE_PUBLISHED_NAME')
        self.predictor = CustomVisionPredictionClient(endpoint=ENDPOINT, credentials=prediction_credentials)
    
    def classify(self, imgData):
        # print(imgData)
        with open(imgData, "rb") as image_contents:

        #  r = predictor.classify_image(
        # project.id, publish_iteration_name, image_contents.read()
            results = self.predictor.classify_image(project_id= self.project_id, published_name=self.published_name, image_data=image_contents.read())
            # results = self.predictor.classify_image_url("project-Id", "Iteration-Id", url=imgData)
            result=""
            if(results.predictions[0].tag_name=="positive"):
                result="Recyclable"
            else:
                result="Not Recyclable"
            return result

        
gp = GarbagePredictor()
