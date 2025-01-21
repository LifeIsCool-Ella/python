import mss
from time import perf_counter as T
left  = 0
right = 2
top   = 0
btm   = 2

with mss.mss() as sct:
    # parameter for sct.grab() can be:
    monitor = sct.monitors[1]         # entire screen
    bbox    = (left, top, right, btm) # screen part to capture

    sT=T()
    sct_im = sct.grab(bbox) # type: <class 'mss.screenshot.ScreenShot'>
    eT=T();print(" >", eT-sT) #  > 0.0003100260073551908

    print(len(sct_im.raw), sct_im.raw)
    # 16 bytearray(b'-12\xff\x02DU\xff-12\xff"S_\xff')

    print(len(sct_im.rgb), sct_im.rgb)
    # 12 b'21-UD\x0221-_S"'