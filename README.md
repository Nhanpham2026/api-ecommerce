# selenium_day12/tests/test_upload.py
![Python API Automation](https://github.com/Nhanpham2026/api-automation-ecommerce/actions/workflows/python-api-automation.yml/badge.svg)
import os
import unittest
from selenium import webdriver
from pages.upload_page import UploadPage

class TestUpload(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.page = UploadPage(cls.driver)

    def test_upload_file(self):
        # Tạo 1 file tạm trong thư mục project
        file_name = "test_upload.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("Đây là file test upload.")

        # Mở trang và upload
        self.page.open()
        abs_path = os.path.abspath(file_name)
        self.page.upload_file(abs_path)

        # Lấy thông báo và assert
        message = self.page.get_upload_message()
        print("Upload message:", message)
        self.assertIn("File Uploaded", message)

        # Xóa file tạm nếu muốn
        os.remove(file_name)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
