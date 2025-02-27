# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Feengagevolumes",
    "author": "Moonling",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}

import bpy
from . Volumes_Planel import *
from .Toolbox_Panel import *

classes = (
    FETools_FixLocators,
    FETools_Panel,
    FEVolumes_Panel,
    FEVolumes_Apply,
    FEVloumes_Clear,
    FEVolumesPropGroup,
)


def register(): 
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.feengagevolumes = bpy.props.PointerProperty(type=FEVolumesPropGroup)

def unregister(): 
    del bpy.types.Scene.feengagevolumes
    for cls in classes:
        bpy.utils.unregister_class(cls)
