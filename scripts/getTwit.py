from settings import settings
import os
import sys
sys.path.append(os.path.join(settings["projectRoot"], "src"))

from twitter.lib import getTwitById
from twitter.settings import settings

res = getTwitById(settings["bearerToken"], 22)

print(res.text)
