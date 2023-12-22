from multiprocessing import Process
import os
import time

def Diplom_script():
    os.system('py Scripts/spotify_bot.py' if os.name == 'nt' else 'python3 Scripts/spotify_bot.py')

if __name__ == '__main__':
    q = Process(target=Spotify_script)
    time.sleep(2)
    q.start()
    q.join()

# read the README.md for more information
