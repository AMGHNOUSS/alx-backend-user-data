#!/usr/bin/env python3
"""
Module for handling Personal Data
"""

import re


def filter_datum(ields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
