import xml.etree.ElementTree as ET
import logs
tree = ET.parse('examples\example.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)


log = logs.MyLogs()

log.write_warning(text="ala")
