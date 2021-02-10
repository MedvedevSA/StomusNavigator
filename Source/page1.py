from main import *

class Ui_Page1(MainWindow):
    def __init__(self, par):
        self.cur_MachineName = "#1 Nexturn"
        self.c_pj_plan = []
        self.plan_pj = []

        #BIND
        self.ui = par.ui
        self.parent = par

        self.ui.Btn_Menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        
        ## Кнопки - инициализация 
        ########################################################################
        self.ui.Btn_curOpenPj.clicked.connect(lambda: self.Btn_c_OpenPjClicked())
        


        ## ButtonGroup - инициализация 
        ########################################################################
        self.rBtn_Machine = QButtonGroup()    
        
        self.rBtn_Machine.addButton(self.ui.rBtn_1_machine)
        self.rBtn_Machine.addButton(self.ui.rBtn_2_machine)
        self.rBtn_Machine.addButton(self.ui.rBtn_3_machine)

        self.rBtn_Machine.buttonClicked.connect(self.rBtnClicked)

    def Btn_c_OpenPjClicked(self):
        
        df = self.c_pj_plan
        path = df[['Путь в папке Production']].values.tolist()[0][0]
        subprocess.Popen(f"explorer {path}")


    def upd_plan_info(self):
        tmpDF = self.parent.DF
        
        #tmpDF = tmpDF[tmpDF['Состояние'].str.contains("На станке",case=False, na=False)]     
        tmpDF = tmpDF.loc[tmpDF['Состояние'].isin(["На станке"])]
        self.plan_pj = tmpDF.loc[tmpDF['Номер станка'].isin([self.get_id_machine()])]
        df = self.plan_pj
        
        headers = df.columns.values.tolist()
        self.ui.TablePlan.setColumnCount(len(headers))
        self.ui.TablePlan.setHorizontalHeaderLabels(headers)
        
        for i, row in df.iterrows():
        # Добавление строки
            self.ui.TablePlan.setRowCount(self.ui.TablePlan.rowCount() + 1)

            for j in range(self.ui.TablePlan.columnCount()):
                self.ui.TablePlan.setItem(i, j, QTableWidgetItem(str(row[j])))

    def upd_c_info(self):
        tmpDF = self.parent.DF
        
        tmpDF = tmpDF.loc[tmpDF['Состояние'].isin(["План"])]
        self.c_pj_plan = tmpDF.loc[tmpDF['Номер станка'].isin([self.get_id_machine()])]

        df = self.c_pj_plan
        bach_name = df[['Производственный код']].values.tolist()[0][0]
        self.ui.lbl_cur_info.setText(bach_name)  

    def rBtnClicked (self, btn):
        self.cur_MachineName = btn.text()
        self.upd_c_info()
        self.upd_plan_info()


    def get_id_machine (self):
        convert = {
            "#1 Nexturn" : 1,
            "#2 Nexturn" : 2,
            "#3 Tsugami" : 3
        }
        return convert[self.cur_MachineName]

