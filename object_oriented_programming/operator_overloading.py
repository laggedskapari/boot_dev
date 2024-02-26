class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == other == 'bronze':
            return 'iron'
        if self.sword_type == other == 'iron':
            return 'steel'
        if self.sword_type != other:
            raise ValueError('can not craft')
