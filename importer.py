import pwx_xml
# import pwx_logs


xml = pwx_xml.MyXml()

xml.load_xml('examples\\example.xml')
print("root tag:" + xml.get_root_tag())
xml.all_tags_from_parent(xml.get_root_tag())

# log = pwx_logs.MyLogs()
# log.write_warning(text="ala")
