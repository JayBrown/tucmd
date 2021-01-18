########################################################################
# This program is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# This program is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.#
#                                                                      #
# Copyright (c) 2014 by marcomg                                        #
# Modification: Copyright (c) 2021 by Joss Brown (pseud.)              #
########################################################################

import requests
import re

index_url = 'http://s000.tinyupload.com/index.php' # tinyupload home page
upload_url = 'http://s000.tinyupload.com/cgi-bin/upload.cgi?sid=' # tinyupload upload page

def upload(file):
	session = requests.Session()
	files = {'file': open(file, 'rb')}
	index_request = session.get(index_url)
	PHPSESSID = index_request.cookies['PHPSESSID']
	r = requests.post(upload_url+PHPSESSID, files=files)
	# If there is an error raise an exception
	try:
		return re.search('http://s000\.tinyupload.com/\?file_id=[^<]+', r.text).group(0)
	except AttributeError:
		raise ResourceWarning
	except TimeoutError:
		raise ResourceWarning
