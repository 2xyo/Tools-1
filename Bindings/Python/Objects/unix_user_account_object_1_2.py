#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Nov 06 14:03:37 2012 by generateDS.py version 2.7c.
#

import sys
import getopt
import re as re_

import user_account_object_1_2
import cybox_common_types_1_0

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class UnixPrivilegeType(user_account_object_1_2.PrivilegeType):
    """The UnixPrivilegeType type is used to specify Unix privileges. It
    extends the abstract user_account_object_1_2.PrivilegeType from the CybOX UserAccount
    object."""
    subclass = None
    superclass = user_account_object_1_2.PrivilegeType
    def __init__(self, Permissions_Mask=None):
        super(UnixPrivilegeType, self).__init__()
        self.Permissions_Mask = Permissions_Mask
    def factory(*args_, **kwargs_):
        if UnixPrivilegeType.subclass:
            return UnixPrivilegeType.subclass(*args_, **kwargs_)
        else:
            return UnixPrivilegeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Permissions_Mask(self): return self.Permissions_Mask
    def set_Permissions_Mask(self, Permissions_Mask): self.Permissions_Mask = Permissions_Mask
    def validate_StringObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.StringObjectAttributeType, a restriction on None.
        pass
    def export(self, outfile, level, namespace_='UnixUserAccountObj:', name_='UnixPrivilegeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='UnixPrivilegeType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='UnixUserAccountObj:', name_='UnixPrivilegeType'):
        super(UnixPrivilegeType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='UnixPrivilegeType')
    def exportChildren(self, outfile, level, namespace_='UnixUserAccountObj:', name_='UnixPrivilegeType', fromsubclass_=False, pretty_print=True):
        super(UnixPrivilegeType, self).exportChildren(outfile, level, 'UnixUserAccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Permissions_Mask is not None:
            self.Permissions_Mask.export(outfile, level, 'UnixUserAccountObj:', name_='Permissions_Mask', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Permissions_Mask is not None or
            super(UnixPrivilegeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='UnixPrivilegeType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(UnixPrivilegeType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(UnixPrivilegeType, self).exportLiteralChildren(outfile, level, name_)
        if self.Permissions_Mask is not None:
            showIndent(outfile, level)
            outfile.write('Permissions_Mask=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Permissions_Mask.exportLiteral(outfile, level, name_='Permissions_Mask')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixPrivilegeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Permissions_Mask':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Permissions_Mask(obj_)
        super(UnixPrivilegeType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixPrivilegeType

class UnixGroupType(user_account_object_1_2.GroupType):
    """The UnixGroupType type is used for specifying Unix groups. It
    extends the abstract user_account_object_1_2.GroupType from the Cybox UserAccount
    element."""
    subclass = None
    superclass = user_account_object_1_2.GroupType
    def __init__(self, Group_ID=None):
        super(UnixGroupType, self).__init__()
        self.Group_ID = Group_ID
    def factory(*args_, **kwargs_):
        if UnixGroupType.subclass:
            return UnixGroupType.subclass(*args_, **kwargs_)
        else:
            return UnixGroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Group_ID(self): return self.Group_ID
    def set_Group_ID(self, Group_ID): self.Group_ID = Group_ID
    def validate_NonNegativeIntegerObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.NonNegativeIntegerObjectAttributeType, a restriction on None.
        pass
    def export(self, outfile, level, namespace_='UnixUserAccountObj:', name_='UnixGroupType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='UnixGroupType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='UnixUserAccountObj:', name_='UnixGroupType'):
        super(UnixGroupType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='UnixGroupType')
    def exportChildren(self, outfile, level, namespace_='UnixUserAccountObj:', name_='UnixGroupType', fromsubclass_=False, pretty_print=True):
        super(UnixGroupType, self).exportChildren(outfile, level, 'UnixUserAccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Group_ID is not None:
            self.Group_ID.export(outfile, level, 'UnixUserAccountObj:', name_='Group_ID', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Group_ID is not None or
            super(UnixGroupType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='UnixGroupType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(UnixGroupType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(UnixGroupType, self).exportLiteralChildren(outfile, level, name_)
        if self.Group_ID is not None:
            showIndent(outfile, level)
            outfile.write('Group_ID=model_.cybox_common_types_1_0.NonNegativeIntegerObjectAttributeType(\n')
            self.Group_ID.exportLiteral(outfile, level, name_='Group_ID')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixGroupType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Group_ID':
            obj_ = cybox_common_types_1_0.UnsignedIntegerObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Group_ID(obj_)
        super(UnixGroupType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixGroupType

class UnixUserAccountObjectType(user_account_object_1_2.UserAccountObjectType):
    """The UnixUserAccountType type is intended to characterize Unix user
    accounts."""
    subclass = None
    superclass = user_account_object_1_2.UserAccountObjectType
    def __init__(self, object_reference=None, disabled=None, locked_out=None, Description=None, Domain=None, password_required=None, Full_Name=None, Group_List=None, Home_Directory=None, Last_Login=None, Privilege_List=None, Script_Path=None, Username=None, User_Password_Age=None, Group_ID=None, User_ID=None, Login_Shell=None):
        super(UnixUserAccountObjectType, self).__init__(object_reference, disabled, locked_out, Description, Domain, password_required, Full_Name, Group_List, Home_Directory, Last_Login, Privilege_List, Script_Path, Username, User_Password_Age, )
        self.Group_ID = Group_ID
        self.User_ID = User_ID
        self.Login_Shell = Login_Shell
    def factory(*args_, **kwargs_):
        if UnixUserAccountObjectType.subclass:
            return UnixUserAccountObjectType.subclass(*args_, **kwargs_)
        else:
            return UnixUserAccountObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Group_ID(self): return self.Group_ID
    def set_Group_ID(self, Group_ID): self.Group_ID = Group_ID
    def validate_UnsignedIntegerObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.UnsignedIntegerObjectAttributeType, a restriction on None.
        pass
    def get_User_ID(self): return self.User_ID
    def set_User_ID(self, User_ID): self.User_ID = User_ID
    def get_Login_Shell(self): return self.Login_Shell
    def set_Login_Shell(self, Login_Shell): self.Login_Shell = Login_Shell
    def validate_StringObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.StringObjectAttributeType, a restriction on None.
        pass
    def export(self, outfile, level, namespace_='UnixUserAccountObj:', name_='UnixUserAccountObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='UnixUserAccountObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='UnixUserAccountObj:', name_='UnixUserAccountObjectType'):
        super(UnixUserAccountObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='UnixUserAccountObjectType')
    def exportChildren(self, outfile, level, namespace_='UnixUserAccountObj:', name_='UnixUserAccountObjectType', fromsubclass_=False, pretty_print=True):
        super(UnixUserAccountObjectType, self).exportChildren(outfile, level, 'UnixUserAccountObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Group_ID is not None:
            self.Group_ID.export(outfile, level, 'UnixUserAccountObj:', name_='Group_ID', pretty_print=pretty_print)
        if self.User_ID is not None:
            self.User_ID.export(outfile, level, 'UnixUserAccountObj:', name_='User_ID', pretty_print=pretty_print)
        if self.Login_Shell is not None:
            self.Login_Shell.export(outfile, level, 'UnixUserAccountObj:', name_='Login_Shell', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Group_ID is not None or
            self.User_ID is not None or
            self.Login_Shell is not None or
            super(UnixUserAccountObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='UnixUserAccountObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(UnixUserAccountObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(UnixUserAccountObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Group_ID is not None:
            showIndent(outfile, level)
            outfile.write('Group_ID=model_.cybox_common_types_1_0.UnsignedIntegerObjectAttributeType(\n')
            self.Group_ID.exportLiteral(outfile, level, name_='Group_ID')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.User_ID is not None:
            showIndent(outfile, level)
            outfile.write('User_ID=model_.cybox_common_types_1_0.UnsignedIntegerObjectAttributeType(\n')
            self.User_ID.exportLiteral(outfile, level, name_='User_ID')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Login_Shell is not None:
            showIndent(outfile, level)
            outfile.write('Login_Shell=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Login_Shell.exportLiteral(outfile, level, name_='Login_Shell')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixUserAccountObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Group_ID':
            obj_ = cybox_common_types_1_0.UnsignedIntegerObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Group_ID(obj_)
        elif nodeName_ == 'User_ID':
            obj_ = cybox_common_types_1_0.UnsignedIntegerObjectAttributeType.factory()
            obj_.build(child_)
            self.set_User_ID(obj_)
        elif nodeName_ == 'Login_Shell':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Login_Shell(obj_)
        super(UnixUserAccountObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixUserAccountObjectType

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Unix_User_Account'
        rootClass = UnixUserAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Unix_User_Account'
        rootClass = UnixUserAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Unix_User_Account",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Unix_User_Account'
        rootClass = UnixUserAccountObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from temp import *\n\n')
    sys.stdout.write('import temp as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "UnixUserAccountObjectType",
    "UnixGroupType",
    "UnixPrivilegeType"
    ]