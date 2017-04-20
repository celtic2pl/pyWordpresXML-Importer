import xml.etree.ElementTree as Xml_ET


class MyXml:

    def __init__(self):
        self.root = None
        self.file = None

    def load_xml(self, file_to_load):
        tree = Xml_ET.parse(file_to_load)
        self.root = tree.getroot()

    def get_root_tag(self):
        return self.root.tag

    def get_children_tags(self, parent=''):
        count = 0   # not used
        children_set = set()
        for children in self.root.iter(parent):
            for child in children:
                count += 1  # not used
                children_set.add(child.tag)
        return children_set

    def all_tags_from_parent(self, parent=''):
        if len(self.get_children_tags(parent)) >= 1:
            for child in self.get_children_tags(parent):
                print(child)
                self.all_tags_from_parent(child)

    def find_element(self, xpath):
        return self.root.findall(xpath)


if __name__ == '__main__':
    file = 'examples\example.xml'
    a = MyXml()
    a.load_xml(file)
    a.all_tags_from_parent(a.get_root_tag())
