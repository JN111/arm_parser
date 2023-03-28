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
from cmsis_svd.parser import SVDParser

parser = SVDParser.for_packaged_svd('STMicro', 'STM32F446.svd')
perph_queue = []
perph_queue_base_addr = []
perph_queue_descr = []
file1 = open('%s.h' % 'abc', "w")
for peripheral in parser.get_device().peripherals:
    perph_queue.append(peripheral.name)
    perph_queue_descr.append(parser.get_device().description)
    perph_queue_base_addr.append(peripheral.base_address)
    fnname = peripheral.name
    #file1.write("#define\t%s\t\t0x%08x \t" % (peripheral.name, peripheral.base_address))
    #file1.write("\t\t // %s\t\n" % peripheral.description)
    file1.write("#define"     (peripheral.name)       (peripheral.base_address))
    #file1.write("\t\t // %s\t\n" % peripheral.description)