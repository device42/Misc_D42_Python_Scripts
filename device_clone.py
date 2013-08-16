'''
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

#################################################################################################
# create cloned devices based on an existing device using REST APIs
# step 1: Change lines 26-31
# step 2: Execute the script
#################################################################################################

import urllib2, urllib
from base64 import b64encode
import simplejson as json


D42_URL = 'https://192.168.11.12/'                   #your_d42_fqdn_or_ip                 #make sure to end in /
D42_USERNAME = 'admin'   #your_d42_username_here
D42_PASSWORD = 'adm!nd42' #your_d42_password_here
DEBUG = True                                                                #True or False. True for detailed info
ORIGINAL_DEVICE_NAME = 'server01'
NEW_DEVICE_NAMES = ['serve02', 'server03', ]                                #Leave last , even if a single name
CLONE_HARDWARE = True
CLONE_OS = True


d42_get_device_url = 'https://'+D42_URL+'/api/1.0/device/name/' + ORIGINAL_DEVICE_NAME + '/'
d42_add_device_url = 'https://'+D42_URL+'/api/device/'

request = urllib2.Request(d42_get_device_url)
request.add_header('Authorization', 'Basic ' + b64encode(D42_USERNAME + ':' + D42_PASSWORD))
try:
    r = urllib2.urlopen(request)
    obj = r.read()
    device_to_be_cloned = json.loads(obj)

    for key,value in  device_to_be_cloned.iteritems():
        print key, value
except Exception, s: print str(s)



