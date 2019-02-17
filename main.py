# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expre/ss or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html') 
        self.response.out.write(template.render(path, {}))
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('<HTML><BODY><H1>Hello, World!</H1><BR>Hahaha</BODY></HTML>')

class MainPage2(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index2.html') 
        self.response.out.write(template.render(path, {}))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about', MainPage2),
], debug=True)
