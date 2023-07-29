#
# Copyright 2015 Paul Osborne <osbpau@gmail.com>
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
import json
import os
from cmsis_svd.parser import SVDParser

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.abspath(os.path.join(dirname, "..",'data','Freescale', 'MK20D7.svd'))

parser = SVDParser.for_xml_file(filename)
svd_dict = parser.get_device().to_dict()
print(json.dumps(svd_dict, sort_keys=True,
                 indent=4, separators=(',', ': ')))
