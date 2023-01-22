import io
import os
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from random import randint


def generate_img(city, planet):

    stability_api = client.StabilityInference(
        key='sk-vSTOSKxpVYvN54rEO8fGo4XXHiflxdedpipngg9dL8sqGznq', 
        verbose=True,
    )
    answers = stability_api.generate(
        prompt=manipulate_prompt(city,planet),
        seed=randint(1,100), # if provided, specifying a random seed makes results deterministic
        steps=30, # defaults to 30 if not specified
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save('../frontend/src/components/output.jpeg')
                return artifact.binary

def manipulate_prompt(city, planet):
    prompt = f"City on {planet} in the year 2050 with human habitats. Create realistic image with higher resolution of {city}"
    return prompt