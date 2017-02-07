def data_type(var):
	
	var_type =type(var)
	if var_type == str:
		return len(var)
	elif var_type ==bool:
		return var
	elif var_type ==int:
		if var == 100:
			return 'equal to 100'
		elif var < 100:
			return 'less than 100'

		else:
			return 'more than 100'

	elif var_type ==list:
		try:
			if var[2]:
				return var[2]
		except(IndexError):
			return None
	else:
		return 'no value'