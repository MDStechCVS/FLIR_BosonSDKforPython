# This is a API for BOSON Camera

import sys
import os
import platform
import serial
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from UTIL.SDK_USER_PERMISSIONS import *


class BosonCamAPI():
    """
    boson camera API를 위한 클래스 -
    파라미터는 원도우일 경우 COMport 숫자
    conn() 커넥션, close()연결 해제 등등
    """
    def __init__(self, portNum):
        self.OsPlatform = platform.system()

        self.portNum = portNum      # 윈도우 라면... COM 뒤에 붙는 번호, 리눅스 이면 /dev/ttyACM 뒤에 번호

        self.isConnect = False      # boson cam 커넥션 여부 확인

        self.ProductName = 'N/A'

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
                self.myport = pyClient.Initialize(manualport= str(self.portNum), manual_baud = 921600)
            else:
                self.myport = pyClient.Initialize(manualport='/dev/ttyACM' + str(self.portNum))

            self.isConnect = True   # boson cam 커넥션 OK
            return True
        except:
            self.isConnect = False  # boson cam 커넥션 실패
            print("Connection FAIL")
            return False


    def close(self):
        try:
            pyClient.Close(self.myport)
            self.isConnect = False
            current_func_name = sys._getframe().f_code.co_name
        except Exception as e:
            print(f"Close {self.myport} FAIL")


    def sysinfoGetProductName(self):
        returnVal = 'N/A'
        if self.isConnect == True:
            rValue, self.ProductName = pyClient.sysinfoGetProductName()
            returnVal = self.ProductName

        return returnVal



    def getSerialNumber(self):
        returnVal = 'N/A'
        if self.isConnect == True:
            rValue, self.serialNum = pyClient.bosonGetCameraSN()
            print(self.serialNum)
            print(rValue)
            returnVal = self.serialNum

        return returnVal

    def colorLutGetId(self):
        returnVal = 0
        if self.isConnect == True:
            rValue, self.colorLutVal = pyClient.colorLutGetId()

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
            rValue = pyClient.colorLutSetId(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def scalerGetMaxZoom(self):
        returnVal = 'N/A'
        if self.isConnect == True:
            rValue, self.zoomMaxVal = pyClient.scalerGetMaxZoom()

            if rValue == FLR_RESULT.R_SUCCESS:
                print(self.zoomMaxVal)
                print(rValue)
                returnVal = self.zoomMaxVal
            

        return returnVal

    def bosonRunFFC(self):
        returnVal = -1
        if self.isConnect == True:

            rValue = pyClient.bosonRunFFC()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal


    def scalerGetZoom(self):
        zoom = 0
        xCenter = 0
        yCenter = 0

        if self.isConnect == True:
            rValue, self.GetZoom = pyClient.scalerGetZoom()

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
            rValue = pyClient.scalerSetZoom(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def bosonlookupFPATempDegCx10(self):
        data = 0
        if self.isConnect == True:
            rValue, data = pyClient.bosonlookupFPATempDegCx10()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return data

    def bosonGetSoftwareRev(self):
        major = 0
        minor = 0
        patch = 0

        if self.isConnect == True:
            rValue, major, minor, patch = pyClient.bosonGetSoftwareRev()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return major, minor, patch

    def bosonGetCameraPN(self):
        cameraStr = ''

        if self.isConnect == True:
            CameraPN = FLR_BOSON_PARTNUMBER_T()
            rValue, CameraPNval = pyClient.bosonGetCameraPN()

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
            rValue, camFPS = pyClient.sysctrlGetCameraFrameRate()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return camFPS

    def bosonReboot(self):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.bosonReboot()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def bosonGetFFCMode(self):
        returnVal = -1
        rData = 0

        if self.isConnect == True:
            returnVal, data = pyClient.bosonGetFFCMode()

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
            rValue = pyClient.bosonSetFFCMode(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def bosonGetFFCFrameThreshold(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            returnVal, data = pyClient.bosonGetFFCFrameThreshold()

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
            rValue = pyClient.bosonSetFFCFrameThreshold(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def bosonGetOverTempThreshold(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.bosonGetOverTempThreshold()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def bosonGetMyriadTemp(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.bosonGetMyriadTemp()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def bosonGetGainMode(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.bosonGetGainMode()

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
                rValue = pyClient.bosonSetGainMode(data)

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
            rValue, data = pyClient.agcGetOutlierCut()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetOutlierCut(self, colVal):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetOutlierCut(colVal)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Max gain
    def agcGetMaxGain(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetMaxGain()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetMaxGain(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetMaxGain(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Damping Factor
    def agcGetdf(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetdf()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetdf(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetdf(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Adaptive Contrast Enhancement
    def agcGetGamma(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetGamma()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetGamma(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetGamma(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Plateau value
    def agcGetPercentPerBin(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetPercentPerBin()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetPercentPerBin(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetPercentPerBin(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Linear Percent
    def agcGetLinearPercent(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetLinearPercent()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetLinearPercent(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetLinearPercent(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Detail Headroom
    def agcGetDetailHeadroom(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetDetailHeadroom()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetDetailHeadroom(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetDetailHeadroom(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Digital Detail Enhancement
    def agcGetd2br(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetd2br()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetd2br(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetd2br(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Smoothing Factor
    def agcGetSigmaR(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetSigmaR()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def agcSetSigmaR(self, val):
        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.agcSetSigmaR(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for Imformation-Based mode
    def agcGetUseEntropy(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.agcGetUseEntropy()

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

            rValue = pyClient.agcSetUseEntropy(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Flat field correction
    def gaoGetFfcState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.gaoGetFfcState()

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

            rValue = pyClient.gaoSetFfcState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Gain correction
    def gaoGetGainState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.gaoGetGainState()

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

            rValue = pyClient.gaoSetGainState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Defect Replacement
    def bprGetState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.bprGetState()

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

            rValue = pyClient.bprSetState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Column filter
    def scnrGetEnableState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.scnrGetEnableState()

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

            rValue = pyClient.scnrSetEnableState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Temporal filter
    def tfGetEnableState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.tfGetEnableState()

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

            rValue = pyClient.tfSetEnableState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # Silent Shutterless NUC
    def spnrGetEnableState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.spnrGetEnableState()

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

            rValue = pyClient.spnrSetEnableState(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # supplemental FFC
    def gaoGetSffcState(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.gaoGetSffcState()

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

            rValue = pyClient.gaoSetSffcState(data)

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
            rValue, data = pyClient.bosonGetGainSwitchParams()

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

            rValue = pyClient.bosonSetGainSwitchParams(data)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    # for FFC Temperature Delta
    def bosonGetFFCTempThreshold(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.bosonGetFFCTempThreshold()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def bosonSetFFCTempThreshold(self, val):

        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.bosonSetFFCTempThreshold(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal

    def gaoGetNumFFCFrames(self):
        returnVal = -1
        data = None
        if self.isConnect == True:
            rValue, data = pyClient.gaoGetNumFFCFrames()

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal, data

    def gaoSetNumFFCFrames(self, val):

        returnVal = -1

        if self.isConnect == True:
            rValue = pyClient.gaoSetNumFFCFrames(val)

            if rValue == FLR_RESULT.R_SUCCESS:
                returnVal = 0
            

        return returnVal
    

    
    