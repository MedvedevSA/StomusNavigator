from main import *

class Ui_Page1(MainWindow):
    def __init__(self, par):
        self.cur_MachineName = "#1 Nexturn"
        
        #BIND
        self.ui = par.ui
        self.parent = par

        self.ui.Btn_Menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        
        ## Кнопки - инициализация 
        ########################################################################
        self.ui.Btn_curOpenPj.clicked.connect(lambda: self.Btn_curOpenPjClicked())
        


        ## ButtonGroup - инициализация 
        ########################################################################
        self.rBtn_Machine = QButtonGroup()    
        
        self.rBtn_Machine.addButton(self.ui.rBtn_1_machine)
        self.rBtn_Machine.addButton(self.ui.rBtn_2_machine)
        self.rBtn_Machine.addButton(self.ui.rBtn_3_machine)

        self.rBtn_Machine.buttonClicked.connect(self.rBtnClicked)

    def Btn_curOpenPjClicked(self):
        tmpDF = self.parent.DF
        
        #tmpDF = tmpDF[tmpDF['Состояние'].str.contains("На станке",case=False, na=False)]     
        tmpDF = tmpDF.loc[tmpDF['Состояние'].isin(["На станке"])]
        tmpDF = tmpDF.loc[tmpDF['Номер станка'].isin([self.get_id_machine()])]
        print(tmpDF)
        
    def rBtnClicked (self, btn):
        self.cur_MachineName = btn.text() 


    def get_id_machine (self):
        convert = {
            "#1 Nexturn" : 1,
            "#2 Nexturn" : 2,
            "#3 Tsugami" : 3
        }
        return convert[self.cur_MachineName]

