# coding=utf-8
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import hill
import logging
from cStringIO import StringIO
import base64


class MainHandler(webapp2.RequestHandler):
    html = u"""
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Hill Cipher | Text and Image Encryption</title>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">

        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css">

        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
    </head>
    <body>
        <form action="/" method="POST" enctype="multipart/form-data">
            <fieldset>
                <div class="container">
                    <div class="row" style="border: 1px solid black">
                        <div class="col-sm-12" style="text-align: center">
                            <legend>Le chiffrement de Hill</legend>
                        </div>
                    </div>
                    <div class="row" style="border: 1px solid black">
                        <div class="col-sm-6">
                            <legend>Chiffrement de texte</legend>
                            <p>
                                <label for="key">Clé</label>
                                <input type="text" name="key26" value="11 3 8 7">
                            </p>
                            <p>
                                <label for="inputText">Text Original</label>
                                <input type="text" name="inputText" value="%s">
                            </p>
                            <p>
                                <label for="outputText">Text Chifrée</label>
                                <input type="text" name="outputText" value="%s">
                            </p>
                            <p>
                                <input type="submit" name="text" value="Chiffrer">
                                <input type="submit" name="text" value="Dechiffrer">
                            </p>
                        </div>
                        <div class="col-sm-6" style="border: 1px solid black">
                            <legend>Chiffrement d'image</legend>
                            <p>
                                <label for="key">Clé</label>
                                <input type="text" name="key256" value="253 176 65 245">
                            </p>
                            <p>
                                <label for="inputImage">Image à chiffrer/déchiffrer</label>
                                <input type="file" name="inputImage">
                            </p>
                            <p>
                                <input type="submit" name="image" value="ChiffrerImage">
                                <input type="submit" name="image" value="DechiffrerImage">
                                <input name="imageData" hidden value="%s">


                            </p>
                            <p>
                                <img src="%s">
                            </p>
                            <p>
                                <input type="submit" name="image" value="DownloadImage">
                            </p>
                        </div>
                    </div>
                </div>
            </fieldset>
        </form>



            <br>

            <br>
        </form>
    </body>
</html>
"""

    def get(self):

        self.response.write(self.html % ("", "", "", ""))

    def post(self):
        key = []
        key27 = self.request.get("key27")
        key256 = self.request.get("key256")
        if len(key27) > 0:
            key = key27.split(' ')
            key = [[int(key[0]), int(key[1])], [int(key[2]), int(key[3])]]
        else:
            key = key256.split(' ')
            key = [[int(key[0]), int(key[1])], [int(key[2]), int(key[3])]]

        if self.request.get("text") == "Chiffrer":
            inputText = self.request.get("inputText")

            outputText = hill.encrypt_text(inputText, key)
            logging.info(outputText)

            self.response.write(self.html % (inputText, outputText, "", ""))


        elif self.request.get("text") == "Dechiffrer":
            outputText = self.request.get("outputText")

            inputText = hill.decrypt_text(outputText, key)
            logging.info(outputText)
            logging.info(inputText)

            self.response.write(self.html % (inputText, outputText, "", ""))

        elif self.request.get("image") == "ChiffrerImage":

            file_jpgdata = StringIO(self.request.get("inputImage"))
            ret = hill.encrypt_image_return(file_jpgdata, key)
            jpeg_image_buffer = StringIO()
            ret.save(jpeg_image_buffer, format="PNG")


            #imgStr =
            imgHtml = 'data:image/png;base64,' + base64.b64encode(jpeg_image_buffer.getvalue())
            #self.response.write(self.html % ("", "", "", imgHtml))

            #self.response.headers['content-type'] = 'application/octet-stream'
            #self.response.headers['content-disposition'] = 'attachment; filename=chiffree.png'
            #self.response.write(jpeg_image_buffer.getvalue())

            self.response.write(self.html % ("", "", base64.b64encode(jpeg_image_buffer.getvalue()), imgHtml))

        elif self.request.get("image") == "DechiffrerImage":

            file_jpgdata = StringIO(self.request.get("inputImage"))
            ret = hill.decrypt_image_return(file_jpgdata, key)
            jpeg_image_buffer = StringIO()
            ret.save(jpeg_image_buffer, format="PNG")

            #import base64
            #imgStr = base64.b64encode(jpeg_image_buffer.getvalue())
            #imgHtml = 'data:image/png;base64,' + imgStr

            imgHtml = 'data:image/png;base64,' + base64.b64encode(jpeg_image_buffer.getvalue())
            #self.response.write(self.html % ("", "", "", imgHtml))

            #self.response.headers['content-type'] = 'application/octet-stream'
            #self.response.headers['content-disposition'] = 'attachment; filename=chiffree.png'
            #self.response.write(jpeg_image_buffer.getvalue())

            self.response.write(self.html % ("", "", base64.b64encode(jpeg_image_buffer.getvalue()), imgHtml))

        elif self.request.get("image") == "DownloadImage":

            #ret = hill.decrypt_image_return(file_jpgdata, key)
            #jpeg_image_buffer = StringIO()
            #ret.save(jpeg_image_buffer, format="PNG")

            #import base64
            #imgStr = base64.b64encode(file_jpgdata.getvalue())
            #imgHtml = 'data:image/png;base64,' + imgStr

            self.response.headers['content-type'] = 'application/octet-stream'
            self.response.headers['content-disposition'] = 'attachment; filename=image.png'
            self.response.write(base64.b64decode(self.request.get("imageData")))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
