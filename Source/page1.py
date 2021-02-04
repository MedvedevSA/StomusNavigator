class Ui_Page1(object):
    def __init__(self, global_ui):
        #BIND
        global_ui.Btn_Menu_1.clicked.connect(lambda: global_ui.Pages_Widget.setCurrentWidget(global_ui.page_1))
    
    def Event_rBtnSelected (self):
        pass
    
    
