import speedtest
import platform, os
import win10toast

def speed_test():
    st = speedtest.Speedtest()
    server_name = st.get_best_server()

    ping = st.results.ping
    download_speed = st.download() / 1024 / 1024
    upload_speed = st.upload() / 1024 / 1024

    result = f"Best server: {server_name['sponsor']} - {server_name['name']}, {server_name['country']} \nPing: {ping} \nDownload speed: {download_speed:.2f} Mbit/s \nUpload speed: {upload_speed:.2f} Mbit/s"
    return result

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

def main():
    push("SpeedTest", "Результат появится в новом уведомлении...")
    result = speed_test()
    push("Result", result)



if __name__ == '__main__':
    main()

