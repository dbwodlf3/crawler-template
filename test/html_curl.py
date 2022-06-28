from settings import settings
import os
import sys
sys.path.append(os.path.join(settings["projectRoot"], "src"))

from curl.lib import getCurl

res = getCurl("http://www.naver.com")
print(res.text)