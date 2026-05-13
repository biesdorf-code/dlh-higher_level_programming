#!/usr/bin/env python3
"""A module for serializing and deserializing to/from xml files"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an xml file"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="unicode", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserialize an xml file into a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
