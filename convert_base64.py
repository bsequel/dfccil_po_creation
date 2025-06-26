import os
import requests
import base64
import json




def convertobase64(file):
        file_text = open(file, 'rb')
        file_read = file_text.read()
        file_encode = base64.encodebytes(file_read).decode('utf-8')

        # Determine file type and data type accordingly
        if file.lower().endswith('.pdf'):
            data_type = 'data:application/pdf;base64,'

        elif file.lower().endswith(('.png')):
            data_type = 'data:image/png;base64,'

        elif file.lower().endswith(('.jpeg')):
            data_type = 'data:image/jpeg;base64,'

        elif file.lower().endswith(('.jpg')):
            data_type = 'data:image/jpg;base64,'

        else:
            raise ValueError('Unsupported file type')
        
        # Add data type before base64 string
        # "file": data_type
        base64_with_data_type = data_type + file_encode

        return base64_with_data_type.replace('\n','')