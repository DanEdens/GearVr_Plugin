# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.org/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

import eg

eg.RegisterPlugin(
    name=u'GearVr_Plugin',
    author=u'Dan Edens',
    version=u'0.0.1a',
    description=u'Hardware Plugin for Samsung Gear Vr bluetooth controller',
    kind=u'remote',
    url=u'https://github.com/DanEdens/GearVr_Plugin',
    help=u'',
    canMultiLoad=False,
    createMacrosOnAdd=True,
    guid=u'{2B97188A-9D8E-4EB4-B05C-431CFF114D39}',
    hardwareId=u'BTHLE\\Dev_aa820fbaba2c\n',
    icon=None
)


class Text:
    class CHARACTERISTICS:
        '1879': [
            ['2A4E', '???'],
            ['2A4B', '???'],
            ['2A4A', '???'],
            ['2A4C', '???'],
            ['2A4D', '???'],
            ['2A22', '???'],
            ['2A32', '???']
        ],

        '4F63756C-7573-2054-6872-65656D6F7465': [
            ['C8C51726-81BC-483B-A052-F7A14EA3D281', 'notify characteristic -- event data'],
            ['C8C51726-81BC-483B-A052-F7A14EA3D282', 'write characteristic -- run command on controller']
        ],

        #https://github.com/numinit/porygon/wiki/protocol
        #FW_UPDATE_SERVICE
        #Firmware update service
        'FEF5': [
            ['8082CAA8-41A6-4021-91C6-56F9B954CC34', '???'],
            ['724249F0-5EC3-4B5F-8804-42345AF08651', '???'],
            ['6C53DB25-47A1-45FE-A022-7C92FB334FD4', '???'],
            ['9D8489A3-000C-49D8-9183-855B673FDA31', '???'],
            ['457871E8-D516-4CA1-9116-57D0B17B9CB2', '???'],
            ['5F78DF94-798C-46F5-990A-B3EB6A065C88', '???'],
            ['61C8849C-F639-4765-946E-5C3419BEBB2A', '???'],
            ['64B4E8B5-0DE5-401B-A21D-ACC8DB3B913A', '???'],
            ['42C3DFDD-77BE-4D9C-8454-8F875267FB3B', '???'],
            ['B7DE1EEA-823D-43BB-A3AF-C4903DFCE23C', '???'],
        ],

        #battery_service
        '180F': [
            ['2A19', 'battery_level']
        ],

        #device_information
        '180A': [
            ['2A29', 'manufacturer_name_string'],
            ['2A24', 'model_number_string'],
            ['2A25', 'serial_number_string'],
            ['2A27', 'revision number'],
            ['2A26', 'hardware_revision_string'],
            ['2A28', 'firmware_revision_string'],
            ['2A50', 'software_revision_string']
        ]

    class Services:
        BATTERY_SERVICE = '180F',
        DEVICE_INFORMATION = '180A',
        FW_UPDATE_SERVICE = 'FEF5',
        CUSTOM_SERVICE = '4F63756C-7573-2054-6872-65656D6F7465',
        UNKNOWN = '1879'

    class Modes:
        OFF_MODE = '0000',
        SENSOR_MODE = '0100',
        UNKNOWN_FIRMWARE_UPDATE_MODE = '0200',
        CALIBRATE_MODE = '0300',
        KEEP_ALIVE_MODE = '0400',
        UNKNOWN_SETTING_MODE = '0500',
        UNKNOWN_LPM_ENABLE_MODE = '0600',
        UNKNOWN_LPM_DISABLE_MODE = '0700',
        VR_MODE = '0800'

todoconvert = """

function getCharacteristic(serviceUUID, index) {
    return CHARACTERISTICS[serviceUUID][index][0].toLowerCase();


const getUUID = uuid => uuid.length === 4 ? eval(`0x${uuid}`) : uuid.toLowerCase();


// CUSTOM_SERVICE.WRITE characteristic expects LE ints
const getLittleEndianUint8Array = hexString => {
    const leAB = new Uint8Array(hexString.length >> 1);

    for (let i = 0, j = 0; i + 2 <= hexString.length; i += 2, j++) {
        leAB[j] = parseInt(hexString.substr(i, 2), 16);
    }

    return leAB;"""

class GearVr_Plugin(eg.PluginBase):
    text = Text

    # you want to add any variables that can be access from anywhere inside of
    # your plugin here
    def __init__(self):
        pass

    # you will want to add any startup parameters and also run any startup code
    # here
    def __start__(self, *args):
        pass

    # this gets called when eg is being closed and you can run code when that
    # happens
    def __close__(self):
        pass

    # this gets called as well when EG closes but it also gets called when a
    # plugin gets disabled. This is where you will do things like close any
    # open sockets
    def __stop__(self):
        pass

    # You will replace the code in this method if you want to make a plugin
    # configuration dialog.
    def Configure(self, *args):
        eg.PluginBase.Configure(self, *args)

    # The next 2 are pretty self explanatory
    def OnComputerResume(self):
        pass

    def OnComputerSuspend(self):
        pass

    # This gets called when a plugin gets deleted from the tree. so here if
    # you use eg.PersistantData to store any data. that data needs to be
    # deleted when the plugin gets removed. this is where that gets done.
    def OnDelete(self):
        pass



