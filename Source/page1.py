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
        actual_col = [
                        "Номер станка",
                        "Производственный код",
                        "Количество штук в партии"]
        tmpDF = self.parent.DF
        
        #tmpDF = tmpDF[tmpDF['Состояние'].str.contains("На станке",case=False, na=False)]     
        tmpDF = tmpDF.loc[tmpDF['Состояние'].isin(["План"])]
        self.plan_pj = tmpDF.loc[tmpDF['Номер станка'].isin([self.get_id_machine()])]
        df = self.plan_pj
        df = df[actual_col]
        
        headers = df.columns.values.tolist()
        self.ui.TablePlan.setColumnCount(len(headers))
        
        self.ui.TablePlan.setHorizontalHeaderLabels(headers)
        
        list_df = df.values.tolist()

        self.ui.TablePlan.setRowCount(len(list_df) + 1)

        for i in range(len(list_df)):
        # Добавление строки

            for j in range(len(list_df[0])):
                #self.ui.TablePlan.setItem(i, j, QtGui.QTableWidgetItem(str(row[j])))
                self.ui.TablePlan.setItem(i, j, QTableWidgetItem(str(list_df[i][j])))

    def upd_c_info(self):
        tmpDF = self.parent.DF
        
        tmpDF = tmpDF.loc[tmpDF['Состояние'].isin(["На станке"])]
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

