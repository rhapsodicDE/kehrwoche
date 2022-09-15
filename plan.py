
print("""

<style>
body{
	font-family: Arial;
	font-size: 0.5em;
}
.monthName {
	font-weight: bold;
	text-align: center;
	font-size: 1.5em;
}
.dayContainer {
}
.day {
	border: 1px solid #999;
}
.sunday {
	background-color: orange;
}
.saturday {
	background-color: yellow;
}
.monthContainer {
	width: 3cm;
	position: absolute;
}
.partei {
	position: absolute;
	font-size: 50px;
	font-weight: bold;
	margin-left: 1.0cm;
	text-shadow: -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white;
}

.restBio {
	background-color: green;
	color: white;
}
.papierGelb {
	background-color: darkred;
	color: white;
}
.legendBox {
	position: absolute;
	margin-left: 5.75cm;
}
.legend {
	position: absolute;
	color: white;
	font-weight: bold;
	border: 1px solid #999;
	padding: 4px;
	text-align: center;
	width: 2cm;
}
.legendRed {
	background-color: darkred;
}
.legendGreen {
	background-color: green;
}
</style>

""")

months = [['Januar', 31], ['Februar', 28], ['M&auml;rz', 31], ['April', 30], ['Mai', 31], ['Juni', 30],
	['Juli', 31], ['August', 31], ['September', 30], ['Oktober', 31], ['November', 30], ['Dezember', 31]]

days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
parteien = ["2", "2a", "3", "3a"]

# first element of array is day of month, second is month (starting at 1)
restBio = [[5, 1], [19, 1],
	[2,2], [16,2],
	[2,3], [16,3], [30,3],
	[12,4], [27,4],
	[11,5], [25,5],
	[9,6], [22,6],
	[6,7], [20,7],
	[3,8], [18,8], [31,8], 
	[15,9], [28,9], 
	[12,10], [26,10],
	[9,11], [23,11],
	[7,12], [21,12]]

papierGelb = [
	[3,1], [1,2], [1,3], [29, 3], [29, 4],
	[27,5], [28,6], [28,7], [24,8],
	[21,9], [20,10], [18,11], [16,12]
	]

def isSpecialDay(specials, day, month):
	for spec in specials:
		if spec[0] == day and spec[1] == month:
			return 1
	return 0

# first day of week of the year
dayOfWeek = 5
monthCount = 1
partei = 0
deferred = 0 # needs to be global to work between June and July

def printPage(rng):

	global monthCount, dayOfWeek, partei, month, deferred

	print('<div style="height: 10.5cm;">')
	print('<div class="legendBox">')
	print('<div class="legend legendRed">Papier/gelber Sack</div>')
	print('<div class="legend legendGreen" style="margin-left: 2.5cm;">Restm&uuml;ll/Bio</div>')
	print('</div>')
	print('<h1>Kehrwoche 2022</div>')
	print('</div>')

	for r in rng:
		name = months[r][0]
		dayCount = months[r][1]

		print('<div class="monthContainer" style="top: '+str(((rng[0]/6)*12)+1.15)+'cm; position: absolute; left: '+str((((monthCount-1)%6)*3))+'cm;">')
		print('<div class="monthName">'+name+'</div>')
		print('<div class="dayContainer">')
		for day in range(dayCount):

			# firstWeekOfYear is an exception for the first week of the year;
			# a house number should be shown for January if the year does not start
			# with a Monday or Tuesday
			firstWeekOfYear = r == 0 and dayOfWeek >= 2 and day == 0
			if dayOfWeek == 0 or firstWeekOfYear:
				# no exception for December, otherwise an item is missing
				if day >= 27 and r != 11:
					deferred = 1
				else:
					print('<div class="partei">'+parteien[partei%len(parteien)]+'</div>')
					partei = partei + 1
			if day == 0 and deferred == 1:
				print('<div class="partei">'+parteien[partei%len(parteien)]+'</div>')
				partei = partei + 1
				deferred = 0


			clazz = 'day'
			if dayOfWeek == 5:
				clazz = clazz + ' saturday'
			if dayOfWeek == 6:
				clazz = clazz + ' sunday'

			if isSpecialDay(restBio, day+1, monthCount):
				clazz = clazz + ' restBio'
			if isSpecialDay(papierGelb, day+1, monthCount):
				clazz = clazz + ' papierGelb'

			print('<div class="'+clazz+'">'+str(day+1)+" "+(days[dayOfWeek])+'</div>')
			dayOfWeek = (dayOfWeek + 1) % 7
		print('</div>')
		print('</div>')
		monthCount = monthCount + 1


print('<div>')
printPage(range(0,6))
print('</div>')
print('<br><br>')
print('<br><br>')
print('<div>')
printPage(range(6,12))
print('</div>')
