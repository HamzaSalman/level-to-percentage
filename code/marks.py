
print 'enter grade'
grade = raw_input()
str(grade)

marks = {}
marks['4+'] = '97'
marks['4'] = '90'
marks['4-'] = '83'
marks['3+'] = '76'
marks['3'] = '74'
marks['3-'] = '71'
marks['2+'] = '68'
marks['2'] = '64'
marks['2-'] = '61'
marks['1+'] = '58'
marks['1'] = '54'
marks['r'] = '30'
marks['1-'] = '51'
marks['ne'] = '0'
marks['4++'] = '100'

if grade == '4+' or grade == '4' or grade == '4-' or grade == '3+' or grade == '3' or grade == '3-' or grade == '2+' or grade == '2' or grade == '2-' or grade == '1+' or grade == '1' or grade == '1-' or grade == 'r' or grade == 'ne' or grade == '4++':
    
    
    print 'your mark is: ' +  marks[grade] + '%'
else:
	print("You have to input level grades only!")
