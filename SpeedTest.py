import speedtest
import platform, os
import win10toast

def speed_test():
    try:
        st = speedtest.Speedtest()
        print("Поиск наилучшего сервера")
        server_name = st.get_best_server()
        print(f"Best server: {server_name['sponsor']} - {server_name['name']}, {server_name['country']}")
        ping = st.results.ping
        print(f"Ping: {ping}")
        download_speed = st.download() / 1024 / 1024
        print(f"Download speed: {download_speed:.2f} Mbit/s")
        upload_speed = st.upload() / 1024 / 1024
        print(f"Upload speed: {upload_speed:.2f} Mbit/s")
        result = f"Best server: {server_name['sponsor']} - {server_name['name']}, {server_name['country']} \nPing: {ping} \nDownload speed: {download_speed:.2f} Mbit/s \nUpload speed: {upload_speed:.2f} Mbit/s"
        return result
    except Exception as e:
        return "null"


def push(title, message):
    plt = platform.system()
    if plt == "Darwin":
        command = '''
        osascript -e 'display notification "{message}" with title "{title}"'
        '''
    elif plt == "Linux":
        command = f'''
        notify-send "{title}" "{message}"
        '''
    elif plt == "Windows":
        win10toast.ToastNotifier().show_toast(title, message)
        return
    else:
        return
    os.system(command)

def get_internet():
    push("SpeedTest", "Результат появится в новом уведомлении...")
    print("Запуск...")
    result = speed_test()
    if result == "null":
        push("Error", "Произошла ошибка! Проверьте подключение к сети")
    else:
        push("Result", result)
    input("Нажмите любую клавишу, чтобы закрыть...")
    exit()

if __name__ == '__main__':
    get_internet()