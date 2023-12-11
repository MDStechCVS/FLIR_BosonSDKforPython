# This is a API for BOSON Camera

import sys
import os
import platform
import serial
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from BosonSDK import *

class BosonCamAPI():
    """
    boson camera API를 위한 클래스 -
    파라미터는 원도우일 경우 COMport 숫자
    conn() 커넥션, close()연결 해제 등등
    """
    def __init__(self, portNum):
        self.OsPlatform = platform.system()
        self.portNum = portNum      
        self.isConnect = False  
        self.myCam = None
        self.ProductName = 'N/A'
        self.conn()

    def getOSPlatform(self):
        return self.OsPlatform

    
    def conn(self):
        """
        카메라 커넥션
        리눅스일 경우 ttyACM 숫자
        :return: 연결 성공-True, 실패-False
        """
        try:
            if self.OsPlatform == 'Windows':
                print("window port")
                self.myCam = CamAPI.pyClient(manualport=self.portNum)
            else:
                self.myCam = CamAPI.pyClient(manualport=self.portNum)
            self.isConnect = True   # boson cam 커넥션 OK
            return True
        except:
            self.isConnect = False  # boson cam 커넥션 실패
            print("Connection FAIL")
            return False


    def close(self):
        try:
            CamAPI.pyClient.Close(self.myCam)
            self.isConnect = False
            current_func_name = sys._getframe().f_code.co_name
            print("Closed Complete")
        except Exception as e:
            print(f"Close {self.myCam} FAIL")


    def sysinfoGetProductName(self):
        returnVal = 'N/A'
        if self.isConnect == True:
            rValue, self.ProductName = self.myCam.sysinfoGetProductName()
            returnVal = self.ProductName

        return returnVal



    def getSerialNumber(self):
        returnVal = 'N/A'
        if self.isConnect == True:
            ret, serialNum = self.myCam.bosonGetCameraSN()
            returnVal = serialNum

        return returnVal

    def colorLutGetId(self):
        returnVal = 0
        if self.isConnect == True:
            rValue, self.colorLutVal = self.myCam.colorLutGetId()

            if rValue == FLR_RESULT.R_SUCCESS:
                print(self.colorLutVal)
                print(rValue)
                print('LUT no is ' + str(int(self.colorLutVal)))
                returnVal = int(self.colorLutVal)
            

        return returnVal

    def colorLutSetId(self, colVal):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_COLORLUT_ID_E(colVal)
            rValue = self.myCam.colorLutSetId(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def scalerGetMaxZoom(self):
        returnVal = 'N/A'
        if self.isConnect == True:
            rValue, self.zoomMaxVal = self.myCam.scalerGetMaxZoom()

            if rValue == FLR_RESULT.R_SUCCESS:
                print(self.zoomMaxVal)
                print(rValue)
                returnVal = self.zoomMaxVal
            

        return returnVal

    def bosonRunFFC(self):
        returnVal = -1
        if self.isConnect == True:

            rValue = self.myCam.bosonRunFFC()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal


    def scalerGetZoom(self):
        zoom = 0
        xCenter = 0
        yCenter = 0

        if self.isConnect == True:
            rValue, self.GetZoom = self.myCam.scalerGetZoom()

            if rValue == FLR_RESULT.R_SUCCESS:
                data = FLR_SCALER_ZOOM_PARAMS_T()
                data = self.GetZoom
                zoom = data.zoom
                xCenter = data.xCenter
                yCenter = data.yCenter
                returnVal = 0
            

        return zoom, xCenter, yCenter


    def scalerSetZoom(self,val, xCenter, yCenter):

        returnVal = -1

        if self.isConnect == True:
            self.SetZoom = val
            self.xCenter = xCenter
            self.yCenter = yCenter
            data = FLR_SCALER_ZOOM_PARAMS_T()
            data.zoom = self.SetZoom
            data.xCenter = self.xCenter
            data.yCenter = self.yCenter
            rValue = self.myCam.scalerSetZoom(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def bosonlookupFPATempDegCx10(self):
        data = 0
        if self.isConnect == True:
            rValue, data = self.myCam.bosonlookupFPATempDegCx10()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return data

    def bosonGetSoftwareRev(self):
        major = 0
        minor = 0
        patch = 0

        if self.isConnect == True:
            rValue, major, minor, patch = self.myCam.bosonGetSoftwareRev()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return major, minor, patch

    def bosonGetCameraPN(self):
        cameraStr = ''

        if self.isConnect == True:
            CameraPN = FLR_BOSON_PARTNUMBER_T()
            rValue, CameraPNval = self.myCam.bosonGetCameraPN()

            if rValue == FLR_RESULT.R_SUCCESS:
                CameraPN = CameraPNval

                for i in CameraPN.value:
                    if i != 0:
                        cameraStr = cameraStr + chr(i)

                returnVal = 0
            

        return cameraStr

    def sysctrlGetCameraFrameRate(self):
        camFPS = 0

        if self.isConnect == True:
            rValue, camFPS = self.myCam.sysctrlGetCameraFrameRate()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return camFPS

    def bosonReboot(self):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.bosonReboot()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def bosonGetFFCMode(self):
        returnVal = -1
        rData = 0

        if self.isConnect == True:
            returnVal, data = self.myCam.bosonGetFFCMode()

            if returnVal == FLR_RESULT.R_SUCCESS:
                returnVal = 0

                if data == FLR_BOSON_FFCMODE_E.FLR_BOSON_EXTERNAL_FFC:
                    rData = 2
                elif data == FLR_BOSON_FFCMODE_E.FLR_BOSON_AUTO_FFC:
                    rData = 1
                elif data == FLR_BOSON_FFCMODE_E.FLR_BOSON_MANUAL_FFC:
                    rData = 0

            else:
                current_func_name = sys._getframe().f_code.co_name
                lf.logError('[' + current_func_name + ']' + ' Function ERROR ' + str(returnVal))
                returnVal = -1

        return returnVal, rData

    def bosonSetFFCMode(self, val):

        returnVal = -1

        if self.isConnect == True:
            data = FLR_BOSON_FFCMODE_E(val)
            rValue = self.myCam.bosonSetFFCMode(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def bosonGetFFCFrameThreshold(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            returnVal, data = self.myCam.bosonGetFFCFrameThreshold()

            if returnVal == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            else:
                current_func_name = sys._getframe().f_code.co_name
                lf.logError('[' + current_func_name + ']' + ' Function ERROR ' + str(returnVal))
                returnVal = -1

        return returnVal, data

    def bosonSetFFCFrameThreshold(self, val):

        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.bosonSetFFCFrameThreshold(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def bosonGetOverTempThreshold(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.bosonGetOverTempThreshold()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def bosonGetMyriadTemp(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.bosonGetMyriadTemp()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def bosonGetGainMode(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.bosonGetGainMode()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                if data == FLR_BOSON_GAINMODE_E.FLR_BOSON_AUTO_GAIN:
                    data = 2
                elif data == FLR_BOSON_GAINMODE_E.FLR_BOSON_LOW_GAIN:
                    data = 1
                else:
                    data = 0
            

        return returnVal, data

    def bosonSetGainMode(self, val):

        returnVal = -1

        if self.isConnect == True:
            if (val >= 0) and (val <= 2):
                data = FLR_BOSON_GAINMODE_E(val)
                rValue = self.myCam.bosonSetGainMode(data)

                if rValue == FLR_RESULT.R_SUCCESS:
                    returnVal = 0
                else:
                    current_func_name = sys._getframe().f_code.co_name
                    lf.logError('[' + current_func_name + ']' + ' Function ERROR ' + str(rValue))
                    returnVal = -1
            else:
                current_func_name = sys._getframe().f_code.co_name
                lf.logError('[' + current_func_name + ']' + ' Function ERROR : ' + str(val) + ' is out of range (0~2)')
                returnVal = -1

        return returnVal

    # ----- AGC functions

    # for Tail Rejection
    def agcGetOutlierCut(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetOutlierCut()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetOutlierCut(self, colVal):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetOutlierCut(colVal)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Max gain
    def agcGetMaxGain(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetMaxGain()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetMaxGain(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetMaxGain(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Damping Factor
    def agcGetdf(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetdf()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetdf(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetdf(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Adaptive Contrast Enhancement
    def agcGetGamma(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetGamma()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetGamma(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetGamma(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Plateau value
    def agcGetPercentPerBin(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetPercentPerBin()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetPercentPerBin(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetPercentPerBin(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Linear Percent
    def agcGetLinearPercent(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetLinearPercent()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetLinearPercent(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetLinearPercent(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Detail Headroom
    def agcGetDetailHeadroom(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetDetailHeadroom()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetDetailHeadroom(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetDetailHeadroom(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Digital Detail Enhancement
    def agcGetd2br(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetd2br()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetd2br(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetd2br(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Smoothing Factor
    def agcGetSigmaR(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetSigmaR()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetSigmaR(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.agcSetSigmaR(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Imformation-Based mode
    def agcGetUseEntropy(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.agcGetUseEntropy()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                # 활성화 되어 있으면 FLR_ENABLE_E.FLR_ENABLE, int(data) 는 1
                # 비활성화 되어 있으면 FLR_ENABLE_E.FLR_DISABLE, int(data) 는 0
            

        return returnVal, data

    def agcSetUseEntropy(self, val):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_ENABLE_E(val)

            # 입력값 val 은 0 또는 1 이어야 한다.
            # 0은 disable
            # 1은 enable

            rValue = self.myCam.agcSetUseEntropy(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Flat field correction
    def gaoGetFfcState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.gaoGetFfcState()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                # 활성화 되어 있으면 FLR_ENABLE_E.FLR_ENABLE, int(data) 는 1
                # 비활성화 되어 있으면 FLR_ENABLE_E.FLR_DISABLE, int(data) 는 0
            

        return returnVal, data

    
    def gaoSetFfcState(self, val):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_ENABLE_E(val)

            # 입력값 val 은 0 또는 1 이어야 한다.
            # 0은 disable
            # 1은 enable

            rValue = self.myCam.gaoSetFfcState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Gain correction
    def gaoGetGainState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.gaoGetGainState()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                # 활성화 되어 있으면 FLR_ENABLE_E.FLR_ENABLE, int(data) 는 1
                # 비활성화 되어 있으면 FLR_ENABLE_E.FLR_DISABLE, int(data) 는 0
            

        return returnVal, data

    def gaoSetGainState(self, val):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_ENABLE_E(val)

            # 입력값 val 은 0 또는 1 이어야 한다.
            # 0은 disable
            # 1은 enable

            rValue = self.myCam.gaoSetGainState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Defect Replacement
    def bprGetState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.bprGetState()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                # 활성화 되어 있으면 FLR_ENABLE_E.FLR_ENABLE, int(data) 는 1
                # 비활성화 되어 있으면 FLR_ENABLE_E.FLR_DISABLE, int(data) 는 0
            

        return returnVal, data

    def bprSetState(self, val):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_ENABLE_E(val)

            # 입력값 val 은 0 또는 1 이어야 한다.
            # 0은 disable
            # 1은 enable

            rValue = self.myCam.bprSetState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Column filter
    def scnrGetEnableState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.scnrGetEnableState()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                # 활성화 되어 있으면 FLR_ENABLE_E.FLR_ENABLE, int(data) 는 1
                # 비활성화 되어 있으면 FLR_ENABLE_E.FLR_DISABLE, int(data) 는 0
            

        return returnVal, data

    def scnrSetEnableState(self, val):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_ENABLE_E(val)

            # 입력값 val 은 0 또는 1 이어야 한다.
            # 0은 disable
            # 1은 enable

            rValue = self.myCam.scnrSetEnableState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Temporal filter
    def tfGetEnableState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.tfGetEnableState()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                # 활성화 되어 있으면 FLR_ENABLE_E.FLR_ENABLE, int(data) 는 1
                # 비활성화 되어 있으면 FLR_ENABLE_E.FLR_DISABLE, int(data) 는 0
            

        return returnVal, data

    def tfSetEnableState(self, val):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_ENABLE_E(val)

            # 입력값 val 은 0 또는 1 이어야 한다.
            # 0은 disable
            # 1은 enable

            rValue = self.myCam.tfSetEnableState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Silent Shutterless NUC
    def spnrGetEnableState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.spnrGetEnableState()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                # 활성화 되어 있으면 FLR_ENABLE_E.FLR_ENABLE, int(data) 는 1
                # 비활성화 되어 있으면 FLR_ENABLE_E.FLR_DISABLE, int(data) 는 0
            

        return returnVal, data

    def spnrSetEnableState(self, val):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_ENABLE_E(val)

            # 입력값 val 은 0 또는 1 이어야 한다.
            # 0은 disable
            # 1은 enable

            rValue = self.myCam.spnrSetEnableState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # supplemental FFC
    def gaoGetSffcState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.gaoGetSffcState()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                # 활성화 되어 있으면 FLR_ENABLE_E.FLR_ENABLE, int(data) 는 1
                # 비활성화 되어 있으면 FLR_ENABLE_E.FLR_DISABLE, int(data) 는 0
            

        return returnVal, data

    def gaoSetSffcState(self, val):
        returnVal = -1

        if self.isConnect == True:
            data = FLR_ENABLE_E(val)

            # 입력값 val 은 0 또는 1 이어야 한다.
            # 0은 disable
            # 1은 enable

            rValue = self.myCam.gaoSetSffcState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Dynamic range Control : High-To-Low Intensity Threshold 외 2개 값 설정에 대한 함수
    def bosonGetGainSwitchParams(self):
        returnVal = -1
        pHighToLow = 0
        cHighToLow = 0
        pLowToHigh = 0
        hyPercent = 0

        data = None
        if self.isConnect == True:
            data = FLR_BOSON_GAIN_SWITCH_PARAMS_T()
            rValue, data = self.myCam.bosonGetGainSwitchParams()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
                pHighToLow = int(data.pHighToLowPercent)  # High-To-Low population Threshold
                cHighToLow = int(data.cHighToLowPercent)  # High-To-Low Intensity Threshold
                pLowToHigh = int(data.pLowToHighPercent)  # Low-To-High population Threshold
                hyPercent = int(data.hysteresisPercent)
            

        return returnVal, pHighToLow, cHighToLow, pLowToHigh, hyPercent

    def bosonSetGainSwitchParams(self, pHighToLow, cHighToLow, pLowToHigh, hyPercent):
        returnVal = -1

        data = FLR_BOSON_GAIN_SWITCH_PARAMS_T()

        if self.isConnect == True:
            data.pHighToLowPercent = int(pHighToLow)
            data.cHighToLowPercent = int(cHighToLow)
            data.pLowToHighPercent = int(pLowToHigh)
            data.hysteresisPercent = int(hyPercent)

            rValue = self.myCam.bosonSetGainSwitchParams(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for FFC Temperature Delta
    def bosonGetFFCTempThreshold(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.bosonGetFFCTempThreshold()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def bosonSetFFCTempThreshold(self, val):

        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.bosonSetFFCTempThreshold(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def gaoGetNumFFCFrames(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = self.myCam.gaoGetNumFFCFrames()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def gaoSetNumFFCFrames(self, val):

        returnVal = -1

        if self.isConnect == True:
            rValue = self.myCam.gaoSetNumFFCFrames(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal
    
    def port_check(self):
        ports = serial.tools.list_ports.comports()
        available_ports = []
        for idx, port in enumerate(ports):
            available_ports.append([port.device, port.serial_number])
        return available_ports


if __name__ == "__main__":
    CAMERA  = BosonCamAPI("COM5")
    ret = CAMERA.getSerialNumber()
    colorlud = CAMERA.colorLutGetId()
    print(f"ret = {ret}")
    print(f"colorlud = {colorlud}")
    

    
    