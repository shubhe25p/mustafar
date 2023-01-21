import io
import os
import warnings
from PIL import Image
from stability_sdk import client
import cv2
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
stability_api = client.StabilityInference(
    key='sk-vSTOSKxpVYvN54rEO8fGo4XXHiflxdedpipngg9dL8sqGznq', 
    verbose=True,
)
answers = stability_api.generate(
    prompt="houston, we are a 'go' for launch!"
)
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img.save('output.png')