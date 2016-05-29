#############################################################################
import configparser

# ini 配置文件格式：
#     节：[session]
#     参数(option)：name = value

cfg = configparser.ConfigParser()
# read()：Read and parse a filename or a list of filenames.
#       Return list of successfully read files.
# sections()：Return a list of section names, excluding [DEFAULT]

try:
    fds = cfg.read('D:/demo/cfg.ini')
    # print(type(fds))
    for section in cfg.sections():
        print(section)
        print(cfg.items(section))
    option = cfg.options('port')
    print(option)

    password = cfg.get('userinfo', 'password')
    print(password)
    # cfg.set('userinfo', 'password', '123456')
    # cfg.set('userinfo', 'email', 'xxx@gmail.com')
    # if cfg.has_option('userinfo', 'email'):
    #     cfg.remove_option('userinfo', 'email')
    # cfg.remove_section('userinfo')
    fd = open('D:/demo/cfg.ini', 'w')
    cfg.write(fd)
except IOError as error:
    print(error)
    fd.close()


class UserInfo(object):
    def __init__(self, recordfile):
        self.__recordfile = recordfile
        self.__cfg = configparser.ConfigParser()

    def cfg_load(self):
        self.__cfg.read(self.__recordfile)

    def cfg_dump(self):
        section_list = self.__cfg.sections()
        for section in section_list:
            print(section)
            print(self.__cfg.items(section))

    def set_option(self, section, key, value):
        self.__cfg.set(section, key, value)

    def delete_option(self, section, key):
        self.__cfg.remove_option(section, key)

    def delete_section(self, section):
        self.__cfg.remove_section(section)

    def save(self):
        fd = open(self.__recordfile, 'w')
        self.__cfg.write(fd)
        fd.close()


if __name__ == '__main__':
    print('=============================')
    user_info = UserInfo('D:/demo/cfg.ini')
    user_info.cfg_load()
    # user_info.cfg_dump()

    # user_info.set_option('userinfo', 'email', 'xxx@gmail.com')
    # user_info.delete_option('userinfo', 'email')
    # user_info.delete_section('userinfo')
    user_info.save()
