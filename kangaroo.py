"""
Create a Kangaroo class as a cautionary tale against a common mistake
"""

class Kangaroo:
    def __init__(self, name=None, contents=None):
        """
        Default values are only assigned once, when the function is read
        So mutable variables will be shared across all instances
        To avoid, we set the default to None then see if we need to create a new list
        """
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents
    
    def put_in_pouch(self, item):
        self.pouch_contents.append(item)
    
    def __str__(self):
        t = [f'{self.name} has this in their pouch:']
        for obj in self.pouch_contents:
            s = object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
        
def main():

    kanga = Kangaroo('Kanga')
    roo = Kangaroo('Roo')

    kanga.put_in_pouch('pouchy_thing')
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)

main()