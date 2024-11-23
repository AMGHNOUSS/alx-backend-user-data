#!/usr/bin/env python3
"""
Module for handling Personal Data
"""

import re


def filter_datum(fields, redaction, message, separator):
    """ Returns a log message obfuscated """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',f'{f}={redaction}{separator}', message)
    return message
