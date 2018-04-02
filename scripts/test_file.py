import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.file_page import FilePage

class TestFile:

    def setup(self):
        self.driver = init_driver()
        self.file_page = FilePage(self.driver)

    def test_first(self):

        # # 创建zzz
        # self.file_page.create_dir_with_name("zzz")
        # # 创建aaa
        # self.file_page.create_dir_with_name("aaa")
        # # 进入zzz
        # self.file_page.entry_dir_with_name("zzz")
        # # 创建1-20.txt
        # for i in range(20):
        #     self.file_page.create_file_with_name(str(i + 1) + ".txt")
        # 全选
        self.file_page.click_operation()
        self.file_page.click_all_select()

        # 进入aaa
        self.file_page.entry_sdcard()
        self.file_page.entry_dir_with_name("aaa")

        # 移动选择项
        self.file_page.click_operation()
        self.file_page.click_move_select()