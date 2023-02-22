#!/usr/bin/env python3
import collections
import sys
from unittest import mock

import polib


def main():
    with mock.patch.object(polib.POEntry, "__cmp__", patched_cmp):
        for path in sys.argv[1:]:
            po_file = polib.pofile(str(path), wrapwidth=100)
            po_file.sort()

            meta = collections.OrderedDict()
            for key, val in sorted(po_file.metadata.items()):
                if key not in IGNORE_META:
                    meta[key] = val
            po_file.metadata = meta

            po_file.save()

            with open(str(path), "r") as fp:
                lines = list(fp.readlines())
            with open(str(path), "w") as fp:
                for line in lines:
                    # Remove merge markers from msgcat
                    if line.startswith("# #-#-#-#-#"):
                        continue
                    
                    # Remove invisible chars
                    line = line.replace("\u00a0", " ")

                    fp.write(line)


IGNORE_META = (
    "Language-Team",
    "Last-Translator",
    "PO-Revision-Date",
    "POT-Creation-Date",
    "Project-Id-Version",
    "Report-Msgid-Bugs-To",
    "X-Generator",
    "X-Translated-Using",
)


def patched_cmp(self, other):
    """
    Called by comparison operations if rich comparison is not defined.

    MV: Had to patch this, because the version from polib==1.1.0 does not
    work with python3.
    """
    # First: Obsolete test
    if self.obsolete != other.obsolete:
        if self.obsolete:
            return -1
        else:
            return 1
    # Work on a copy to protect original
    occ1 = sorted(self.occurrences[:])
    occ2 = sorted(other.occurrences[:])
    if occ1 > occ2:
        return 1
    if occ1 < occ2:
        return -1
    # Compare context
    msgctxt = self.msgctxt or "0"
    othermsgctxt = other.msgctxt or "0"
    if msgctxt > othermsgctxt:
        return 1
    elif msgctxt < othermsgctxt:
        return -1
    # Compare msgid_plural
    msgid_plural = self.msgid_plural or "0"
    othermsgid_plural = other.msgid_plural or "0"
    if msgid_plural > othermsgid_plural:
        return 1
    elif msgid_plural < othermsgid_plural:
        return -1
    # Compare msgstr_plural
    msgstr_plural = self.msgstr_plural or "0"
    othermsgstr_plural = other.msgstr_plural or "0"
    if msgstr_plural > othermsgstr_plural:
        return 1
    elif msgstr_plural < othermsgstr_plural:
        return -1
    # Compare msgid
    if self.msgid > other.msgid:
        return 1
    elif self.msgid < other.msgid:
        return -1
    return 0
