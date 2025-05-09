init python:
    #import math

    class Photo():
        def __init__(self, filename, vertical=False):
            self.file = filename
            self.vertical = vertical

            if config.developer:
                if(filename is None) or (filename == ""):
                    raise Exception("Tried to create Photo object without a file.")

        def is_same_photo(self, filename):
            return self.file == filename



    def add_photo(filename: str, vertical=False):
        for photo in smartphone.photos:
            if(photo.is_same_photo(filename)):
                return
        smartphone.photos.append(Photo(filename, vertical))
