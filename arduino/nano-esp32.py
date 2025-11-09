from machine import Pin, UART, SPI

'''
a tiny piece of code to abstract your micropython-esp32 pin names and use the pins on-board
rather than having to search online each time
'''

keymap = {
    'D0': Pin(44),
    'D1': Pin(43),
    
    'D2': Pin(5),
    'D3': Pin(6),
    'D4': Pin(7),
    'D5': Pin(8),
    'D6': Pin(9),
    'D7': Pin(10),
    'D8': Pin(17),
    'D9': Pin(18),
    'D10': Pin(21),
    'D11': Pin(38),
    'D12': Pin(47),
    
    'D13': Pin(48),
    'D14': Pin(46),
    'D15': Pin(0),
    'D16': Pin(45),
    
    'D17': Pin(1),
    'D18': Pin(2),
    'D19': Pin(3),
    'D20': Pin(4),
    'D21': Pin(11),
    'D22': Pin(12),
    'D23': Pin(13),
    'D24': Pin(14),
    
    'A0': Pin(1),
    'A1': Pin(2),
    'A2': Pin(3),
    'A3': Pin(4),
    'A4': Pin(11),
    'A5': Pin(12),
    'A6': Pin(13),
    'A7': Pin(14),

    #  onboard RGB LED pins:
    'LED_R': Pin(46),
    'LED_G': Pin(0),
    'LED_B': Pin(45),

    # Onboard LED data line:
    'LED_BUILTIN': Pin(48),   
}

# Example usage:
# led = PinMap['D13']
# led.init(Pin.OUT)
# led.value(1)
PinMap = keymap
