import os
import requests
import folium
from stegano import exifHeader


def ip():
	ip = input('IP ( если нажать enter, пробьёт ваш ip ): ')
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		data = {
					'[Айпи]': response.get('query'),
					'[Провайдер]': response.get('isp'),
					'[Организация]': response.get('org'),
					'[Страна]': response.get('country'),
					'[Регион]': response.get('regionName'),
					'[Город]': response.get('city'),
					'[ZIP]': response.get('zip'),
					'[Широта]': response.get('lat'),
					'[Долгота]': response.get('lon'),
		        }

		info = ''
		mapp = folium.Map(location=[response.get('lat'),response.get('lon')])
		mapp.save(f'{response.get("query")}.html')
		for k, v in data.items():
			info += f'{k} :: {v}\n'

		print(f'{info}\nКарта находится в файле: {response.get("query")}.html')
		main()
	except:
		print('Ошибка')
		main()


def enc_pict():
	print('''1) Перенесите в папку "@sblro4eeek" (Путь : /storage/emulated/0/@sblro4eeek) фотографию
2) Следуйте указаниям :3''')
	image = input('Имя фотографии в которую шифруем: ')
	txt = input('Текст который шифруем: ')
	try:
		sng = exifHeader.hide(f'/storage/emulated/0/@sblro4eeek/{image}', f'/storage/emulated/0/@sblro4eeek/crp_{image}', txt)
		print(f'Успешно! Текст зашифрован в фотографию\n /storage/emulated/0/@sblro4eeek/crp_{image}')
		main()

	except:
		print('Произошла ошибка(')
		main()

def dec_pict():
	image = input('Имя фотографии которую дешифруем: ')
	try:
		de = (exifHeader.reveal(f'/storage/emulated/0/@sblro4eeek/{image}')).decode()
		f = open('pict.txt','a')
		f.write(de)
		f.close(	)
		print(f'Успешно! Текст дешифрован из фотографии\n /storage/emulated/0/@sblro4eeek/pict.txt')
		main()

	except Exception as _ex:
		print('Произошла ошибка(')
		main()



def main():
	menu = int(input('''[1] Пробив IP
[2] Шифрование текста в фото 
[Ваш выбор] '''))
	if menu == 1:
		ip()
	elif menu == 2:
		pict = int(input('''[1] Зашифровать
[2] Расшифровать
[Ваш выбор] '''))
		if pict == 1:
			enc_pict()
		elif pict == 2:
			dec_pict()
		else:
			print('Проверьте правильность ввода')
	else:
		print('Проверьте правильность ввода')


if __name__ == '__main__':
	os.mkdir('/storage/emulated/0/@sblro4eeek')
	os.system('cls' if os.name == 'nt' else 'clear')
	print('''
      _     _          _  _                 _    
     | |   | |        | || |               | |   
  ___| |__ | |_ __ ___| || |_ ___  ___  ___| | __
 / __| '_ \| | '__/ _ \__   _/ _ \/ _ \/ _ \ |/ /
 \__ \ |_) | | | | (_) | | ||  __/  __/  __/   < 
 |___/_.__/|_|_|  \___/  |_| \___|\___|\___|_|\_\
			
			''')
	main()