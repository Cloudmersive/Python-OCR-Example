import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException

import sys
import os.path
print (sys.path[0])


api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
image_file = sys.path[0] + '\\example_hebrew.png' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.

language="HEB"

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '04d1a7be-c9d1-4d93-8ec4-e7545c2a570a'

try:
    # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
    api_response = api_instance.image_ocr_post(image_file,language=language)
    print(api_response)
except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)