from main import *

class Ui_Page1(MainWindow):
    
    def __init__(self, par):
        self.cur_MachineName = "#1 Nexturn"
        self.c_pj_plan = []
        self.plan_pj = []
        
        self.journal_path = ".\\Resurce\\journal.json"
        
        #BIND
        self.ui = par.ui
        self.parent = par

        self.ui.Btn_Menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        
        ## Кнопки - инициализация 
        ########################################################################
        self.ui.Btn_curOpenPj.clicked.connect(lambda: self.Btn_c_OpenPjClicked())
        
        self.ui.TablePlan.installEventFilter(self.parent)

        ## ButtonGroup - инициализация 
        ########################################################################
        self.rBtn_Machine = QButtonGroup()    
        
        self.rBtn_Machine.addButton(self.ui.rBtn_1_machine)
        self.rBtn_Machine.addButton(self.ui.rBtn_2_machine)
        self.rBtn_Machine.addButton(self.ui.rBtn_3_machine)

        self.rBtn_Machine.buttonClicked.connect(self.rBtnClicked)


        self.ui.BtnAddNote.clicked.connect(lambda: self.BtnAddNoteClicked())
        self.updJournal()

    def Btn_c_OpenPjClicked(self):
        
        df = self.c_pj_plan
        path = df[['Путь в папке Production']].values.tolist()[0][0]
        self.getFileName(path)


    def upd_plan_info(self):
        actual_col = [
                        "Номер станка",
                        "Производственный код",
                        "Количество штук в партии",
                        "Что это такое"]
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

        self.ui.TablePlan.setRowCount(len(list_df))
        
        max_with = []
        for i in range(len(list_df[0])):
            max_with.append(0)
        
        for i in range(len(list_df)):
        # Добавление строки
            for j in range(len(list_df[0])):
                c_len = len(str(list_df[i][j]) )
                
                if max_with[j] < c_len:
                    max_with[j] = c_len

                self.ui.TablePlan.setItem(i, j, QTableWidgetItem(str(list_df[i][j])))

        for col in range(0,len(list_df[0])):
            self.ui.TablePlan.setColumnWidth(col, 8*max_with[col])
        

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
        self.upd_BookMarks()

    def BtnAddNoteClicked(self):
        self.add_note()

    def get_id_machine (self):
        convert = {
            "#1 Nexturn" : 1,
            "#2 Nexturn" : 2,
            "#3 Tsugami" : 3
        }
        return convert[self.cur_MachineName]

    def getFileName(self, def_path):
        filename = ""
        filename, filetype = QFileDialog.getOpenFileName(self.parent,
                                "Выбрать файл",
                                def_path,
                                "Все (*.prt;*.txt;*.xlsx;*.pdf;*.docm;*.docx);;\
                                Siemens NX (*.prt);;\
                                PDF (*.pdf);;\
                                MS Word (*.docm;*.docx);;\
                                MS Excel (*.xlsx;*.xlsm);;\
                                Text file (*.txt);;\
                                All Files (*)")
        if filename is not "":
            path = Path(filename)
            subprocess.Popen( ["explorer", path] )
    
    def add_note(self):

        date = datetime.datetime.today().strftime("%H:%M   %d/%m/%Y")

        note = {
            "prog" : "Stas",
            "date" : date,
            "note" : "Приплыли"
        }
        path = self.journal_path

        journal = self.get_journal()
        if journal == "":
            journal = dict()
            journal["data"] = []

        journal["data"].append(note)

        with open(path, 'w') as outfile:
            json.dump(journal, outfile, indent=2)
        
        self.updJournal()
    
    def get_journal (self):
        
        path = self.journal_path
        
        try :
            with open(path, "r") as read_file:
                data = json.load(read_file)
            
            return data
        except:
            print("Alarm: crash with open journal")
            return ""
        

    def updJournal(self):
        journal = self.get_journal()
        br = "------------------------------------------------------------\n"
        string = str()

        for index in range(len(journal['data'])):
            date = '\n\t' + journal['data'][index]["date"] + '\n'
            note = journal['data'][index]["note"] + '\n'
            string += date + note + br


        self.ui.Journal.setText(string)

    def upd_BookMarks(self):
        pass

    def TableEvent (self, source, event):
        menu = QMenu()
        newAction = QAction("В закладки")
        newAction.triggered.connect(lambda: self.addBookmark())
        menu.addAction(newAction)

        menu.exec_(event.globalPos())

    def addBookmark(self):
        row = self.ui.TablePlan.currentRow()
        col = self.ui.TablePlan.currentColumn()
        value = self.ui.TablePlan.item(row, col).text()
        
        print(f"R:{row}\nC:{col}\nV:{value}") 
    



