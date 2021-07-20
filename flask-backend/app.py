# from flask import Flask, request
# from flask_cors import CORS
# import json
# from face_rec import FaceRec, rodrigo
# from PIL import Image
# import base64
# import io
# import os
# import shutil
# import time


# app = Flask(__name__)
# CORS(app)


# @app.route('/api', methods=['POST', 'GET'])
# def api():
# 	data = request.get_json()
# 	resp = 'Nobody'
# 	directory = './stranger'
# 	if data:
# 		if os.path.exists(directory):
# 			shutil.rmtree(directory)

# 		if not os.path.exists(directory):
# 			try:
# 				os.mkdir(directory)
# 				time.sleep(1)
# 				result = data['data']
# 				b = bytes(result, 'utf-8')
# 				image = b[b.find(b'/9'):]
# 				im = Image.open(io.BytesIO(base64.b64decode(image)))
# 				im.save(directory+'/stranger.jpeg')

# 				if your-name.recognize_faces() == 'your-name':
# 					resp = 'your-name'
# 				else:
# 					resp = 'Nobody'
# 			except:
# 				pass
# 	return resp


	







# if __name__ == '__main__':
# 	app.run()