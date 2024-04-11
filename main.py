import os, shutil
import wget
import subprocess


URL = '' # URL удален по соображеним безопасности 
NAME_LIST = ['1.Appx', '2.Appx', '3.Appx', '4.Appx', '5.Appx', '0.Msixbundle']
DIR = r'C:\WA_Install'


def install():
    for name in NAME_LIST:
        url = f'{URL}{name}'
        dir = f'{DIR}\{name}'
        wget.download(url, dir)
        command = f'add-appxpackage –path "{dir}"'
        proc = subprocess.Popen(['powershell', '-Command', command], stdout=subprocess.PIPE)
        output, errors = proc.communicate()
        if errors:
            print("Errors:", errors.decode('utf-8'))
        os.remove(dir)
    print('\nУдаление файлов установки...')
    shutil.rmtree(DIR)
    print('Удалено')


def create_whatsapp_ink():
    print('Создание ярлыка...')
    file = 'WhatsApp-TEST.txt'
    real_file = 'WhatsApp.lnk'
    url = f'{URL}{file}'
    desktop = os.path.expanduser('~/Desktop')
    dir = os.path.join(desktop, os.path.basename(file))
    real_dir = os.path.join(desktop, os.path.basename(real_file))
    try:
        os.remove(real_dir)
        os.remove(dir)
    except:
        None
    wget.download(url, dir)
    os.rename(dir, real_dir)
    print('\nЯрлык создан!')


os.system('color')
release = os.sys.getwindowsversion()
build = int(str(release.build)[:4])


if build >= 1836:
    try:
        shutil.rmtree(DIR)
    except:
        None
    os.mkdir(DIR)
    command = r'Get-AppxPackage *whatsapp* | Remove-AppxPackage'
    proc = subprocess.Popen(['powershell', '-Command', command], stdout=subprocess.PIPE)
    print('\033[1m' + '\033[93m' + 'Устанавливаю всё необходимое, откинься на спинку кресла и отдохни' + '\033[0m')
    install()
    create_whatsapp_ink()
    input('\033[1m' + '\033[32m' + '\n\nУстановка завершена! WhatsApp можно найти в меню "Пуск" или на рабочем столе. Закрой окно программы для завершения. Хорошего дня! :)' + '\033[0m')
else:
    print(f'System build: {build}')
    input('\033[1m' + '\033[91m' + 'К сожалению Whatsapp не поддерживается версией твоей ОС Windows :( Обратись в канал ~itquestions')
