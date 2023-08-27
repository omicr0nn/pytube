# Creator by omicr0nn
# Creator by omicr0nn
import os
from pytube import YouTube
from colorama import Fore, Style
from os import system

MENU = """{}
----------- Video Downloader App --------------
{}1. Convert to MP3
{}2. Convert to MP4
{}3. Contact İnfo
{}4. Exit
{}-----------------------------------------------{}
""".format(Fore.LIGHTMAGENTA_EX, Fore.RED, Fore.RED, Fore.GREEN, Fore.LIGHTWHITE_EX, Fore.LIGHTMAGENTA_EX, Fore.RESET)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def convert_to_mp3(video_url, output_folder):
    try:
        yt = YouTube(video_url)

        current_directory = os.getcwd()
        output_path = os.path.join(current_directory, output_folder, f"{yt.title}.mp3")

        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_folder)

        old_file_path = os.path.join(output_folder, audio_stream.default_filename)
        new_file_path = os.path.join(output_folder, f"{yt.title}.mp3")
        os.rename(old_file_path, new_file_path)

        print(Fore.GREEN + "[+] Video download and conversion complete:", new_file_path + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "[-] Hata (URL: {}):".format(video_url), e + Fore.RESET)

def convert_to_mp4(video_url, output_folder):
    try:
        yt = YouTube(video_url)

        current_directory = os.getcwd()
        output_path = os.path.join(current_directory, output_folder, f"{yt.title}.mp4")

        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_folder)

        print(Fore.GREEN + "[+] Video download complete:", output_path + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "[-] Hata (URL: {}):".format(video_url), e + Fore.RESET)

def show_contact_info():
    system("cls||clear")
    print("\n--- İ N F O ---")
    print("GitHub: " + Fore.GREEN + "github.com/omicr0nn" + Fore.RESET)

def main():
    input_file = "links.txt"
    mp3_output_folder = "mp3"
    mp4_output_folder = "mp4"

    if not os.path.exists(mp3_output_folder):
        os.makedirs(mp3_output_folder)

    if not os.path.exists(mp4_output_folder):
        os.makedirs(mp4_output_folder)

    while True:
        clear_console()
        print(MENU)
        choice = input("{}Please enter an option (1/2/3/4): ".format(Fore.RED))

        if choice == "1":
            with open(input_file, "r") as file:
                video_urls = file.readlines()

            for url in video_urls:
                url = url.strip()
                if url:
                    convert_to_mp3(url, mp3_output_folder)

        elif choice == "2":
            with open(input_file, "r") as file:
                video_urls = file.readlines()

            for url in video_urls:
                url = url.strip()
                if url:
                    convert_to_mp4(url, mp4_output_folder)

        elif choice == "3":
            show_contact_info()

        elif choice == "4":
            system("cls||clear")
            print("""
 {}Thank you for choosing us.
 {}Exiting...{}
                  """.format(Fore.LIGHTWHITE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            break

        input("\n{}Press Enter to return".format(Fore.GREEN))

if __name__ == "__main__":
    main()

# Coding by omicr0n

# Coding by omicr0n
