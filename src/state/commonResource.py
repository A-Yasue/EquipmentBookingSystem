#!/usr/bin/env python


class CommonResource():
    ENQUIRY_INVALID = ""
    ENQUIRY_BORROW = "0"
    ENQUIRY_RETURN = "1"
    ENQUIRY_UPDATE = "2"

    employeeId = ""                 # 社員番号
    enquiry = ENQUIRY_INVALID       # 問い合わせ内容
    expirationDate = ""

    @staticmethod
    def initialize():
        CommonResource.employeeId = ""                 # 社員番号
        CommonResource.enquiry = CommonResource.ENQUIRY_INVALID       # 問い合わせ内容
        CommonResource.expirationDate = ""
