import os

ELEMENT_IMAGES = {}

def init_config(script_path):
    script_dir = os.path.dirname(script_path)

    ELEMENT_IMAGES['Gate 1'] = os.path.join(script_dir, 'Icons', 'gate_and.png')
    ELEMENT_IMAGES['Gate 2'] = os.path.join(script_dir, 'Icons', 'gate_and.png')
    