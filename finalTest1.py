import win32gui
import win32con
import sys,os, win32com.client
import subprocess
import time
from sap1 import data 
import keyboard


# for index, (key, value) in enumerate(data.items()):
#     print(type(index),key)  
    
#     for index1,value1 in enumerate(value):
#         print(index1,value1,value1['name'])
# quit()



'''
Creates a SAP connection object
connection_name -> SAP connection instance name for which connection object needs to be created
'''
 
 
def create_sap_connection(connection_name):
 
    try:
        os.system("taskkill /im saplogon.exe /F")
    except:
        pass
 
    global session,session1
    error = 'SAP Connection Error'
 
    path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
    subprocess.Popen(path)
    time.sleep(20)
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    if not type(SapGuiAuto) == win32com.client.CDispatch:
        return error,1
 
    application = SapGuiAuto.GetScriptingEngine
    if not type(application) == win32com.client.CDispatch:
        SapGuiAuto = None
        return error,2
 
    connection = application.OpenConnection(connection_name, True)
       
    if not type(connection) == win32com.client.CDispatch:
        application = None
        SapGuiAuto = None
        return error,3
 
    if connection.DisabledByServer == True:
        application = None
        SapGuiAuto = None
        return error,4
 
    session = connection.Children(0)
    session1 = session
    if not type(session) == win32com.client.CDispatch:
        connection = None
        application = None
        SapGuiAuto = None
        return error,5
 
    if session.Info.IsLowSpeedConnection == True:
        connection = None
        application = None
        SapGuiAuto = None
        return error,6
   
    print("cretae") 
    return 'Success', session

'''
Login into SAP with the provided username and password
session -> SAP connection object
username -> SAP username for login
password -> SAP password for login
'''

def sap_login(session,username,password):
    print("log..")
    time.sleep(5)
    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "500"
    session.findById("wnd[0]/usr/txtRSYST-BNAME").text = username
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").setFocus()
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").caretPosition = 16
    session.findById("wnd[0]").resizeWorkingPane(168, 25, False)
    session.findById("wnd[0]").sendVKey(0)
    
    # If multiple SAP login pop-up occurs then select 2nd option
    ##try:
       
        # session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").select()
        # session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").setFocus()
        # session.findById("wnd[1]").sendVKey(0)
    #session.findById("wnd[1]/usr/radMULTI_LOGON_OPT2").select()
    #session.findById("wnd[1]/usr/radMULTI_LOGON_OPT2").setFocus()
        
        # session.findById("wnd[1]/tbar[0]/btn[0]").press()
    #session.findById("wnd[1]").sendVKey(0)
    
  
    ##except:

    #session.findById("wnd[0]").sendVKey(0)
    
    return "Success"


import time
def sap_one_creation(result,session):
    result  = 'Success'
    print("qqqq")
    if result == 'Success':
        print("qqqq1")
        print("Connection Created")
        result = sap_login(session,'sonel','Dfccil@@1234567890')
        if result == 'Success':
            print("qqqq")
            print("Login Successful")   
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "me21n"
            session.findById("wnd[0]").sendVKey(0)
            time.sleep(5)
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/cmbMEPO_TOPLINE-BSART").key = "ZIT"
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").text = "40015543"
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").setFocus()
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:1105/ctxtMEPO_TOPLINE-SUPERFIELD").caretPosition = 8
            session.findById("wnd[0]").sendVKey(0)
            time.sleep(1)
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKORG").text = "3000"
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-EKGRP").text = "H18"
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-BUKRS").text = "1000"
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-BUKRS").setFocus()
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT9/ssubTABSTRIPCONTROL2SUB:SAPLMEGUI:1221/ctxtMEPO1222-BUKRS").caretPosition = 4
            time.sleep(2)
            session.findById("wnd[0]").sendVKey(0)
            time.sleep(2)
            keyboard.press_and_release('CTRL+F3')
            time.sleep(4)
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211").verticalScrollbar.position = 3
            time.sleep(1)
            # print(data.items(), "<<<<=====Data items====")
            
            
            
            for index, (key, value) in enumerate(data.items()):
                print(index, key)
                time.sleep(2)

                try:
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0013/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211").getAbsoluteRow(index).selected = -1
                    id = '0013'
                except:
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211").getAbsoluteRow(index).selected = -1
                    id = '0019'
                    
                session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:{id}/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-KNTTP[2,{index}]").text = "K"
                session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:{id}/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-EPSTP[3,{index}]").text = "D"
                session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:{id}/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/txtMEPO1211-TXZ01[5,{index}]").text = key
                session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:{id}/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-WGBEZ[14,{index}]").text = "125"
                session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:{id}/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-NAME1[15,{index}]").text = "2010"
                session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:{id}/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-NAME1[15,{index}]").setFocus()
                session.findById(f"wnd[0]/usr/subSUB0:SAPLMEGUI:{id}/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1211/tblSAPLMEGUITC_1211/ctxtMEPO1211-NAME1[15,{index}]").caretPosition = 4
                time.sleep(2)
                session.findById("wnd[0]").sendVKey(0)
                session.findById("wnd[0]/tbar[1]/btn[39]").press()
                session.findById("wnd[1]/tbar[0]/btn[0]").press() 
                
                count = 0
                try:
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0020/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/btnUEBERSICHTSBILD").press()
                except:
                
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT1/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1328/subSUB0:SAPLMLSP:0400/btnUEBERSICHTSBILD").press()
                for index1,value1 in enumerate(value):
                    try:
                        session.findById("wnd[0]/usr/subSERVICE:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW").getAbsoluteRow(count).selected = -1
                        secId = '0400'
                    except:
                        session.findById("wnd[0]/usr/subSERVICE:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW").getAbsoluteRow(count).selected = -1
                        secId = '0400'
                        
                    session.findById(f"wnd[0]/usr/subSERVICE:SAPLMLSP:{secId}/tblSAPLMLSPTC_VIEW/txtESLL-KTEXT1[3,{count}]").text = value1['name']
    
                    time.sleep(1)
                    
                    session.findById(f"wnd[0]/usr/subSERVICE:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-MENGE[4,{count}]").text = value1['numbers']
                    session.findById(f"wnd[0]/usr/subSERVICE:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/ctxtESLL-MEINS[5,{count}]").text = "MAM"
                    session.findById(f"wnd[0]/usr/subSERVICE:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-TBTWR[6,{count}]").text = "300000"
                    
                    count += 1
                    
                    
                session.findById("wnd[0]/usr/subSERVICE:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-TBTWR[6,2]").setFocus()
                session.findById("wnd[0]/usr/subSERVICE:SAPLMLSP:0400/tblSAPLMLSPTC_VIEW/txtESLL-TBTWR[6,2]").caretPosition = 6
                session.findById("wnd[0]").sendVKey(0)
                session.findById("wnd[1]/usr/ctxtESKN-SAKTO").text = "61000081"
                session.findById("wnd[1]/usr/subKONTBLOCK:SAPLKACB:1101/ctxtCOBL-KOSTL").text = "2010030"
                session.findById("wnd[1]/usr/subKONTBLOCK:SAPLKACB:1101/ctxtCOBL-KOSTL").setFocus()
                session.findById("wnd[1]/usr/subKONTBLOCK:SAPLKACB:1101/ctxtCOBL-KOSTL").caretPosition = 7
                time.sleep(1)
                session.findById("wnd[1]/tbar[0]/btn[7]").press()
                session.findById("wnd[0]/tbar[0]/btn[3]").press()
                try:
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0020/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT14").select()
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT14/ssubTABSTRIPCONTROL2SUB:SAPLZMM_FG_ADDITION_PO_TAB_1:0100/ctxtCI_EKKODB-ZZREF_CONT_NO").text = "TESTING FOR AUTOMATION2"
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT14/ssubTABSTRIPCONTROL2SUB:SAPLZMM_FG_ADDITION_PO_TAB_1:0100/cmbCI_EKKODB-ZCTYP").key = "O"
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT14/ssubTABSTRIPCONTROL2SUB:SAPLZMM_FG_ADDITION_PO_TAB_1:0100/cmbCI_EKKODB-ZCTYP").setFocus()
                    session.findById("wnd[0]").sendVKey(0)
                    
                    
                except:
                    try:

                        session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT15").select()
                        session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT15/ssubTABSTRIPCONTROL2SUB:SAPLZMM_FG_ADDITION_PO_TAB_1:0100/ctxtCI_EKKODB-ZZREF_CONT_NO").text = "TESTING FOR AUTOMATION2"
                        session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT15/ssubTABSTRIPCONTROL2SUB:SAPLZMM_FG_ADDITION_PO_TAB_1:0100/cmbCI_EKKODB-ZCTYP").key = "O"
                        session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT15/ssubTABSTRIPCONTROL2SUB:SAPLZMM_FG_ADDITION_PO_TAB_1:0100/cmbCI_EKKODB-ZCTYP").setFocus()
                        session.findById("wnd[0]").sendVKey(0)
                        # pass
                    except :
                        pass
                    
                try:
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0017/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT7/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1317/ctxtMEPO1317-MWSKZ").text = "i7"
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0017/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT7/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1317/ctxtMEPO1317-MWSKZ").caretPosition = 2
                    session.findById("wnd[0]").sendVKey(0)
                except:
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0015/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT7/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1317/ctxtMEPO1317-MWSKZ").text = "i7"
                    session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0015/subSUB3:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1301/subSUB2:SAPLMEGUI:1303/tabsITEM_DETAIL/tabpTABIDT7/ssubTABSTRIPCONTROL1SUB:SAPLMEGUI:1317/ctxtMEPO1317-MWSKZ").caretPosition = 2
                    session.findById("wnd[0]").sendVKey(0)
 
            session.findById("wnd[0]/tbar[1]/btn[39]").press()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB1:SAPLMEVIEWS:4000/btnDYN_4000-BUTTON").press()
            session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0018/subSUB1:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1102/tabsHEADER_DETAIL/tabpTABHDT15").select()
            session.findById("wnd[0]").sendVKey(4)
            

            
            session.findById("wnd[1]/usr/lbl[5,3]").setFocus()
            session.findById("wnd[1]/usr/lbl[5,3]").caretPosition = 2
            print("exiting....") 
           
            session.findById("wnd[1]").sendVKey(2)
            
         
            session.findById("wnd[0]/tbar[1]/btn[39]").press()
            session.findById("wnd[0]/tbar[0]/btn[11]").press() 

           
# This is a standalone file to run sap automation

# result,session = create_sap_connection('ECQ [10.22.22.23]')
# sap_one_creation(result,session)
