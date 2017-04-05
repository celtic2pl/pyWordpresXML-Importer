import logging
import datetime


class MyLogs:
    status_ok = True

    def __init__(self):
        self.file_log_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.log'
        self.folder = "logs"
        self.log_path = self.folder + '/' + self.file_log_name
        self.level = logging.INFO
        logging.basicConfig(filename=self.log_path, level=self.level)

    def write_info(self, text=''):
        print(text)
        logging.info(text)
        return self.status_ok

    def write_warning(self, text=''):
        print(text)
        logging.warning(text)
        return self.status_ok


a = MyLogs()
a.write_warning("To jest warning")
a.write_info("To jest info")
