import os
import errno
import json

class Cache(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
        self.filename = 'cache_json.json'
        try:
            file_handle = os.open(os.path.join(self.BASE_DIR, self.filename), flags)
        except OSError as e:
            if e.errno == errno.EEXIST:  # Failed as the file already exists.
                pass
            else:  # Something unexpected went wrong so reraise the exception.
                raise
        else:
            with os.fdopen(file_handle, 'w') as file_obj:
                pass

    def _convert(self):
        read_file = open(os.path.join(self.BASE_DIR, self.filename), 'r')
        data = read_file.read()
        if not data:
            data = '{"default": "None"}'
        return json.loads(data)

    def set(self, var, value):
        object = self._convert()
        self.file = open(os.path.join(self.BASE_DIR, self.filename), 'w+')
        object[var] = value
        json_object = json.dumps(object)
        self.file.write(json_object)
        self.file.close()
        return True
        
    def get(self, var):
        object = self._convert()
        return object.get(var)
