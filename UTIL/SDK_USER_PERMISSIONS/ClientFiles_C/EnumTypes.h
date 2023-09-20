//  /////////////////////////////////////////////////////
//  // DO NOT EDIT.  This is a machine generated file. //
//  /////////////////////////////////////////////////////

/******************************************************************************/
/*                                                                            */
/*  Copyright (C) 2018, FLIR Systems                                          */
/*  All rights reserved.                                                      */
/*                                                                            */
/*  This document is controlled to FLIR Technology Level 2. The information   */
/*  contained in this document pertains to a dual use product controlled for  */
/*  export by the Export Administration Regulations (EAR). Diversion contrary */
/*  to US law is prohibited. US Department of Commerce authorization is not   */
/*  required prior to export or transfer to foreign persons or parties unless */
/*  otherwise prohibited.                                                     */
/*                                                                            */
/******************************************************************************/


#ifndef ENUM_TYPES_H
#define ENUM_TYPES_H

#include <stdint.h>


enum e_FLR_ENABLE_E {
    FLR_DISABLE = (int32_t) 0,
    FLR_ENABLE = (int32_t) 1,
    FLR_ENABLE_END = (int32_t) 2,
};
typedef enum e_FLR_ENABLE_E FLR_ENABLE_E;

enum e_FLR_GAO_NUC_TYPE_E {
    FLR_GAO_NUC_TYPE_ONE_POINT_FFC = (int32_t) 0,
    FLR_GAO_NUC_TYPE_TWO_POINT_FIELD = (int32_t) 1,
    FLR_GAO_NUC_TYPE_TWO_POINT_FACTORY = (int32_t) 2,
    FLR_GAO_NUC_TYPE_END = (int32_t) 3,
};
typedef enum e_FLR_GAO_NUC_TYPE_E FLR_GAO_NUC_TYPE_E;

enum e_FLR_ROIC_TEMP_MODE_E {
    FLR_ROIC_TEMP_NORMAL_MODE = (int32_t) 0,
    FLR_ROIC_TEMP_OFFSET_MODE = (int32_t) 1,
    FLR_ROIC_TEMP_STATIC_MODE = (int32_t) 2,
    FLR_ROIC_TEMP_MODE_END = (int32_t) 3,
};
typedef enum e_FLR_ROIC_TEMP_MODE_E FLR_ROIC_TEMP_MODE_E;

enum e_FLR_ROIC_EXT_SYNC_MODE_E {
    FLR_ROIC_EXT_SYNC_DISABLE_MODE = (int32_t) 0,
    FLR_ROIC_EXT_SYNC_MASTER_MODE = (int32_t) 1,
    FLR_ROIC_EXT_SYNC_SLAVE_MODE = (int32_t) 2,
    FLR_ROIC_EXT_SYNC_END = (int32_t) 3,
};
typedef enum e_FLR_ROIC_EXT_SYNC_MODE_E FLR_ROIC_EXT_SYNC_MODE_E;

enum e_FLR_BPR_DISPLAY_MODE_E {
    FLR_BPR_NORMAL_DISPLAY_MODE = (int32_t) 0,
    FLR_BPR_MIN_VALUE_ONLY_MODE = (int32_t) 1,
    FLR_BPR_MAX_VALUE_ONLY_MODE = (int32_t) 2,
    FLR_BPR_MIN_MAX_TOGGLE_MODE = (int32_t) 3,
    FLR_BPR_BPR_DISPLAY_MODE_END = (int32_t) 4,
};
typedef enum e_FLR_BPR_DISPLAY_MODE_E FLR_BPR_DISPLAY_MODE_E;

enum e_FLR_TELEMETRY_LOC_E {
    FLR_TELEMETRY_LOC_TOP = (int32_t) 0,
    FLR_TELEMETRY_LOC_BOTTOM = (int32_t) 1,
    FLR_TELEMETRY_LOC_END = (int32_t) 2,
};
typedef enum e_FLR_TELEMETRY_LOC_E FLR_TELEMETRY_LOC_E;

enum e_FLR_TELEMETRY_PACKING_E {
    FLR_TELEMETRY_PACKING_DEFAULT = (int32_t) 0,
    FLR_TELEMETRY_PACKING_Y = (int32_t) 1,
    FLR_TELEMETRY_PACKING_8BITS = (int32_t) 2,
    FLR_TELEMETRY_PACKING_END = (int32_t) 3,
};
typedef enum e_FLR_TELEMETRY_PACKING_E FLR_TELEMETRY_PACKING_E;

enum e_FLR_BOSON_GAINMODE_E {
    FLR_BOSON_HIGH_GAIN = (int32_t) 0,
    FLR_BOSON_LOW_GAIN = (int32_t) 1,
    FLR_BOSON_AUTO_GAIN = (int32_t) 2,
    FLR_BOSON_DUAL_GAIN = (int32_t) 3,
    FLR_BOSON_MANUAL_GAIN = (int32_t) 4,
    FLR_BOSON_GAINMODE_END = (int32_t) 5,
};
typedef enum e_FLR_BOSON_GAINMODE_E FLR_BOSON_GAINMODE_E;

enum e_FLR_BOSON_FFCMODE_E {
    FLR_BOSON_MANUAL_FFC = (int32_t) 0,
    FLR_BOSON_AUTO_FFC = (int32_t) 1,
    FLR_BOSON_EXTERNAL_FFC = (int32_t) 2,
    FLR_BOSON_SHUTTER_TEST_FFC = (int32_t) 3,
    FLR_BOSON_FFCMODE_END = (int32_t) 4,
};
typedef enum e_FLR_BOSON_FFCMODE_E FLR_BOSON_FFCMODE_E;

enum e_FLR_BOSON_TIMESTAMPTYPE_E {
    FLR_BOSON_UARTINIT = (int32_t) 0,
    FLR_BOSON_PIXELCLOCKINIT = (int32_t) 1,
    FLR_BOSON_AUTHEVENT = (int32_t) 2,
    FLR_BOSON_FIRSTVALIDIMAGE = (int32_t) 3,
    FLR_BOSON_TIMESTAMPTYPE_END = (int32_t) 4,
};
typedef enum e_FLR_BOSON_TIMESTAMPTYPE_E FLR_BOSON_TIMESTAMPTYPE_E;

enum e_FLR_BOSON_FFCSTATUS_E {
    FLR_BOSON_NO_FFC_PERFORMED = (int32_t) 0,
    FLR_BOSON_FFC_IMMINENT = (int32_t) 1,
    FLR_BOSON_FFC_IN_PROGRESS = (int32_t) 2,
    FLR_BOSON_FFC_COMPLETE = (int32_t) 3,
    FLR_BOSON_FFCSTATUS_END = (int32_t) 4,
};
typedef enum e_FLR_BOSON_FFCSTATUS_E FLR_BOSON_FFCSTATUS_E;

enum e_FLR_BOSON_MYRIADTEMPMODE_E {
    FLR_BOSON_NORMAL_MYRIADTEMP_MODE = (int32_t) 0,
    FLR_BOSON_STATIC_MYRIADTEMP_MODE = (int32_t) 1,
};
typedef enum e_FLR_BOSON_MYRIADTEMPMODE_E FLR_BOSON_MYRIADTEMPMODE_E;

enum e_FLR_BOSON_EXT_SYNC_MODE_E {
    FLR_BOSON_EXT_SYNC_DISABLE_MODE = (int32_t) 0,
    FLR_BOSON_EXT_SYNC_MASTER_MODE = (int32_t) 1,
    FLR_BOSON_EXT_SYNC_SLAVE_MODE = (int32_t) 2,
    FLR_BOSON_EXT_SYNC_END = (int32_t) 3,
};
typedef enum e_FLR_BOSON_EXT_SYNC_MODE_E FLR_BOSON_EXT_SYNC_MODE_E;

enum e_FLR_BOSON_TEMP_DIODE_STATUS_E {
    FLR_BOSON_TEMP_DIODE_NORMAL = (int32_t) 0,
    FLR_BOSON_TEMP_DIODE_FAULT = (int32_t) 1,
    FLR_BOSON_TEMP_DIODE_END = (int32_t) 2,
};
typedef enum e_FLR_BOSON_TEMP_DIODE_STATUS_E FLR_BOSON_TEMP_DIODE_STATUS_E;

enum e_FLR_DVO_OUTPUT_FORMAT_E {
    FLR_DVO_RGB = (int32_t) 0,
    FLR_DVO_YCBCR = (int32_t) 1,
    FLR_DVO_DEFAULT_FORMAT = (int32_t) 2,
    FLR_DVO_IR16 = (int32_t) 3,
    FLR_DVO_OUTPUT_FORMAT_END = (int32_t) 4,
};
typedef enum e_FLR_DVO_OUTPUT_FORMAT_E FLR_DVO_OUTPUT_FORMAT_E;

enum e_FLR_DVO_OUTPUT_RGB_FORMAT_E {
    FLR_DVO_RGB888 = (int32_t) 0,
    FLR_DVO_MRGB888 = (int32_t) 1,
    FLR_DVO_OUTPUT_RGB_FORMAT_END = (int32_t) 2,
};
typedef enum e_FLR_DVO_OUTPUT_RGB_FORMAT_E FLR_DVO_OUTPUT_RGB_FORMAT_E;

enum e_FLR_DVO_OUTPUT_YCBCR_FORMAT_E {
    FLR_DVO_YCBCR422_8B = (int32_t) 0,
    FLR_DVO_MYCBCR422_8B = (int32_t) 1,
    FLR_DVO_OUTPUT_YCBCR_FORMAT_END = (int32_t) 2,
};
typedef enum e_FLR_DVO_OUTPUT_YCBCR_FORMAT_E FLR_DVO_OUTPUT_YCBCR_FORMAT_E;

enum e_FLR_DVO_OUTPUT_IR16_FORMAT_E {
    FLR_DVO_IR16_16B = (int32_t) 0,
    FLR_DVO_MIR16_8B = (int32_t) 1,
    FLR_DVO_OUTPUT_IR16_FORMAT_END = (int32_t) 2,
};
typedef enum e_FLR_DVO_OUTPUT_IR16_FORMAT_E FLR_DVO_OUTPUT_IR16_FORMAT_E;

enum e_FLR_DVO_OUTPUT_CBCR_ORDER_E {
    FLR_DVO_CRCB = (int32_t) 0,
    FLR_DVO_CBCR = (int32_t) 1,
    FLR_DVO_OUTPUT_CBCR_ORDER_END = (int32_t) 2,
};
typedef enum e_FLR_DVO_OUTPUT_CBCR_ORDER_E FLR_DVO_OUTPUT_CBCR_ORDER_E;

enum e_FLR_DVO_OUTPUT_Y_ORDER_E {
    FLR_DVO_YFIRST = (int32_t) 0,
    FLR_DVO_YLAST = (int32_t) 1,
    FLR_DVO_OUTPUT_Y_ORDER_END = (int32_t) 2,
};
typedef enum e_FLR_DVO_OUTPUT_Y_ORDER_E FLR_DVO_OUTPUT_Y_ORDER_E;

enum e_FLR_DVO_OUTPUT_RGB_ORDER_E {
    FLR_DVO_ORDER_RGB = (int32_t) 0,
    FLR_DVO_ORDER_BGR = (int32_t) 1,
    FLR_DVO_OUTPUT_RGB_ORDER_END = (int32_t) 2,
};
typedef enum e_FLR_DVO_OUTPUT_RGB_ORDER_E FLR_DVO_OUTPUT_RGB_ORDER_E;

enum e_FLR_DVO_TYPE_E {
    FLR_DVO_TYPE_MONO16 = (int32_t) 0,
    FLR_DVO_TYPE_MONO8 = (int32_t) 1,
    FLR_DVO_TYPE_COLOR = (int32_t) 2,
    FLR_DVO_TYPE_ANALOG = (int32_t) 3,
    FLR_DVO_TYPE_END = (int32_t) 4,
};
typedef enum e_FLR_DVO_TYPE_E FLR_DVO_TYPE_E;

enum e_FLR_DVO_DISPLAY_MODE_E {
    FLR_DVO_CONTINUOUS = (int32_t) 0,
    FLR_DVO_ONE_SHOT = (int32_t) 1,
    FLR_DVO_DISPLAY_MODE_END = (int32_t) 2,
};
typedef enum e_FLR_DVO_DISPLAY_MODE_E FLR_DVO_DISPLAY_MODE_E;

enum e_FLR_DVO_VIDEO_STANDARD_E {
    FLR_DVO_NTSC = (int32_t) 0,
    FLR_DVO_PAL = (int32_t) 1,
    FLR_DVO_VIDEO_STANDARD_END = (int32_t) 2,
};
typedef enum e_FLR_DVO_VIDEO_STANDARD_E FLR_DVO_VIDEO_STANDARD_E;

enum e_FLR_DVO_LCD_CONFIG_ID_E {
    FLR_DVO_DEFAULT = (int32_t) 0,
    FLR_DVO_CUSTOM1 = (int32_t) 1,
    FLR_DVO_CUSTOM2 = (int32_t) 2,
    FLR_DVO_CONFIG1 = (int32_t) 3,
    FLR_DVO_CONFIG2 = (int32_t) 4,
};
typedef enum e_FLR_DVO_LCD_CONFIG_ID_E FLR_DVO_LCD_CONFIG_ID_E;

enum e_FLR_CAPTURE_SRC_E {
    FLR_CAPTURE_SRC_NUC = (int32_t) 1,
    FLR_CAPTURE_SRC_RESERVED = (int32_t) 2,
    FLR_CAPTURE_SRC_TNF = (int32_t) 3,
    FLR_CAPTURE_SRC_BLEND = (int32_t) 4,
    FLR_CAPTURE_SRC_VIS = (int32_t) 5,
    FLR_CAPTURE_SRC_MSX = (int32_t) 6,
    FLR_CAPTURE_SRC_END = (int32_t) 7,
};
typedef enum e_FLR_CAPTURE_SRC_E FLR_CAPTURE_SRC_E;

enum e_FLR_CAPTURE_FILE_TYPE_E {
    FLR_CAPTURE_NONE = (int32_t) 0,
    FLR_CAPTURE_JPEG = (int32_t) 1,
    FLR_CAPTURE_PNG = (int32_t) 2,
};
typedef enum e_FLR_CAPTURE_FILE_TYPE_E FLR_CAPTURE_FILE_TYPE_E;

enum e_FLR_AGC_MODE_E {
    FLR_AGC_MODE_NORMAL = (int32_t) 0,
    FLR_AGC_MODE_HOLD = (int32_t) 1,
    FLR_AGC_MODE_THRESHOLD = (int32_t) 2,
    FLR_AGC_MODE_END = (int32_t) 3,
};
typedef enum e_FLR_AGC_MODE_E FLR_AGC_MODE_E;

enum e_FLR_TF_MOTION_MODE_E {
    FLR_TF_MOTION_MODE_FRAME_BASED = (int32_t) 0,
    FLR_TF_MOTION_MODE_MOTION_BASED = (int32_t) 1,
    FLR_TF_MOTION_MODE_END = (int32_t) 2,
};
typedef enum e_FLR_TF_MOTION_MODE_E FLR_TF_MOTION_MODE_E;

enum e_FLR_MEM_LOCATION_E {
    FLR_MEM_INVALID = (int32_t) 0,
    FLR_MEM_BOOTLOADER = (int32_t) 1,
    FLR_MEM_UPGRADE_APP = (int32_t) 2,
    FLR_MEM_LENS_NVFFC = (int32_t) 3,
    FLR_MEM_LENS_SFFC = (int32_t) 4,
    FLR_MEM_LENS_GAIN = (int32_t) 5,
    FLR_MEM_LENS_DISTORTION = (int32_t) 6,
    FLR_MEM_USER_SPACE = (int32_t) 7,
    FLR_MEM_RUN_CMDS = (int32_t) 8,
    FLR_MEM_JFFS2 = (int32_t) 9,
    FLR_MEM_LAST = (int32_t) 10,
};
typedef enum e_FLR_MEM_LOCATION_E FLR_MEM_LOCATION_E;

enum e_FLR_COLORLUT_ID_E {
    FLR_COLORLUT_0 = (int32_t) 0,
    FLR_COLORLUT_DEFAULT = (int32_t) 0,
    FLR_COLORLUT_WHITEHOT = (int32_t) 0,
    FLR_COLORLUT_1 = (int32_t) 1,
    FLR_COLORLUT_BLACKHOT = (int32_t) 1,
    FLR_COLORLUT_2 = (int32_t) 2,
    FLR_COLORLUT_RAINBOW = (int32_t) 2,
    FLR_COLORLUT_3 = (int32_t) 3,
    FLR_COLORLUT_RAINBOW_HC = (int32_t) 3,
    FLR_COLORLUT_4 = (int32_t) 4,
    FLR_COLORLUT_IRONBOW = (int32_t) 4,
    FLR_COLORLUT_5 = (int32_t) 5,
    FLR_COLORLUT_LAVA = (int32_t) 5,
    FLR_COLORLUT_6 = (int32_t) 6,
    FLR_COLORLUT_ARCTIC = (int32_t) 6,
    FLR_COLORLUT_7 = (int32_t) 7,
    FLR_COLORLUT_GLOBOW = (int32_t) 7,
    FLR_COLORLUT_8 = (int32_t) 8,
    FLR_COLORLUT_GRADEDFIRE = (int32_t) 8,
    FLR_COLORLUT_9 = (int32_t) 9,
    FLR_COLORLUT_HOTTEST = (int32_t) 9,
    FLR_COLORLUT_ID_END = (int32_t) 10,
};
typedef enum e_FLR_COLORLUT_ID_E FLR_COLORLUT_ID_E;

enum e_FLR_SPNR_STATE_E {
    FLR_SPNR_READY = (int32_t) 0,
    FLR_SPNR_DESIRED = (int32_t) 1,
    FLR_SPNR_IN_PROGRESS = (int32_t) 2,
    FLR_SPNR_COMPLETE = (int32_t) 3,
};
typedef enum e_FLR_SPNR_STATE_E FLR_SPNR_STATE_E;

enum e_FLR_SPNR_ONESHOT_STATE_E {
    FLR_SPNR_ONE_SHOT_READY = (int32_t) 0,
    FLR_SPNR_ONE_SHOT_EXECUTE = (int32_t) 1,
    FLR_SPNR_ONE_SHOT_RESET = (int32_t) 2,
    FLR_SPNR_ONE_SHOT_INIT = (int32_t) 3,
    FLR_SPNR_ONE_SHOT_ABORT = (int32_t) 4,
};
typedef enum e_FLR_SPNR_ONESHOT_STATE_E FLR_SPNR_ONESHOT_STATE_E;

enum e_FLR_TESTRAMP_TYPE_E {
    FLR_TESTRAMP_ZERO = (int32_t) 0,
    FLR_TESTRAMP_INCREMENTING = (int32_t) 1,
    FLR_TESTRAMP_VERT_SHADE = (int32_t) 2,
    FLR_TESTRAMP_HORIZ_SHADE = (int32_t) 3,
    FLR_TESTRAMP_BIG_VERT_SHADE = (int32_t) 4,
    FLR_TESTRAMP_SIMPLE_VERTICAL = (int32_t) 5,
    FLR_TESTRAMP_VTST_CHECKERBOARD = (int32_t) 6,
    FLR_TESTRAMP_VTST_DIAGONAL_STRIPE = (int32_t) 7,
    FLR_TESTRAMP_VTST_MOVING_LINE_BLACK = (int32_t) 8,
    FLR_TESTRAMP_VTST_DIAGONAL_LR = (int32_t) 9,
    FLR_TESTRAMP_VTST_DIAGONAL_RL = (int32_t) 10,
    FLR_TESTRAMP_TYPE_LAST = (int32_t) 11,
};
typedef enum e_FLR_TESTRAMP_TYPE_E FLR_TESTRAMP_TYPE_E;

enum e_FLR_SYMBOLOGY_TEXT_ALIGNMENT_E {
    FLR_SYMBOLOGY_LEFT_TOP = (int16_t) 17,
    FLR_SYMBOLOGY_CENTER_TOP = (int16_t) 18,
    FLR_SYMBOLOGY_RIGHT_TOP = (int16_t) 19,
    FLR_SYMBOLOGY_LEFT_MIDDLE = (int16_t) 33,
    FLR_SYMBOLOGY_CENTER_MIDDLE = (int16_t) 34,
    FLR_SYMBOLOGY_RIGHT_MIDDLE = (int16_t) 35,
    FLR_SYMBOLOGY_LEFT_BOTTOM = (int16_t) 49,
    FLR_SYMBOLOGY_CENTER_BOTTOM = (int16_t) 50,
    FLR_SYMBOLOGY_RIGHT_BOTTOM = (int16_t) 51,
    FLR_SYMBOLOGY_ALIGNMENT_LAST = (int16_t) 64,
};
typedef enum e_FLR_SYMBOLOGY_TEXT_ALIGNMENT_E FLR_SYMBOLOGY_TEXT_ALIGNMENT_E;

enum e_FLR_SYMBOLOGY_TRANSFORMATION_E {
    FLR_SYMBOLOGY_TRANSFORMATION_NONE = (int16_t) 0,
    FLR_SYMBOLOGY_TRANSFORMATION_FLIP_BOTH = (int16_t) 1,
    FLR_SYMBOLOGY_TRANSFORMATION_FLIP_HORIZONTAL = (int16_t) 2,
    FLR_SYMBOLOGY_TRANSFORMATION_FLIP_VERTICAL = (int16_t) 3,
};
typedef enum e_FLR_SYMBOLOGY_TRANSFORMATION_E FLR_SYMBOLOGY_TRANSFORMATION_E;

enum e_FLR_SYMBOLOGY_IMAGE_TYPE_E {
    FLR_SYMBOLOGY_RAW_IMAGE = (int16_t) 0,
    FLR_SYMBOLOGY_PNG_IMAGE = (int16_t) 1,
    FLR_SYMBOLOGY_JPEG_IMAGE = (int16_t) 2,
    FLR_SYMBOLOGY_BMP_IMAGE = (int16_t) 3,
};
typedef enum e_FLR_SYMBOLOGY_IMAGE_TYPE_E FLR_SYMBOLOGY_IMAGE_TYPE_E;

enum e_FLR_SYMBOLOGY_SCALING_MODE_E {
    FLR_SYMBOLOGY_SCALING_MODE_NONE = (int16_t) 0,
    FLR_SYMBOLOGY_SCALING_MODE_FIT = (int16_t) 1,
    FLR_SYMBOLOGY_SCALING_MODE_CROP = (int16_t) 2,
    FLR_SYMBOLOGY_SCALING_MODE_FILL = (int16_t) 3,
};
typedef enum e_FLR_SYMBOLOGY_SCALING_MODE_E FLR_SYMBOLOGY_SCALING_MODE_E;

enum e_FLR_JFFS2_STATE_E {
    FLR_JFFS2_INITIAL = (int32_t) 0,
    FLR_JFFS2_CONFIGURED = (int32_t) 1,
    FLR_JFFS2_MOUNTING = (int32_t) 2,
    FLR_JFFS2_MOUNTED = (int32_t) 3,
    FLR_JFFS2_UNMOUNTING = (int32_t) 4,
    FLR_JFFS2_UNMOUNTED = (int32_t) 5,
    FLR_JFFS2_FAILED_MOUNT = (int32_t) 6,
    FLR_JFFS2_FAILED_UNMOUNT = (int32_t) 7,
    FLR_JFFS2_FAILED_CONFIG = (int32_t) 8,
    FLR_JFFS2_DISABLED = (int32_t) 9,
    FLR_JFFS2_STATE_END = (int32_t) 10,
};
typedef enum e_FLR_JFFS2_STATE_E FLR_JFFS2_STATE_E;

enum e_FLR_SPLASHSCREEN_FILETYPE_E {
    FLR_SPLASHSCREEN_PNG = (int32_t) 0,
    FLR_SPLASHSCREEN_BMP = (int32_t) 1,
    FLR_SPLASHSCREEN_RAW = (int32_t) 2,
    FLR_SPLASHSCREEN_NONE = (int32_t) 3,
    FLR_SPLASHSCREEN_FILE_END = (int32_t) 4,
};
typedef enum e_FLR_SPLASHSCREEN_FILETYPE_E FLR_SPLASHSCREEN_FILETYPE_E;

enum e_FLR_SYSTEMSYMBOLS_SYMBOL_E {
    FLR_SYSTEMSYMBOLS_FFC_IMMINENT = (int32_t) 0,
    FLR_SYSTEMSYMBOLS_FFC_DESIRED = (int32_t) 1,
    FLR_SYSTEMSYMBOLS_TABLE_SWITCH_DESIRED = (int32_t) 2,
    FLR_SYSTEMSYMBOLS_LOW_GAIN = (int32_t) 3,
    FLR_SYSTEMSYMBOLS_OVERTEMP = (int32_t) 4,
    FLR_SYSTEMSYMBOLS_SYMBOL_LAST = (int32_t) 5,
};
typedef enum e_FLR_SYSTEMSYMBOLS_SYMBOL_E FLR_SYSTEMSYMBOLS_SYMBOL_E;

enum e_FLR_SYSTEMSYMBOLS_ID_TYPE_E {
    FLR_SYSTEMSYMBOLS_ELEMENT = (int32_t) 0,
    FLR_SYSTEMSYMBOLS_GROUP = (int32_t) 1,
    FLR_SYSTEMSYMBOLS_ID_LAST = (int32_t) 2,
};
typedef enum e_FLR_SYSTEMSYMBOLS_ID_TYPE_E FLR_SYSTEMSYMBOLS_ID_TYPE_E;

enum e_FLR_SYSTEMSYMBOLS_STATE_E {
    FLR_SYSTEMSYMBOLS_ENTERED = (int32_t) 0,
    FLR_SYSTEMSYMBOLS_EXITED = (int32_t) 1,
    FLR_SYSTEMSYMBOLS_STATE_LAST = (int32_t) 2,
};
typedef enum e_FLR_SYSTEMSYMBOLS_STATE_E FLR_SYSTEMSYMBOLS_STATE_E;

#endif //ENUM_TYPES_H
