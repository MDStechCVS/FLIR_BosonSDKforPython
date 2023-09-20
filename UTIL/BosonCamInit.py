
import serial.tools.list_ports
import UTIL.BosonCamAPI as BsCam 


class BosonCamInitClass():
    def __init__(self, windows, portNum):
        self.windows = windows
        self.bsCam = 0

        # 현재 커넥션 여부
        self.isConnect = False

        # 카메라 정보
        self.serialNumber = 0

        # 접속된 카메라의 줌 최대 값
        self.zoomMaxVal = 0
        self.zoomMinVal = 0

        # 현재 줌 설정값 확인
        self.zoomVal = 0
        self.zoomXCenter = 0
        self.zoomYCenter = 0

        # 현재 LUT 값 0 ~ 9
        self.lutValue = 0
        
        self.portNum = portNum

    def camConnect(self):
        
        self.bsCam = BsCam.BosonCamAPI(self.portNum)
        
        self.isConnect = self.bsCam.conn()
        self.serialNumber = self.bsCam.getSerialNumber()
        self.CamProc = self.bsCam.bosonGetCameraPN()
        
        # connect 시 모든 정보 불러옴.
        '''
        if self.isConnect == True:
            # 초기화 할때 가져올수 있는 정보를 확보 한다.
            self.serialNumber = self.bsCam.getSerialNumber()
            self.zoomMaxVal = self.bsCam.scalerGetMaxZoom()
            self.zoomVal, self.zoomXCenter, self.zoomYCenter = self.bsCam.scalerGetZoom()
            print('zoomVal: ' + str(self.zoomVal) + ' zoomXCenter: ' + str(self.zoomXCenter) + ' zoomYCenter: ' + str(self.zoomYCenter))

            # LUT 정보 가져오기
            self.lutValue = self.bsCam.colorLutGetId()

            # UI2 의 정보 가져오기
            # Diagnostic Tools - STATUS PANEL
            # ---TFPA
            self.TFPAvalue = float(self.bsCam.bosonlookupFPATempDegCx10()) / 10     # 나누기 10을 해줘야 함
            print('TFPA: ' + str(self.TFPAvalue))

            # ---Camera Software Revision
            major, minor, patch = self.bsCam.bosonGetSoftwareRev()
            self.SWRevision = str(major) + '.' + str(minor) + '.' + str(patch)
            print('SW Rev: ' + str(self.SWRevision))

            # ---Camera Product Number
            self.CamProc = self.bsCam.bosonGetCameraPN()
            print('Camera PN: ' + str(self.CamProc))

            # ---Camera Serial Number
            # self.serialNumber에 값이 있음. 위에서 값을 가져왔음.

            # ---Camera FFC mode
            # mode 2 : external mode
            # mode 1 : auto mode
            # mode 0 : manual mode
            retunVal, self.FFCMode = self.bsCam.bosonGetFFCMode()
            print('FFC mode: ' + str(self.FFCMode))

            # ---Camera FFC period
            retunVal, self.FFCPeriod = self.bsCam.bosonGetFFCFrameThreshold()
            print('FFC period: ' + str(self.FFCPeriod))

            # ---Camera FFC Temperature Delta
            retunVal, self.FFCTempDelta = self.bsCam.bosonGetFFCTempThreshold()
            print('FFC Temp delta: ' + str(self.FFCTempDelta))

            # ---Camera FFC Integration Period
            retunVal, self.FFCIPval = self.bsCam.gaoGetNumFFCFrames()
            print('FFC Integration period: ' + str(self.FFCIPval))

            # ---Camera Gain mode
            retunVal, self.GainMode = self.bsCam.bosonGetGainMode()
            print('Gain mode: ' + str(self.GainMode))

            # ---Dynamic range control values
            returnVal, self.pHighToLow, self.cHighToLow, self.pLowToHigh, self.hyPercent = self.getGainSwitchParams()
            print('Gain mode high to Low Intensity: ' + str(self.cHighToLow) +
                  ' High to Low Pop: ' + str(self.pHighToLow) +
                  ' Low to High Pop: ' + str(self.pLowToHigh) +
                  ' hyPercent: ' + str(self.hyPercent))

            # --- AGC functions
            self.TailRej = 0
            self.MaxGain = 0.25
            self.DampingFactor = 0
            self.ACE = 0.5
            self.PlateauVal = 1
            self.LinearPer = 1
            self.DetailHeadroom = 0
            self.DDE = 0.0
            self.SmoothingFactor = 1
            self.ImageBasedMode = 1

            self.getAGCControls()   # 값 가져오기

            # --- ADVANCED
            self.FFCEnable = 1
            self.GainEnable = 1
            self.DefectRepEnable = 1
            self.ColumnFilterEnable = 1
            self.TemporalFilterEnable = 1
            self.SSNUCEnable = 1
            self.SFFCEnable = 1

            # advanced 정보 가져오기
            self.getFFCState()
            self.getGCState()
            self.getDR()
            self.getCF()
            self.getTF()
            self.getSSNUC()
            self.getSFFC()
        '''

        return self.isConnect, self.CamProc 

    
    def getSerialNum(self):
        return self.serialNumber

    def getZoomMaxval(self):
        return self.zoomMaxVal

    def setZoomValue(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.scalerSetZoom(val, self.zoomXCenter, self.zoomYCenter)

        return rValue

    def setLutID(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.colorLutSetId(val)
            if rValue == 0:
                self.lutValue = val

        return rValue
    
    
    def getLutID(self):
        rValue = -1
        if self.isConnect == True:
            rValue = self.bsCam.colorLutGetId()
        return rValue
        
    def doFFC(self):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.bosonRunFFC()

        return rValue

    def getTFPAtemperature(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.bosonlookupFPATempDegCx10()
        return rValue

    def camClose(self):
        rValue = False

        if self.isConnect == True:
            self.bsCam.close()
            self.isConnect = False
            rValue = True

        return rValue

    def camReboot(self):
        rValue = False

        if self.isConnect == True:
            self.bsCam.bosonReboot()
            self.isConnect = False
            rValue = True

        return rValue

    def setFFCMode(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.bosonSetFFCMode(val)
            if rValue == 0:
                self.FFCMode = val

        return rValue

    def setFFCperiod(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.bosonSetFFCFrameThreshold(val)
            if rValue == 0:
                self.FFCPeriod = val

        return rValue

    def setFFCTempThreshold(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.bosonSetFFCTempThreshold(val)
            if rValue == 0:
                self.FFCTempDelta = val     # 가져오는 온도 값은 설정값의 10배이다.

        return rValue

    def getOverTempThreshold(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.bosonGetOverTempThreshold()

        return data

    def getMyriadTemp(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.bosonGetMyriadTemp()

        return data

    def getGainMode(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.bosonGetGainMode()
            if rValue == 0:
                self.GainMode = data

        return data

    def setGainMode(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.bosonSetGainMode(val)

        return rValue

    def getAGCControls(self):
        if self.isConnect == True:
            rValue, data = self.bsCam.agcGetOutlierCut()
            if rValue == 0:
                self.TailRej = data

            rValue, data = self.bsCam.agcGetMaxGain()
            if rValue == 0:
                self.MaxGain = data

            rValue, data = self.bsCam.agcGetdf()
            if rValue == 0:
                self.DampingFactor = data

            rValue, data = self.bsCam.agcGetGamma()
            if rValue == 0:
                self.ACE = data

            rValue, data = self.bsCam.agcGetPercentPerBin()
            if rValue == 0:
                self.PlateauVal = data

            rValue, data = self.bsCam.agcGetLinearPercent()
            if rValue == 0:
                self.LinearPer = data

            rValue, data = self.bsCam.agcGetDetailHeadroom()
            if rValue == 0:
                self.DetailHeadroom = data

            rValue, data = self.bsCam.agcGetd2br()
            if rValue == 0:
                self.DDE = data

            rValue, data = self.bsCam.agcGetSigmaR()
            if rValue == 0:
                self.SmoothingFactor = data

            rValue, data = self.bsCam.agcGetUseEntropy()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.ImageBasedMode = data

    def setTailRej(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetOutlierCut(val)
            if rValue == 0:
                self.TailRej = val

        return rValue

    def setMaxGain(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetMaxGain(val)
            if rValue == 0:
                self.MaxGain = val

        return rValue

    def setDampingFactor(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetdf(val)
            if rValue == 0:
                self.DampingFactor = val

        return rValue

    def setACE(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetGamma(val)
            if rValue == 0:
                self.ACE = val

        return rValue

    def setPlateauValue(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetPercentPerBin(val)
            if rValue == 0:
                self.PlateauVal = val

        return rValue

    def setLinearPercent(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetLinearPercent(val)
            if rValue == 0:
                self.LinearPer = val

        return rValue

    def setDetailHeadroom(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetDetailHeadroom(val)
            if rValue == 0:
                self.DetailHeadroom = val

        return rValue

    def setDDE(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetd2br(val)
            if rValue == 0:
                self.DDE = val

        return rValue

    def setSmoothingFactor(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetSigmaR(val)
            if rValue == 0:
                self.SmoothingFactor = val

    def setImageBasedMode(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.agcSetUseEntropy(val)
            if rValue == 0:
                self.ImageBasedMode = val

        return rValue


    # Flat field correction
    def getFFCState(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.gaoGetFfcState()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.FFCEnable = data

    def setFFCState(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.gaoSetFfcState(val)
            if rValue == 0:
                self.FFCEnable = val

    # Gain correction
    def getGCState(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.gaoGetGainState()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.GainEnable = data

    def setGCState(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.gaoSetGainState(val)
            if rValue == 0:
                self.GainEnable = val

    # Defect Replacement
    def getDR(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.bprGetState()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.DefectRepEnable = data

    def setDR(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.bprSetState(val)
            if rValue == 0:
                self.DefectRepEnable = val

    # Column filter
    def getCF(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.scnrGetEnableState()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.ColumnFilterEnable = data

    def setCF(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.scnrSetEnableState(val)
            if rValue == 0:
                self.ColumnFilterEnable = val

    # Temporal filter
    def getTF(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.tfGetEnableState()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.TemporalFilterEnable = data

    def setTF(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.tfSetEnableState(val)
            if rValue == 0:
                self.TemporalFilterEnable = val

        return rValue

    # Silent Sutterless NUC
    def getSSNUC(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.spnrGetEnableState()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.SSNUCEnable = data

    def setSSNUC(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.spnrSetEnableState(val)
            if rValue == 0:
                self.SSNUCEnable = val

        return rValue


    # supplemental FFC
    def getSFFC(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.gaoGetSffcState()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.SFFCEnable = data

    def setSFFC(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.gaoSetSffcState(val)
            if rValue == 0:
                self.SFFCEnable = val

        return rValue

    def getGainSwitchParams(self):
        rValue = -1
        pHtoL = 0
        cHtoL = 0
        pLtoH = 0
        hyPercent = 0

        if self.isConnect == True:
            rValue, pHtoL, cHtoL, pLtoH, hyPercent = self.bsCam.bosonGetGainSwitchParams()
            if rValue != 0:
                print('getGainSwitchParam is FAIL : ' + str(rValue))
                rValue = -1

        return rValue, pHtoL, cHtoL, pLtoH, hyPercent

    def setGainSwitchParams(self, pHtoL, cHtoL, pLtoH):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.bosonSetGainSwitchParams(pHtoL, cHtoL, pLtoH, self.hyPercent)
            if rValue != 0:
                print('setGainSwitchParam is FAIL : ' + str(rValue))
                rValue = -1
            else:
                self.pHighToLow = pHtoL
                self.cHighToLow = cHtoL
                self.pLowToHigh = pLtoH

        return rValue

    def getNumFFCFrames(self):
        rValue = -1

        if self.isConnect == True:
            rValue, data = self.bsCam.gaoGetNumFFCFrames()
            if rValue == 0:
                if int(data) == 0:
                    data = 0
                else:
                    data = 1

                self.FFCIPval = data


    def setNumFFCFrames(self, val):
        rValue = -1

        if self.isConnect == True:
            rValue = self.bsCam.gaoSetNumFFCFrames(val)
            if rValue == 0:
                self.FFCIPval = val

        return rValue


# find Serial  Port
class Make_Port_List():
    def __init__(self):
        self.camera_id = 0
        
      
    def port_check(self):
        ports = serial.tools.list_ports.comports()
        available_ports = []
        for idx, port in enumerate(ports):
            # if 'FLIR' in port.description:
            available_ports.append([port.device, port.serial_number])
        return available_ports
    

