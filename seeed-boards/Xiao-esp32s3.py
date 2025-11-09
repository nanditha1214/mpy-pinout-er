from machine import Pin, UART, SPI

'''
XIAO ESP32S3 pin naming helper

'''

keymap = {

    
    # D name     ||||   A Name      |||  T name      |||   Comm Name
    
    'D0': Pin(1),      'A0': Pin(1),   'T0': Pin(1),
    'D1': Pin(2),      'A1': Pin(2),   'T1': Pin(2),
    'D2': Pin(3),      'A2': Pin(3),   'T2': Pin(3),
    'D3': Pin(4),      'A3': Pin(4),   'T3': Pin(4),
    'D4': Pin(5),      'A4': Pin(5),   'T4': Pin(5),      'SDA': Pin(5),
    'D5': Pin(6),      'A5': Pin(6),   'T5': Pin(6),      'SCL': Pin(6),

    'D6': Pin(43),     'A6': Pin(43),                     'TX': Pin(43),
    'D7': Pin(44),     'A7': Pin(44),                     'RX': Pin(44),

    'D8': Pin(7),      'A8': Pin(7),   'T7': Pin(7),      'SCK':  Pin(7),
    'D9': Pin(8),      'A9': Pin(8),   'T8': Pin(8),      'MISO': Pin(8),
    'D10': Pin(9),     'A10': Pin(9),  'T9': Pin(9),      'MOSI': Pin(9),
    'D11': Pin(42),    'A11': Pin(42), 'T12': Pin(42),
    'D12': Pin(41),    'A12': Pin(41), 'T13': Pin(41),
                                    

}

