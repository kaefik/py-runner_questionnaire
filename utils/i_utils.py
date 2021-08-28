"""
 my ulitites
 Author: Ilnur Sayfutdinov
 E-mail: ilnursoft@gmail.com
"""
from typing import Optional

import re


def validate_url(raw_text: str) -> Optional[str]:
    """
    валидация и выделение из текста урл
    param: raw_text - входящий текст
    return: если не соответствует урл, то возвращается None, иначе возвращается сам урл
    """
    rexp_http_url: str = r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"

    # выделение урл из общей массы сообщения
    match = re.search(rexp_http_url, raw_text)
    if not match:
        return None
    url = match.group()
    return url
