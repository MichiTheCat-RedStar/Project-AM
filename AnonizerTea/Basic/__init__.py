try: from . import Base64
except ModuleNotFoundError: raise ModuleNotFoundError('Не найден модуль Base64 в ./Basic.')

try: from . import Binary
except ModuleNotFoundError: raise ModuleNotFoundError('Не найден модуль Binary в ./Basic.')

try: from . import Caesars
except ModuleNotFoundError: raise ModuleNotFoundError('Не найден модуль Caesars в ./Basic.')

try: from . import Hash
except ModuleNotFoundError: raise ModuleNotFoundError('Не найден модуль Hash в ./Basic.')

try: from . import Bytes
except ModuleNotFoundError: raise ModuleNotFoundError('Не найден модуль Bytes в ./Basic.')
