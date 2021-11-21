_mytrans_dict = {
    'Sistemi Operativi' : {'en':'Operating Systems'},
    'Osservazione' : {'en':'Observation'},
    'Domanda' : {'en':'Question'},
}

_mylanguage = 'it'

def init_mylang(lang):
	global _mylanguage
	_mylanguage = lang	

def mytranslate(string):
	if string not in _mytrans_dict:
		return string
	if _mylanguage not in _mytrans_dict[string]:
		return string
	return _mytrans_dict[string][_mylanguage]

