# created by Yogaswara
# sh.yoganews@gmail.com

# how to use
# 1. paste the script to a folder
# 2. if the main python is in the same folder, 
#    import the script using from day_translator import dayTranslate
# 3. if the main python is in other folder, first create empty __init__.py in the same folder as this script
#    and then import the script using from folder_name.day_translator import dayTranslate
# 4. prepare the day name u want to translate as input, example following line 31

# test creating day translator using list

'''
[CHANGELOG 22 Jan 2024]
-added monthTranslate function to translate month name (%b) into Indonesian

'''
from datetime import datetime
import pandas as pd

def dayTranslate(day_name):
	# creating dictionary dataframe
	eng_day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	ina_day = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu'] # Translate for Indonesian day name from English
	list_tupple = list(zip(eng_day,ina_day))
	df = pd.DataFrame(list_tupple,columns=['eng_day','ina_day'])

	# translating the day name according to input
	dname_eng = day_name
	dname_ina = df[df.eng_day == dname_eng].ina_day.iloc[0]
	return dname_eng, dname_ina

def monthTranslate(month_name):
	# creating dictionary dataframe
	eng_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	ina_month = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'] # Translate for Indonesian day name from English
	list_tupple = list(zip(eng_month,ina_month))
	df = pd.DataFrame(list_tupple,columns=['eng_month','ina_month'])

	# translating the day name according to input
	mname_eng = month_name
	mname_ina = df[df.eng_month == mname_eng].ina_month.iloc[0]
	return mname_eng, mname_ina

# test run translate for today's day name
if __name__ == '__main__':
	now = datetime.now()
	dname_now = now.strftime('%A')
	dname_eng, dname_ina = dayTranslate(dname_now)
	print(f'Terjemahan dari {dname_eng} ke dalam bahasa Indonesia adalah {dname_ina}')
