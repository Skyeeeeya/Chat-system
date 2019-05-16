#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 07:53:43 2019

@author: shenmengjie
"""
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
def aes_encrypt(data, key):
    """aes加密函数，如果data不是16的倍数【加密文本data必须为16的倍数！】，那就补足为16的倍数
    :param key:
    :param data:
    """
    cipher = AES.new(key, AES.MODE_CBC, key)  # 设置AES加密模式 此处设置为CBC模式
    block_size = AES.block_size
    # 判断data是不是16的倍数，如果不是用b'\0'补足
    if len(data) % block_size != 0:
        add = block_size - (len(data) % block_size)
    else:
        add = 0
    data += '\0' * add
    encrypted = cipher.encrypt(data)  # aes加密
    result = b2a_hex(encrypted).decode()  # b2a_hex encode  将二进制转换成16进制
    return result


def aes_decode(data, key):
    """aes解密
    :param key:
    :param data:
    """
    cipher = AES.new(key, AES.MODE_CBC, key)
    result2 = a2b_hex(data)  # 十六进制还原成二进制
    decrypted = cipher.decrypt(result2)
    return decrypted.rstrip(b'\0').decode()  # 解密完成后将加密时添加的多余字符'\0'删除

if __name__ == '__main__':  
    a = aes_encrypt("0123456789ABCDEF",'keyskeyskeyskeys')
    b = aes_decode('4a3d146ad6c7fc256093f6870991111e','keyskeyskeyskeys' )
    print(a,b)