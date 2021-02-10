from main import *

class DataFunc(MainWindow):
    def get_data(self):
        sheet_url = "https://docs.google.com/spreadsheets/d/1WY0pdiHgJ39govH042CNgQD_vKKYyTsTslZMYsEw1Og/edit#gid=942461385"
        key_path = ".\\Resurce\\key.json"

        gc = gspread.service_account(filename=key_path)

        try :
            sht = gc.open_by_url(sheet_url)
            worksheet = sht.sheet1
            self.DF  = pd.DataFrame(worksheet.get_all_records()) 
            QMessageBox.about(self, "Уведомление", "Вроде получилось")
        
        except :
            QMessageBox.about(self, "Ошибка", "Проверьте подключение к интернету")
