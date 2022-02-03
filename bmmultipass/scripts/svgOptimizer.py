EXTRAS = False;

def main():



    svg = '''
SA/RA
'''


    # # Green Border
    # svg = '''<rect style = "opacity:0.6;mix-blend-mode:normal;fill:none;stroke:#0b9100;stroke-width:15;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;paint-order:normal" id = "rect926" width = "315" height = "315" x = "17" y = "17" / >
    #     <rect style = "opacity:0.33;mix-blend-mode:normal;fill:none;stroke:#0b9100;stroke-width:1.82496;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;paint-order:normal" id = "rect926-4" width = "288" height = "288" x = "31" y = "31" / >'''
    #
    # # White Checkmark
    # svg = '''<path style="fill:none;stroke:#ffffff;stroke-width:15;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" d="m 139,238 20.4,23.7 56.9,-56.6" id="path3787" sodipodi:nodetypes="ccc" />'''
    #
    # # Green Background
    # svg = '''<rect style="opacity:0.33;fill:#157700;fill-opacity:0.33;stroke:#0b9100;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;paint-order:normal" width="350" height="350" x="0" y="0" />'''

    # Necessary
    svg = svg.replace('"', "'")
    svg = svg.replace('%', "%25")
    svg = svg.replace('#', "%23")
    svg = svg.replace('{', "%7B")
    svg = svg.replace('}', "%7D")
    svg = svg.replace('<', "%3C")
    svg = svg.replace('>', "%3E")
    # easier to create a dictionary and replace it that way, but..

# Maybes
    if EXTRAS:
        svg = svg.replace('|', "%7C")
        svg = svg.replace('[', "%7B")
        svg = svg.replace(']', "%5D")
        svg = svg.replace('^', "%5E")
        svg = svg.replace('`', "%60")
        svg = svg.replace(';', "%3B")
        svg = svg.replace('?', "%3F")
        svg = svg.replace(':', "%3A")
        svg = svg.replace('@', "%40")
        svg = svg.replace('=', "%3D")

    print(f'Final: \n{svg}')

main()
