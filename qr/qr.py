#!/usr/bin/env python3
import qrcode

img = qrcode.make(input("Link: "))
img.save("qrcode.png")
