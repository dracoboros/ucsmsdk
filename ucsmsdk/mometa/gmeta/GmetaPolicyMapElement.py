"""This module contains the general information for GmetaPolicyMapElement ManagedObject."""
import sys, os

from ...ucsmo import ManagedObject
from ...ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class GmetaPolicyMapElementConsts():
    pass


class GmetaPolicyMapElement(ManagedObject):
    """This is GmetaPolicyMapElement class."""

    consts = GmetaPolicyMapElementConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("GmetaPolicyMapElement", "gmetaPolicyMapElement", "policymapelem-[name]", VersionMeta.Version212a, "InputOutput", 0x3f, [], ["read-only"], [u'gmetaPolicyMapHolder'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version212a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{2,64}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "GmetaPolicyMapElement", parent_mo_or_dn, **kwargs)

