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
import os
from cmsis_svd.parser import SVDParser


# Use the following class method for initialization when using svd file provided with package
# parser = SVDParser.for_packaged_svd('STMicro', 'STM32F446.svd')

# Use the following initialization method when using svd file from this repository's data folder
dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.abspath(os.path.join(dirname, "..",'data','STMicro', 'STM32F446.svd'))
parser = SVDParser.for_xml_file('STMicro', 'STM32F446.svd')

perph_queue = []
perph_queue_base_addr = []
perph_queue_descr = []
for peripheral in parser.get_device().peripherals:
    perph_queue.append(peripheral.name)
    perph_queue_descr.append(parser.get_device().description)
    perph_queue_base_addr.append(peripheral.base_address)
    fnname = peripheral.name
    file1 = open('%s.h' % peripheral.name, "w")
    file1.write("#define    {:<15}".format(peripheral.name))
    x = str(hex(peripheral.base_address))
    file1.write("{:>10}".format(x))
    if ((peripheral.description).find('\n') == -1):
        file1.write("       //  {:<10}\n".format(peripheral.description))
    else:
        temp_desc1 = " ".join((peripheral.description).split())
        temp_desc2 = (peripheral.description).replace("\n","")
        file1.write("       //  {:<10}\n".format(temp_desc1))
def write_peripheral_to_file(peripheral,peripheral_name):
    if (peripheral in (peripheral.name)):
        if ((parser.get_device().peripherals).string.count(peripheral.description) == 1):
            file_peripheral  = open("%s.h" % peripheral.name,'w') 
            file_peripheral.write("typedef struct")
        else:
            file_peripheral.close("typedef struct")

write_peripheral_to_file(peripheral,peripheral.name)
