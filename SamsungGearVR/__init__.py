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
    description=(
        u'Hardware Plugin for Samsung Gear Vr bluetooth controller\n
    ),
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
    # add variables with string that you want to be able to have translated
    # using the language editor in here
    pass


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



