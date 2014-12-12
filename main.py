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


class MainHandler(webapp2.RequestHandler):
    html = u"""
<html>
    <head>
        <title>Hill Cipher | Text and Image Encryption</title>
    </head>
    <body>
        <form action="/" method="POST" enctype="multipart/form-data">
            <p>
                <label for="inputText">Text Original</label>
                <input type="text" name="inputText" value="%s">
            </p>
            <p>
                <label for="outputText">Text Chifrée</label>
                <input type="text" name="outputText" value="%s">
            </p>
            <p>
                <label for="key">Key (LiCo à la suite)</label>
                <input type="text" name="key" value="11 3 8 7">
            </p>
            <p><input type="submit" name="text" value="Chiffrer">
            <input type="submit" name="text" value="Dechiffrer"></p>
            <br>
            <p>
                <label for="inputImage">Text Chifrée</label>
                <input type="file" name="inputImage">
                <input type="submit" name="image" value="ChiffrerImage">
                <img src="%s">
            </p>
            <p>
                <label for="outputImage">Image Chifrée</label>
                <input type="submit" name="image" value="DechiffrerImage">
                <img src="%s">
            </p>
            <br>
        </form>
    </body>
</html>
"""

    def get(self):

        self.response.write(self.html % ("", "", "", ""))

    def post(self):
        self.response.write(self.request.get("image"))
        if self.request.get("text") == "Chiffrer":
            inputText = self.request.get("inputText")
            key = self.request.get("key")
            key = key.split(' ')
            logging.info(inputText)
            logging.info(key)
            key = [[int(key[0]), int(key[1])], [int(key[2]), int(key[3])]]
            logging.info(key)
            outputText = hill.encrypt_text(inputText, key)
            logging.info(outputText)

            self.response.write(self.html % (inputText, outputText, "", ""))


        elif self.request.get("text") == "Dechiffrer":
            outputText = self.request.get("outputText")

            key = self.request.get("key")
            key = key.split(' ')
            key = [[int(key[0]), int(key[1])], [int(key[2]), int(key[3])]]

            inputText = hill.decrypt_text(outputText, key)
            logging.info(outputText)
            logging.info(inputText)

            self.response.write(self.html % (inputText, outputText, "", ""))

        elif self.request.get("image") == "ChiffrerImage":
            self.response.write(self.request.get("inputImage"))

            key = self.request.get("key")
            key = key.split(' ')
            key = [[int(key[0]), int(key[1])], [int(key[2]), int(key[3])]]
            #inputText = hill.decrypt_text(outputText, key)
            #logging.info(outputText)
            #logging.info(inputText)

            self.response.write(self.html % ("", "", "", ""))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
